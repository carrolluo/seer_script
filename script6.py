from common import *

def do_catch():
    time.sleep(1)
    find_and_click("./skills/bokeer/shouxialiuqing.png",confidence=0.8)
    pyautogui.moveTo(center_location[0], center_location[1], duration=0.1)
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(0.05)  # 停留一点点
    pyautogui.mouseUp()

    while not find_and_click("./switch_icon/lisha.png",confidence=0.8):
        while (not find_and_click("./ui/switch.png", confidence=0.8)):
            pyautogui.moveTo(center_location[0], center_location[1], duration=0.1)
            find_and_click("./ui/fight.png", confidence=0.8)
            time.sleep(0.2)
        time.sleep(0.2)
    find_and_click("./ui/go_out.png", confidence=0.9)
    time.sleep(3)

    catch_count = 1

    while not find_and_click('./ui/catch_confirm.png', confidence=0.7):
        
        while not (locate_color_strict_match('./ui/capsule.png', confidence=0.99) or locate_color_strict_match('./ui/grey_capsule.png', confidence=0.99)): 
            while not (find_and_click("./ui/prop.png", confidence=0.9) or find_and_click("./ui/prop2.png", confidence=0.9)):
                if keyboard.is_pressed('space'):
                    print("[检测到空格键，脚本终止]")
                    exit(0)  # 或者 return False, 取决于你想退出多彻底
                time.sleep(0.2)
            pyautogui.mouseDown()
            time.sleep(0.05)  # 停留一点点
            pyautogui.mouseUp()
            time.sleep(1)

        if locate_color_strict_match('./ui/grey_capsule.png', confidence=0.99):
            find_and_click('./ui/fight.png', confidence=0.99) 
            do_fight()
            break
        else:
            if catch_count % 3 == 0:
                find_and_click('./ui/middle_capsule.png', confidence=0.99)
            else:
                find_and_click('./ui/capsule.png', confidence=0.99)
        time.sleep(5)
    
        catch_count += 1



def print_func(count):
    print(f"round : {count}")

def main():
    count = 13661

    heal_round = 10

    monster_name_py = "youfu"
    monster = get_all_file_paths('./learning_ability/'+ monster_name_py)

    while True:

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")  
            exit(0)  # 或者 return False, 取决于你想退出多彻底
        print(">>> 开始寻找怪物...")
        #print(not find_image("./ui/hp.png", confidence=0.99))
        while not find_image("./ui/hp.png", confidence=0.99):
            if keyboard.is_pressed('space'):                
                print("[检测到空格键，脚本终止]")  
                exit(0)  # 或者 return False, 取决于你想退出多彻底
            find_and_click(monster, confidence=0.9) #ex:0.9 #ma: 0.6
            print_func(count)
            find_and_click("./ui/confirm.png")
        count = catch_if(monster_name_py, count)
        if count % heal_round == 0:
            do_heal()
        time.sleep(1.5)
        print(">>> 一轮完成，准备下一轮...\n")
        count += 1
        print_func(count)

if __name__ == "__main__":
    main()
    