import time
import keyboard
import pyautogui
import win32api
import win32con

# 30, 37, 42 (955, 764) not hovering rgb values
# 7, 78, 110  (955, 764)  hovering rgb values
# import pyautogui
# pyautogui.displayMousePosition()
# x = 520 y = 80 rgb = 34,34,34


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while pyautogui.pixel(520, 80)[0, 0, 0] == 34:
   
    if pyautogui.pixel(897, 753)[0] == 30:
        click(955, 764)
