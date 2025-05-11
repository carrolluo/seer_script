import pyautogui
import time
from pyautogui import ImageNotFoundException
import keyboard  # 引入库

#solo刷塔

monster_location = (965, 530)
skill1 = (980, 704)
skill2 = (1097, 704)
skill3 = (980, 760)
skill4 = (1097, 760)

def find_and_click(images, confidence=0.6, timeout=0.5):
    """
    支持传入多张图像，循环查找并点击，直到找到或超时
    """
    if isinstance(images, str):
        images = [images]  # 如果只传了一个文件名，也转为列表

    start = time.time()
    while time.time() - start < timeout:

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底

        for image in images:
            try:
                location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
            except ImageNotFoundException:
                location = None
            print(location)
            
            if location:
                x, y = location
                pyautogui.moveTo(x, y, duration=0.1)
                pyautogui.mouseDown()
                time.sleep(0.05)  # 停留一点点
                pyautogui.mouseUp()
                print(f"[点击] {image}")
                return True
        time.sleep(0.01)

    print(f"[未找到任何图像] {images}")
    return False

def click(x,y):
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.mouseDown()
    time.sleep(0.05)  # 停留一点点
    pyautogui.mouseUp()
    print(f"[点击] ({x} {y})")

def find_image(images, confidence=0.8, timeout=2):
    if isinstance(images, str):
        images = [images]

    start = time.time()
    while time.time() - start < timeout:

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底

        for image in images:
            try:
                location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
                if location:
                    print(f"[识别成功] {image} → {location}")
                    return location
            except pyautogui.ImageNotFoundException:
                continue
        time.sleep(0.01)

    print("[识别失败] 无匹配图像")
    return None

def do_fight():
    print(">>> 进入战斗中...")

    # 点击胜利按钮
    while not find_and_click("./ui/confirm.png"):

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底
        click(skill3[0], skill3[1])
        time.sleep(0.1)

    while find_image("./ui/confirm.png", timeout=0.1) or find_image("./ui/confirm2.png", timeout=0.1) or find_image("./ui/confirm3.png", timeout=0.1) or find_image("./ui/confirm4.png", timeout=0.1):

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底
        find_and_click("./ui/confirm.png", timeout=0.05)
        find_and_click("./ui/confirm2.png", timeout=0.05)
        find_and_click("./ui/confirm3.png", timeout=0.05)
        find_and_click("./ui/confirm4.png", timeout=0.05)


def do_run():
    while not find_and_click("./ui/run.png", confidence= 0.99):
        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底
        time.sleep(0.2)
    while find_image("./ui/confirm.png", timeout=0.1) or find_image("./ui/confirm2.png", timeout=0.1) or find_image("./ui/confirm3.png", timeout=0.1) or find_image("./ui/confirm4.png", timeout=0.1):

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底
        find_and_click("./ui/confirm.png", timeout=0.1)
        find_and_click("./ui/confirm2.png", timeout=0.1)
        find_and_click("./ui/confirm3.png", timeout=0.1)
        find_and_click("./ui/confirm4.png", timeout=0.1)
        time.sleep(0.1)




def do_heal():
    print(">>> 打开背包恢复中...")
    if find_and_click("./tower_ui/bag.png"): 
        time.sleep(0.1)
        if find_and_click("./ui/heal.png", confidence=0.8):
            time.sleep(0.1)
            if find_and_click("./ui/confirm.png"):
                time.sleep(0.1)
        find_and_click("./ui/x.png")  # 关闭背包或返回
        time.sleep(0.1)
    else:
        print(">>> 找不到背包按钮，跳过恢复")

def main():
    count = 0
    while True:
        
        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底
        print(">>> 开始寻找怪物...")

        while not find_and_click("./tower_ui/enter.png", confidence=0.65):
            a = 1
        time.sleep(1)
        while not find_and_click("./tower_ui/choose_floor.png", confidence=0.65):
            a = 1
        time.sleep(1)
        while not find_and_click("./tower_ui/21floor.png", confidence=0.9):
            a = 1
        time.sleep(0.5)
        
        while count < 9:

            click(monster_location[0], monster_location[1])
            if find_image("./ui/battle_confirm.png", timeout=3):
                time.sleep(2)  # 等待进入战斗

                do_fight()
                count += 1
                if count % 1 == 0 or count == 9:
                    do_heal()
                
                print(">>> 一轮完成，准备下一轮...\n")
        find_and_click('./tower_ui/exit.png', confidence=0.9)
        count = 0


if __name__ == "__main__":
    main()