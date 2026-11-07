import pyautogui
import time
# Open Notepad
pyautogui.press('win')
time.sleep(3)
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('enter')
pyautogui.write('Hello, World!')
time.sleep(3)
# Hot Keys
pyautogui.hotkey('ctrl', 'a')
time.sleep(3)
pyautogui.hotkey('ctrl', 'c')
time.sleep(3)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')

