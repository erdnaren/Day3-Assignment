
import pyautogui
import pyperclip
import time
import os
from datetime import datetime

# Step 1: Basic settings
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

print("Daily Report Bot Started")

# Step 2: Get current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Step 3: Open Google Chrome
print("Opening Google Chrome...")

pyautogui.hotkey('win', 'r')
time.sleep(2)

pyautogui.write('chrome', interval=0.1)
pyautogui.press('enter')

time.sleep(8)

# Step 4: Open weather website
print("Opening weather website...")

pyautogui.hotkey('ctrl', 'l')
pyautogui.write('https://wttr.in/Chennai?format=3',
                interval=0.05)
pyautogui.press('enter')

time.sleep(8)

# Step 5: Copy weather information
print("Fetching weather information...")

pyautogui.click(500, 300)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

time.sleep(2)

weather_data = pyperclip.paste().strip()

# Remove extra spaces and line breaks
weather_data = weather_data.replace('\n', ' ')
weather_data = weather_data.replace('\t', ' ')

if not weather_data:
    weather_data = "Weather information unavailable"

print("Fetched Data:", weather_data)

# Step 6: Open Microsoft Excel
print("Opening Microsoft Excel...")

pyautogui.hotkey('win', 'r')
time.sleep(2)

pyautogui.write('excel', interval=0.1)
pyautogui.press('enter')

time.sleep(10)

# Step 7: Enter data into Excel
print("Entering data into Excel...")

comment = "Weather update recorded automatically"

excel_data = (
    "Date and Time\tWeather Information\tComment\n"
    + current_time + "\t"
    + weather_data + "\t"
    + comment
)

pyperclip.copy(excel_data)

# Paste data starting from cell A1
pyautogui.hotkey('ctrl', 'v')

time.sleep(3)

# Step 8: Save Excel file
print("Saving Excel report...")

file_name = f"daily_report_{current_date}.xlsx"

file_path = os.path.join(os.getcwd(), file_name)

pyautogui.press('f12')
time.sleep(3)

# Enter complete file path
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(file_path, interval=0.02)
pyautogui.press('enter')

time.sleep(5)

# Step 9: Take screenshot of Excel sheet
print("Taking Excel screenshot...")

screenshot_name = f"daily_report_{current_date}.png"

screenshot_path = os.path.join(
    os.getcwd(), screenshot_name
)

pyautogui.screenshot().save(screenshot_path)

# Step 10: Display completion message
print("--------------------------------")
print("Daily Report Automation Completed")
print("Excel File:", file_path)
print("Screenshot:", screenshot_path)
print("--------------------------------")
