from script1 import *

#useless

def main():
    count = 1

    monster = get_png_file_paths('./ex')

    while True:

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底
        while not find_and_click("./ui/crystal.png"):
            a = 1
        print(">>> 开始寻找怪物...")
        while not find_image("./ui/battle_confirm.png", timeout=1):
            find_and_click(monster, confidence=0.8)
            find_and_click("./ui/confirm.png")
        
        time.sleep(1)

        if find_image("./special_monster/nier.png"):
            do_run()
        else:
            do_fight()
        if count % 20 == 0:
            do_heal()
        
        print(">>> 一轮完成，准备下一轮...\n")

        count += 1

if __name__ == "__main__":
    main()