import pyautogui
import time
from pyautogui import ImageNotFoundException
import keyboard  # 引入库
from common import confirm_func, find_and_click, find_image

#嘟咕噜带刷塔

monster_location = (965, 530)
skill1 = (980, 704)
skill2 = (1097, 704)
skill3 = (980, 760)
skill4 = (1097, 760)
run = (1353, 765)
switch = (1257, 766)
third_monster_location = (1025, 684)
go_out = (847, 786)
in_tower_my_location = (930, 440)
heal_location = (973, 390)

def click(x,y):
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.mouseDown()
    time.sleep(0.05)  # 停留一点点
    pyautogui.mouseUp()
    print(f"[点击] ({x} {y})")

def do_fight(skill):
    print(">>> 进入战斗中...")
    c = 0
    # 点击胜利按钮
    while not find_image("./ui/confirm.png"):

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底
        
        while not find_and_click("./skills/dugulu/150.png",confidence=0.9999):
            x = c
        pyautogui.moveTo(x = 1000, y = 500, duration=0.1)
        time.sleep(2)
        while not find_and_click("./skills/dugulu/120.png",confidence=0.9999):
            x = c  
        pyautogui.moveTo(x = 1000, y = 500, duration=0.1)
        time.sleep(2) 
        
        while not find_and_click("./ui/go_out.png",confidence=0.99):
            while not find_and_click("./switch_icon/shanguangpipi.png",confidence=0.8):
                while not((not find_and_click("./ui/switch.png", confidence=0.999))):
                    x = c 
                pyautogui.mouseDown()
                time.sleep(0.05)  # 停留一点点
                pyautogui.mouseUp()
            pyautogui.mouseDown()
            time.sleep(0.05)  # 停留一点点
            pyautogui.mouseUp()

        time.sleep(3)
        while not find_image("./ui/confirm.png"):
            find_and_click(skill, confidence=0.9)   
            pyautogui.moveTo(x = 1000, y = 500, duration=0.1)


    confirm_func()

def do_all_heal():
    '''
    try:
        location = pyautogui.locateCenterOnScreen("./tower_ui/seer.png", confidence=0.7)
    except ImageNotFoundException:
        location = None
    if location == None:
        location = pyautogui.locateCenterOnScreen("./tower_ui/seer2.png", confidence=0.9)
    '''
    while not find_and_click("./tower_ui/heal.png",confidence=0.9):
        pyautogui.moveTo(in_tower_my_location[0], in_tower_my_location[1], duration=0.1)
        time.sleep(0.1)
    
    time.sleep(0.5)
    confirm_func()
    print("complete heal")
'''
def do_all_heal(): ation=0.2)
    time.sleep(0.3)
    click(heal_location[0], heal_location[1]) 
    if find_and_click("./tower_ui/bag.png"):
        time.sleep(0.5)
        if find_and_click("./ui/heal.png", confidence=0.8):
            time.sleep(0.5) 
            if find_and_click("./ui/confirm.png"):
                time.sleep(0.5)
        find_and_click("./ui/x.png")  # 关闭背包或返回
        time.sleep(0.5)
    else:
        print(">>> 找不到背包按钮，跳过恢复")
'''

round = 10
heal_round = 4
skill1 = r'./skills/shanguangpipi/120.png'
skill2 = r'./skills/shanguangpipi/120.png'

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
        
        while count < round:

            click(monster_location[0], monster_location[1])
            if find_image("./ui/battle_confirm.png", timeout=3):
                time.sleep(3)  # 等待进入战斗
                if count == 2:
                    do_fight(skill2)
                else:
                    do_fight(skill1)
                count += 1
                if count % heal_round == 0 or count == round:
                    do_all_heal()
                
                print(">>> 一轮完成，准备下一轮...\n")
        find_and_click('./tower_ui/exit.png', confidence=0.9)
        count = 0 


if __name__ == "__main__":
    main()