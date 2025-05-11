from common import *

def do_catch():
 
    find_and_click("./skills/bokeer/shouxialiuqing.png",confidence=0.9)
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(0.05)  # 停留一点点
    pyautogui.mouseUp()

    while not find_and_click("./switch_icon/lisha.png",confidence=0.8):
        while not((not find_and_click("./ui/switch.png", confidence=0.9)) or (not find_and_click("./ui/switch2.png", confidence=0.999))):
            x = 1
            time.sleep(0.2)
        time.sleep(0.2)
    find_and_click("./ui/go_out.png", confidence=0.9)
    time.sleep(3)

    while not find_and_click('./ui/catch_confirm.png', confidence=0.7):
        while not find_and_click('./ui/capsule.png', confidence=0.99): 
            while not (find_and_click("./ui/prop.png", confidence=0.9) or find_and_click("./ui/prop2.png", confidence=0.9)):
                if keyboard.is_pressed('space'):
                    print("[检测到空格键，脚本终止]")
                    exit(0)  # 或者 return False, 取决于你想退出多彻底
                time.sleep(0.2)
            pyautogui.mouseDown()
            time.sleep(0.05)  # 停留一点点
            pyautogui.mouseUp()
        pyautogui.mouseDown()
        time.sleep(0.05)  # 停留一点点
        pyautogui.mouseUp()
        time.sleep(5)

def main():
    count = 1 

    heal_round = 10

    #skill = "./skills/aiwen/70.png"
    
    monster_name = "乌凯"
    monster_name_py = "wukai"
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
            find_and_click("./ui/confirm.png")
        if find_image("./special_monster/nier.png", confidence=0.95): 
            time.sleep(2)

            monster_info = detect_game_text_with_enhancement(monster_name='尼尔',save_debug=True)
            percect = monster_info['perfect?']
            dialogue = monster_info['dialogue']

            if percect or dialogue:
                do_catch()
            else:
                do_run()

        elif find_image("./special_monster/zhake.png" ,confidence= 0.95):
            time.sleep(2)

            monster_info = detect_game_text_with_enhancement(monster_name='扎克',save_debug=True)
            percect = monster_info['perfect?']
            dialogue = monster_info['dialogue']

            if percect or dialogue:
                do_catch()
            else:
                do_run()

        else:
            monster_info = detect_game_text_with_enhancement(monster_name=monster_name,save_debug=True)
            percect = monster_info['perfect?']
            dialogue = monster_info['dialogue']

            if percect or dialogue:
            #if dialogue:
                do_catch()
            else:
                do_run()

        if count % heal_round == 0:
            do_heal()
        print(">>> 一轮完成，准备下一轮...\n")
        count += 1

if __name__ == "__main__":
    main()
    