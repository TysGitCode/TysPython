# League of Legends auto accept match script
import time
import pyautogui
import win32api
import win32con
import pyautogui as pag
pag.FAILSAFE = True


# This is the actual image recognition method
def get_position(image: str):
    try:
        position = pag.locateCenterOnScreen(image, confidence=0.8)
        if position is None:
            print(f'{image} not found on screen...')
            return None
        else:
            x = position[0]
            y = position[1]
            return x, y
    except OSError as e:
        raise Exception(e)


# While the picture is the same as the league menu screen
while __name__ == '__main__':
    time.sleep(5)
    get_position('leagueScreen.png')

    # This is the method to click the button
    def click(x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    # This says to click the button if it is the right color
    if pyautogui.pixel(897, 753)[0] == 30:
        time.sleep(9)
        # This calls the click method
        click(955, 764)
