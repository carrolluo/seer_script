from common import *

#闪皮刷材料

def do_catch():
    time.sleep(2)
 
    move_and_click_func(skill4)
    pyautogui.moveTo(center_location[0], center_location[1], duration=0.1)
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(0.05)  # 停留一点点
    pyautogui.mouseUp()

    catch_count = 1

    while not find_and_click('./ui/catch_confirm.png', confidence=0.7):
        
        while not (locate_color_strict_match('./ui/capsule.png', confidence=0.99) or locate_color_strict_match('./ui/grey_capsule.png', confidence=0.98)): 
            while not (find_and_click("./ui/prop.png", confidence=0.9)):
                if keyboard.is_pressed('space'):
                    print("[检测到空格键，脚本终止]")
                    exit(0)  # 或者 return False, 取决于你想退出多彻底
                find_and_click("./ui/switch.png", confidence=0.9)
                time.sleep(0.2)
            pyautogui.mouseDown()
            time.sleep(0.05)  # 停留一点点
            pyautogui.mouseUp()
            time.sleep(1)

        if locate_color_strict_match('./ui/grey_capsule.png', confidence=0.99):
            find_and_click('./ui/fight.png', confidence=0.9) 
            do_fight()
            break
        else:
            if catch_count % 3 == 0:
                find_and_click('./ui/middle_capsule.png', confidence=0.99)
            else:
                find_and_click('./ui/capsule.png', confidence=0.99)
        time.sleep(5)
    
        catch_count += 1
    
def catch_if(monster, count, action):
    if find_image("./special_monster/nier.png", confidence=0.95): 
        time.sleep(1)
        monster_in_battle = r'./monster/nier/in_battle'
        monster_in_battle_file = get_all_file_paths(monster_in_battle)
        if not find_image(monster_in_battle_file,confidence=0.95,timeout=3):
            count += 299900000
            do_catch()
        else:
            if find_image('./ui/nier46/' + monster + '.png',confidence=0.99):
                do_catch()
            else:
                do_run()                            
           
    elif find_image("./special_monster/zhake.png" ,confidence= 0.95):
        time.sleep(1)
        monster_in_battle = r'./monster/zhake/in_battle' 
        monster_in_battle_file = get_all_file_paths(monster_in_battle)
        if find_image(monster_in_battle_file,confidence=0.95,timeout=3):
            do_catch()
        else:
            count += 10000000
            do_catch()

    else:
        monster_in_battle = r'./monster/' + monster + r'/in_battle'
        monster_in_battle_file = get_all_file_paths(monster_in_battle)
        if find_image(monster_in_battle_file,confidence=0.95,timeout=3):
            if action == "fight":
                do_fight()
            else:
                do_run()
        else:
            count += 99900000
            do_catch()     
    return count

def main():
    global count
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
            if find_image(monster_outside, confidence=0.9): #ex:0.9 #ma: 0.6
                if find_color_and_click(monster_color, tolerance=2):
                    mark = 1
                else:
                    mark = 0
                    find_and_click(monster_outside, confidence=0.9)
            elif find_color_and_click(monster_color, tolerance=2):
                mark = 1
            print_func(count)
            time.sleep(1)
            find_and_click("./ui/nono_x.png", confidence=0.9)
            find_and_click("./ui/self_x.png", confidence=0.9)
            find_and_click("./ui/ex_x.png", confidence=0.9)
            find_and_click("./ui/confirm.png")
        if mark == 0:
            #count = catch_if(monster, count, "run")
            count = catch_if(monster, count, "fight")
        elif mark == 1:
            do_catch()
        mark = 0
        if count % heal_round == 0:
            do_heal()
        time.sleep(1.5)
        print(">>> 一轮完成，准备下一轮...\n")
        count += 1
        print_func(count)

if __name__ == "__main__":
    count = 0
    heal_round = 10
    #monster = "jier"
    monster = "huojingshou"
    monster_outside = get_all_file_paths(r"./monster/" + monster + r"/outside")           
    monster_color = monster_dc_map[monster]

    main()