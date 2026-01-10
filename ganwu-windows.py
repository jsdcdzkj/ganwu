import pyautogui
import pyperclip
import time
import requests
import schedule
import time

def job():
    print("开始执行定时任务...")
    # target_user = "【软件事业部】张兆吉"  # 微信好友备注名
    target_user = "鼎驰科技"  # 微信好友备注名
    message_content = get_message()
    if send_wechat_message(target_user, message_content):
        print(f"消息发送成功: {message_content}")
    else:
        print("消息发送失败，请手动检查")


def get_message():
    """调用API获取消息内容"""
    """
        接口：https://v1.hitokoto.cn/?c=d&c=k&encode=text
        随机一句诗：https://v1.jinrishici.com/rensheng.txt
        随机一句话：https://api.kekc.cn/api/yiyan
        随机一句话：https://api.kekc.cn/api/wawr
        随机一句情话：https://api.uomg.com/api/rand.qinghua
        随机一句舔狗语录：http://api.kekc.cn/api/tiangou
    """
    response = requests.get("https://v1.jinrishici.com/rensheng.txt", timeout=5)
    # response = requests.get("https://api.uomg.com/api/rand.qinghua", timeout=5)
    response.raise_for_status()
    return "感悟：" + response.text

def send_wechat_message(user_name, message):
    """向指定微信用户发送消息"""
    try:
        # 打开微信 (需提前设置微信快捷键为Ctrl+Alt+W)
        pyautogui.hotkey('shift', 'alt', 'ctrl', 's')
        time.sleep(2)  # 等待窗口加载

        # 激活搜索框
        # pyautogui.hotkey('ctrl', 'alt','f')
        pyautogui.hotkey('shift', 'alt', 'ctrl', 'f')
        time.sleep(2)

        # 输入用户名
        pyperclip.copy(user_name)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)  # 等待搜索结果

        # 选择用户
        pyautogui.press('enter')
        time.sleep(2)

        # 输入并发送消息
        pyperclip.copy(message)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(2)

        # 关闭微信窗口
        pyautogui.hotkey('shift', 'alt', 'ctrl', 's')
        return True
    except Exception as e:
        print(f"发送失败: {str(e)}")
        return False

schedule.every().day.at("08:00").do(job)

if __name__ == "__main__":
    print("等待定时任务执行...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # 每分钟检查一次