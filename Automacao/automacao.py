import pyautogui
import time

pyautogui.press('win')
time.sleep(2)
pyautogui.write('')
time.sleep(2)
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(643 , 405,duration=1)
time.sleep(4)
pyautogui.click(643 , 405)
time.sleep(3)
pyautogui.write('github')
pyautogui.press('enter')
pyautogui.moveTo(x = 224 ,y = 524, duration=1)
pyautogui.click(x = 224, y = 524)