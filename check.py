from PIL import ImageDraw
import pyautogui
from pyautogui import ImageNotFoundException    

from common import *

# 截全屏
screenshot = pyautogui.screenshot()

enemy_hp1_box=(1070, 260, 1095, 290)
enemy_hp2_box=(1085 + 2, 260, 1105 - 2, 290)
enemy_level_box=(1318, 260, 1345, 280)
dialogue_box=(520, 680, 760, 790)
second_monster_location = (1025, 684)

# 画红圈
draw = ImageDraw.Draw(screenshot)
monster_in_battle = r'./ui/nono_x.png' 
#monster_in_battle_file = get_all_file_paths(monster_in_battle)
try:
    #x, y = locate_color_strict_match(image_path='./monster_in_battle/jier/jier.png', confidence=0.99)
    #x, y = find_image(monster_in_battle_file, confidence=0.99)
    
    x,y = find_and_click(monster_in_battle, confidence=0.99)
except ImageNotFoundException:      
    
    print('error')
    exit(0)

#do_all_heal()

r = 15
draw.ellipse((x - r, y - r, x + r, y + r), outline="red", width=3)
pyautogui.moveTo(x, y, duration=0.1)
'''
pyautogui.mouseDown()
time.sleep(0.05)  # 停留一点点
pyautogui.mouseUp()
#find_and_click('./ui/go_out.png', confidence = 0.9)

'''
# 保存并查看
screenshot.save("debug_location.png")
print(f"已保存位置图：debug_location.png. location: ({x}, {y})")

