from PIL import ImageDraw
import pyautogui
from pyautogui import ImageNotFoundException
from script2 import do_run, find_and_click
from script3 import do_all_heal

# 截全屏
screenshot = pyautogui.screenshot()

# 画红圈
draw = ImageDraw.Draw(screenshot)
'''
try:
    x, y = pyautogui.locateCenterOnScreen('./lisa_skill/yelvguangshu.png', confidence=0.999999)
except ImageNotFoundException:
    
    print('error')
    exit(0)
'''
#do_all_heal()
#   x, y = pyautogui.locateCenterOnScreen('./ui/switch.png',confidence=0.99)
x,y = 1113, 275
r = 10
draw.ellipse((x - r, y - r, x + r, y + r), outline="red", width=3)

find_and_click('./ui/go_out.png', confidence = 0.9)


# 保存并查看
screenshot.save("debug_location.png")
print(f"已保存位置图：debug_location.png. location: ({x}, {y})")

