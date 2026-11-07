import pyautogui
import time
from datetime import datetime

# Step 1: Open the Chrome Browser

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

print("Opening Chrome browser")

time.sleep(3)

# Open Windows Run dialog
pyautogui.hotkey('win', 'r', interval=0.1)

time.sleep(1)

# Type Chrome
pyautogui.write('chrome')

time.sleep(1)

# Press Enter
pyautogui.press('enter')

time.sleep(3)

print("Chrome browser opened successfully")
#Step2 Enter the weather site
time.sleep(1)
pyautogui.write(' https://www.accuweather.com/en/in/chennai/206671/hourly-weather-forecast/206671/')
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)
print("Copy the weather site successfully")
pyautogui.hotkey('ctrl', 'a',interval=0.1)
time.sleep(1)
pyautogui.hotkey('ctrl', 'c',interval=0.1)
time.sleep(1)
print("Open the notepad and paste the date")
pyautogui.press('win')
time.sleep(3)
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('Enter')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v',interval=0.1)
time.sleep(1)
