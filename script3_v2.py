import pyautogui
import time
from pyautogui import ImageNotFoundException
import keyboard  # 引入库
from common import *

#嘟咕噜带刷塔

def do_fight(skill, location):
    print(">>> 进入战斗中...")
    c = 0
    # 点击胜利按钮
    
    move_and_click_func(monster_location)
    time.sleep(2)
 
    move_and_click_func(skill3)
    time.sleep(2.5)
    
    move_and_click_func(skill2)
    time.sleep(2.5)
    
    while not find_image('./ui/switch.png', confidence=0.99):
        move_and_click_func(switch)
        time.sleep(0.3)

    move_and_click_func(location)
    time.sleep(0.3)

    move_and_click_func(go_out)
    time.sleep(2)

    while not find_image("./ui/confirm.png"):
        move_and_click_func(skill)   
        
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
        move_and_click_func(move_location)
        pyautogui.moveTo(shake_location[0], shake_location[1], duration=0.1)
  
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
property = 'x' #'lightning' #or ground 
location = second_monster_location

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

            move_and_click_func(monster_location)
            if find_image("./ui/battle_confirm.png", timeout=3):
                time.sleep(1.2 )  # 等待进入战斗
                if property == 'ground':
                    print("ground")
                    if count == 2:
                        do_fight(skill2, location)
                    else:
                        do_fight(skill3, location)
                elif property == 'lightning':
                    print("lightning and {count}")
                    if count == 0 or count == 8:
                        do_fight(skill2, location)
                    else:
                        do_fight(skill3, location)
                else:
                    print("normal")
                    do_fight(skill2, location)
                count += 1
                if count % heal_round == 0 or count == round:
                    do_all_heal()
                
                print(">>> 一轮完成，准备下一轮...\n")
        find_and_click('./tower_ui/exit.png', confidence=0.9)
        count = 0 


if __name__ == "__main__":
    main()