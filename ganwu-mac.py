import pyautogui
import pyperclip
import time
import requests
import schedule

def job():
    print("开始执行定时任务...")
    target_user = "鼎驰科技"  # 企业微信联系人
    message_content = get_message()
    if send_wechat_message(target_user, message_content):
        print(f"消息发送成功: {message_content}")
    else:
        print("消息发送失败，请手动检查")

def get_message():
    """调用API获取消息内容"""
    response = requests.get("https://v1.jinrishici.com/rensheng.txt", timeout=5)
    response.raise_for_status()
    return "感悟：" + response.text.strip()

def send_wechat_message(user_name, message):
    """在 macOS 企业微信上发送消息"""
    try:
        # 打开或切换到企业微信
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.hotkey('command', 'y')
        time.sleep(2)  # 等待企业微信激活

        # 聚焦搜索框 (Command + Option + F)
        pyautogui.hotkey('command', 'f')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        # 输入联系人名
        pyperclip.copy(user_name)
        pyautogui.hotkey('command', 'v')
        time.sleep(1)
        pyautogui.press('enter')  # 打开聊天
        time.sleep(1)

        # 输入消息并发送
        pyperclip.copy(message)
        pyautogui.hotkey('command', 'v')
        pyautogui.press('enter')
        time.sleep(1)

        # 最小化窗口 (可选)
        pyautogui.hotkey('command', 'm')

        return True
    except Exception as e:
        print(f"发送失败: {str(e)}")
        return False

# 定时每天早上 08:00 执行
schedule.every().day.at("08:00").do(job)

if __name__ == "__main__":
    print("等待定时任务执行...")
    # send_wechat_message("小小", "测试消息")
    while True:
        schedule.run_pending()
        time.sleep(60)
