from common import *
#solo刷塔

monster_location = (965, 530)
skill1 = (980, 704)
skill2 = (1097, 704)
skill3 = (980, 760)
skill4 = (1097, 760)

skill_order = [[3,2,2], [2,2,3], [3,2,3,3], [3,2,3], [3,2,3], [2,2,3], [3,2,3], [2,2,3], [2,2,3,3]]

def click_skill(x):
    if x == 1:
        move_and_click_func(skill1)
    elif x == 2:
        move_and_click_func(skill2)
    elif x == 3:
        move_and_click_func(skill3)
    elif x == 3:
        move_and_click_func(skill4)
    else:
        print('error')

def do_fight(order):
    print(">>> 进入战斗中...")

    # 点击胜利按钮
    while not find_and_click("./ui/confirm.png"):

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底
        if len(order) == 4:
            click_skill(order[0])
            time.sleep(4.5)
            click_skill(order[1])
            time.sleep(3.3)
            click_skill(order[2])
            time.sleep(3.3)
            click_skill(order[3])
            time.sleep(4.5)
        else:
            click_skill(order[0])
            time.sleep(3.3)
            click_skill(order[1])
            time.sleep(3.3)
            click_skill(order[2])
            time.sleep(4.5)

    confirm_func()

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
    heal_round = 3
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
        while not find_and_click("./tower_ui/31floor.png", confidence=0.9):
            a = 1
        time.sleep(0.5)
        
        while count < 9: 

            move_and_click_func(monster_location)
            if find_image("./ui/battle_confirm.png", timeout=3):
                time.sleep(3)  # 等待进入战斗

                do_fight(skill_order[count])
                count += 1
                if count % heal_round == 0 or count == 9:
                    do_heal()
                
                print(">>> 一轮完成，准备下一轮...\n")
        find_and_click('./tower_ui/exit.png', confidence=0.9)
        count = 0


if __name__ == "__main__":
    main()