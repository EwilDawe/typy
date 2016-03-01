import win32api, win32con
import time


def move(x, y, path = 'sudden'):
    """
    Moves the cursor to (x, y)
    """
    win32api.SetCursorPos((x, y))


def moveline(x, y, speed = 1):
    """
    Moves the cursor in a straight line to (x, y) at a certain speed.
    """

    _x, _y = win32api.GetCursorPos()
    if not (x - _x):
        m = (y - _y) / (x - _x)
        c = y - (m * x)
        for a in range(_x, x + 1, speed) if _x <= x else range(_x, x - 1, -speed):
            b = int(m * a + c)
            move(a, b)
            time.sleep(0.01)
        move(x, y)
    else:
        for b in range(_y, y + 1, speed) if _y <= y else range(_y, y - 1, -speed):
            move(x, b)
            time.sleep(0.01)
        move(x, y)


def drag(*args, function = move):
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    function(*args)
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click_left(x = None, y = None):
    """
    Simulates a mouse left click on pixel (x,y) if x and y are provided.
    If x and y are not passed to this function, a mouse click is simulated at the current (x,y)
    """

    if not (x) or not (y):
        cursor = win32api.GetCursorPos()
        if not (x): x = cursor[0]
        if not (y): y = cursor[1]
    move(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click_right(x = None, y = None):
    """
    Simulates a mouse right click on pixel (x,y) if x and y are provided.
    If x and y are not passed to this function, a mouse click is simulated at the current (x,y)
    """

    if not (x) or not (y):
        cursor = win32api.GetCursorPos()
        if not (x): x = cursor[0]
        if not (y): y = cursor[1]
    move(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)
