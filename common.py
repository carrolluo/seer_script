import pyautogui
import time
from pyautogui import ImageNotFoundException
import keyboard  # 引入库
from pathlib import Path
import pytesseract
import cv2
import numpy as np
import mss
from PIL import Image
import pytesseract
import datetime

skill_1 = (980, 704)  
skill_2 = (1097, 704)
skill_3 = (980, 760)
skill_4 = (1097, 760)

perfect_monster_map = {'火晶兽': {16:68, 17:50}, '尼尔': {16:46}, '加格': {17:52, 18:54}, '查斯': {20:64, 21:66}, '扎克': {16:50},
                       '乌凯': {10:34, 11:36}}


def find_and_click(images, confidence=0.6, timeout=0.5):
    """
    支持传入多张图像，循环查找并点击，直到找到或超时
    """
    if isinstance(images, str):
        images = [images]  # 如果只传了一个文件名，也转为列表

    start = time.time()
    while time.time() - start < timeout:

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底

        for image in images:
            try:
                location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
            except ImageNotFoundException:
                location = None
            print(location)
            
            if location:
                x, y = location
                pyautogui.moveTo(x, y, duration=0.2)
                pyautogui.mouseDown()
                time.sleep(0.05)  # 停留一点点
                pyautogui.mouseUp()
                print(f"[点击] {image}")
                return True
        

    print(f"[未找到任何图像] {images}")
    return False


def find_image(images, confidence=0.8, timeout=0.5, region=None):
    """
    在屏幕上查找指定图像，支持多图像、多区域查找。
    若设置了 region，将保存该区域的截图方便检查。
    """
    if isinstance(images, str):
        images = [images]

    '''
    # 如果设置了 region，则保存截图
    if region is not None:
        x, y, w, h = region
        screenshot = pyautogui.screenshot(region=region)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"region_capture_{timestamp}.png"
        screenshot.save(filename)
        print(f"[区域截图已保存] {filename} ← {region}")
    '''    
    
    start = time.time()
    while time.time() - start < timeout:

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)

        for image in images:
            try:
                location = pyautogui.locateCenterOnScreen(image, confidence=confidence, region=region)
                if location:
                    print(f"[识别成功] {image} → {location}")
                    return location
            except pyautogui.ImageNotFoundException:
                continue

    print(f"[识别失败] 无匹配图像: {images}")
    return False

def confirm_func():
    while find_and_click("./ui/confirm.png", timeout=0.01) or find_and_click("./ui/confirm2.png", timeout=0.01) or find_and_click("./ui/confirm3.png", timeout=0.01) or find_and_click("./ui/confirm4.png", timeout=0.01): 
        time.sleep(0.03)

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底  

def do_fight(skill):
    print(">>> 进入战斗中...")

    # 点击胜利按钮
    while not find_image("./ui/confirm.png"):

        if keyboard.is_pressed('space'):
            print("[检测到空格键，脚本终止]")
            exit(0)  # 或者 return False, 取决于你想退出多彻底
        find_and_click(skill, confidence=0.9)
        pyautogui.mouseDown()
        time.sleep(0.05)  # 停留一点点
        pyautogui.mouseUp() 
        
    confirm_func()

def do_run():
    while not find_and_click("./ui/run_confirm.png", confidence=0.95):
        if keyboard.is_pressed('space'): 
            print("[检测到空格键，脚本终止]")   
            exit(0)  # 或者 return False, 取决于你想退出多彻底
        time.sleep(0.2)
        find_and_click("./ui/run.png", confidence=0.95)
        find_and_click("./ui/switch.png", confidence=0.95)
    time.sleep(2)
    pyautogui.mouseDown()
    time.sleep(0.05)  # 停留一点点
    pyautogui.mouseUp()
    confirm_func() 

def do_heal():
    print(">>> 打开背包恢复中...")
    if find_and_click("./ui/bag.png"):
        time.sleep(0.5)
        if find_and_click("./ui/heal.png", confidence=0.8):
            time.sleep(0.5)
            if find_and_click("./ui/confirm.png"):
                time.sleep(0.5)
        find_and_click("./ui/x.png")  # 关闭背包或返回
        time.sleep(0.5)
    else:
        print(">>> 找不到背包按钮，跳过恢复")


