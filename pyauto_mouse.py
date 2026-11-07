import pyautogui
import time

#mouse moviement
pyautogui.moveTo(100,100, duration=1)

#mouse  Click
pyautogui.click(100,100)

#Mouse Right Click
pyautogui.rightClick(100,100)

#Mouse Left Click
pyautogui.leftClick(100,100)

#Mouse Double Click
#pyautogui.DoubleClick(100,100)

#Mouse Drag
pyautogui.dragTo(200,200,duration=1)

#Mouse Scroll
pyautogui.scroll(-500)
#time.sleep(3)
pyautogui.scroll(500)
#time.sleep(3)

