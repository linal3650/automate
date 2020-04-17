#! python3
# lookingBusy.py - Nudges the mouse so messaging programs don't go into idle mode

import time, pyautogui

print('NudgeBot activated, press CRTL-C to quit.')
try:
    while True:
        pyautogui.moveRel(10, 0, 0.5)
        pyautogui.moveRel(-10, 0, 0.5)
        time.sleep(10)
except KeyboardInterrupt:
    print('Nudgebot deactivated.')