def get_all_file_paths(folder_path):
    """
    输入：文件夹路径
    输出：该路径下所有文件（包括子文件夹）的完整路径列表
    """
    folder = Path(folder_path)
    all_files = [str(f) for f in folder.rglob('*') if f.is_file()]
    return all_files

def do_catch():
    while not find_and_click("./switch_icon/bokeer.png",confidence=0.8):
        while not((not find_and_click("./ui/switch.png", confidence=0.9)) or (not find_and_click("./ui/switch2.png", confidence=0.999))):
            x = 1
            time.sleep(0.2)
        time.sleep(0.2)
    find_and_click("./ui/go_out.png", confidence=0.9)
    time.sleep(3)
 
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
            while not (find_and_click("./ui/prop.png", confidence=0.99) or find_and_click("./ui/prop2.png", confidence=0.99)):
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

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
enemy_hp1_box=(1070, 260, 1095, 290)
enemy_hp2_box=(1085, 260, 1105, 290)
enemy_level_box=(1318, 260, 1345, 280)
dialogue_box=(520, 680, 760, 790)

def rect_to_region(x):
    return (x[0], x[1], x[2] - x[0], x[3] - x[1])

def recognize_log(roi, name="dialogue", save_debug=True):
    """
    对蓝底红字图片进行颜色分离、增强、OCR。
    """
    ocr_config = '--psm 6'
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # 红色在HSV中有两个范围（低红和高红）
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    # 提取红色掩膜
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)

    # 膨胀文字边缘，增强字形
    kernel = np.ones((2, 2), np.uint8)
    red_mask = cv2.dilate(red_mask, kernel, iterations=1)

    # 可视化保存
    if save_debug:
        cv2.imwrite(f'debug_{name}_redmask.png', red_mask)

    # OCR（使用 mask 作为单通道二值图像）
    text = pytesseract.image_to_string(red_mask, config=ocr_config, lang='chi_sim')
    print(text.strip())
    return text.strip()

def get_level(string):
    path = r'./ui/enemy_level/' + string +r'.png'
    return path

def get_hp(string):
    path = r'./ui/enemy_hp/' + string +r'.png'
    return path

def modify_order(l):
    record = -1
    for i in l:
        if int(i) % 11 == 0:
            record = i
    if record == -1:
        return l
    else:
        l.remove(record)
        l.append(record)
        return l

def perfect_check(level_roi, hp_roi1, hp_roi2, monster_name):
    levels = list(perfect_monster_map[monster_name].keys())
    levels = modify_order(levels)

    for i in levels:
        level_list = list(str(i))
        flag = True
        true_level = ''
        for j in level_list:
            if not find_image(get_level(j),confidence=0.95,region=rect_to_region(level_roi)):
                flag = False
                true_level = ''
            else:
                true_level += j
        if flag:
            perfect_hp = perfect_monster_map[monster_name][int(true_level)]
            hp1 = str(perfect_hp)[0]
            hp2 = str(perfect_hp)[1]
            if find_image(get_hp(hp1),confidence=0.8,region=rect_to_region(hp_roi1)):
                if find_image(get_hp(hp2),confidence=0.8,region=rect_to_region(hp_roi2)):
                    return True
    return False

def detect_game_text_with_enhancement(
    monster_name,
    save_debug=True
):
    """
    尝试多种增强方式对两个区域做 OCR，返回最可信文本。
    同时保存每种方法的处理图像（以供人工检查）。
    """
    save_debug=True
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    def extract_region_dialogue(region, name):
        x1, y1, x2, y2 = region
        roi = img[y1:y2, x1:x2]
        return recognize_log(roi, save_debug, name)
    
    return {
        'perfect?': perfect_check(enemy_level_box, enemy_hp1_box, enemy_hp2_box, monster_name),
        'dialogue': extract_region_dialogue(dialogue_box, 'dialogue')
    }

def detect_dialogue_text_with_enhancement(
    save_debug=True
):
    """
    尝试多种增强方式对两个区域做 OCR，返回最可信文本。
    同时保存每种方法的处理图像（以供人工检查）。
    """
    save_debug=True
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    def extract_region_dialogue(region, name):
        x1, y1, x2, y2 = region
        roi = img[y1:y2, x1:x2]
        return recognize_log(roi, save_debug, name)
    
    return {
        'dialogue': extract_region_dialogue(dialogue_box, 'dialogue')
    }

def check_variant(dialogue):
    if dialogue:
        return True
    else:
        return False