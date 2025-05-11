from common import *

#普通刷怪        

def main():
    count = 1 

    heal_round = 10

    skill = "./skills/shanguangpipi/120.png"

    monster = get_all_file_paths('./learning_ability/hp/')

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
            #do_catch()
            do_run()
        elif find_image("./special_monster/zhake.png" ,confidence= 0.95):
            time.sleep(2)
            do_catch()
            #do_run()
        elif check_variant(detect_game_text_with_enhancement(save_debug=False)['dialogue']):
            time.sleep(2)
            do_catch()
            #do_run()
        else:
            #do_catch()
            do_fight(skill)
        if count % heal_round == 0:
            do_heal()
        if count == 1000:
            break
        print(">>> 一轮完成，准备下一轮...\n")
        count += 1
        

if __name__ == "__main__":
    main()