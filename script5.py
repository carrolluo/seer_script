from script1 import find_and_click, get_all_file_paths, confirm_func

#埃闻射击

monster = monster = get_all_file_paths('./learning_ability/hp/3')

def do_shoot():
    while not find_and_click('./ui/script5_confirm.png', confidence = 0.85):
        find_and_click('./ui/shoot.png')
        find_and_click('./ui/shoot2.png')
        while not find_and_click('./ui/claw.png', confidence = 0.85):
            a = 1
    while not find_and_click(monster, confidence= 0.9):
        a= 1

if __name__ == "__main__":
    while 1 == 1:
        do_shoot()


 