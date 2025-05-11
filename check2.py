import pyautogui

import cv2
import numpy as np
import mss


enemy_hp1_box=(1070, 260, 1095, 290),
enemy_hp2_box=(1085, 260, 1105, 290),
enemy_level_box=(1318, 260, 1345, 280)
dialogue_box=(520, 680, 760, 790)

def check_detection_regions(
    enemy_info_box=(1070, 260, 1095, 290),
    dialogue_box=(1085, 260, 1105, 290),
    save_path='region_check.png'
):
    """
    在全屏截图中框出指定区域（敌人信息+战斗对白），并保存一张图供检查。

    参数：
        enemy_info_box (tuple): 敌人等级与血量区域
        dialogue_box (tuple): 战斗对白区域
        save_path (str): 输出图片路径
    """
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)

    img = np.array(screenshot)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    # 画框：红色表示敌人信息，绿色表示战斗文字
    x1, y1, x2, y2 = enemy_info_box
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Red

    x1, y1, x2, y2 = dialogue_box
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green

    # 保存
    cv2.imwrite(save_path, img)
    print(f"[✓] 检查图已保存至: {save_path}")

check_detection_regions()