from common import *

#刷学习力

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
            if find_and_click(monster_outside, confidence=0.9): #ex:0.9 #ma: 0.6
                mark = 0
            elif find_color_and_click(monster_color, tolerance=0):
                mark = 1
            print_func(count)
            time.sleep(1)
            find_and_click("./ui/nono_x.png", confidence=0.9)
            find_and_click("./ui/self_x.png", confidence=0.9)
            find_and_click("./ui/ex_x.png", confidence=0.9)
            find_and_click("./ui/confirm.png")
        print(f"mark: {mark}")
        if mark == 0:     
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
    monster_dc_map = {"jier" : "#ffdd0a", "luojilasi" : "#ffdd0a", "jidongshou": "#ffde7d", "dinglute": "#c5d2e4", "yiyasi": "#ffa2ff", 
                      "chaerdun": "#26448f", "xisaliula": "#80edff", "huojingshou" : "#9a70f7"}
    monster = "xisaliula"
    heal_round = 5
    monster_outside = get_all_file_paths(r"./monster/" + monster + r"/outside")
    monster_color = monster_dc_map[monster]

    main()