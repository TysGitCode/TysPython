import time
import pyautogui
import win32api
import win32con


#
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while pyautogui.pixel(520, 80)[0] == 34 or pyautogui.pixel(22, 11)[0] == 88:
   
    if pyautogui.pixel(897, 753)[0] == 30:
        click(955, 764)
