import win32api
import win32con
import time
import math


def move(x, y):
    """
    Moves the cursor to (x, y)

    :param x: target x-ordinate
    :param y: target y-ordinate
    :return: None
    """
    win32api.SetCursorPos((x, y))


def move_line(x, y, speed = 1):
    """
    Moves the cursor in a straight line to (x, y) at a certain speed

    :param x: target x-ordinate
    :param y: target y-ordinate
    :param speed: pixel traversal rate
    :return: None
    """

    _x, _y = win32api.GetCursorPos()
    if x - _x:
        m = (y - _y) / (x - _x)
        c = y - (m * x)
        for a in range(_x, x + 1, speed) if _x < x else range(_x, x - 1, -speed):
            b = int(m * a + c)
            move(a, b)
            time.sleep(0.01)
    else:
        for b in range(_y, y + 1, speed) if _y <= y else range(_y, y - 1, -speed):
            move(x, b)
            time.sleep(0.01)
    move(x, y)


def move_arc(x, y, r, speed = 1, orientation = True):
    # WARNING: This function currently contains inaccuracy likely due to the rounding of trigonometric functions
    """
    Moves the cursor in an arc of radius r to (x, y) at a certain speed

    :param x: target x-ordinate
    :param y: target y-ordinate
    :param r: radius
    :param speed: pixel traversal rate
    :param orientation: direction of arc
    :return: None
    """

    _x, _y = win32api.GetCursorPos()
    c_len = (r**2 - (((x - _x)/2)**2 + ((y - _y)/2)**2))**0.5
    t = (c_len**2/((y - _y)**2 + (x - _x)**2))**0.5
    t = t if orientation else -t
    centre = ((_x + x)/2 + t*(_x - x), (_y + y)/2 + t*(y - _y))
    if any(isinstance(ordinate, complex) for ordinate in centre):
        raise ValueError("Radius too low - minimum: {}".format(((x - _x)**2 + (y - _y)**2)**0.5/2))
    theta = math.atan2(_y - centre[1], _x - centre[0])
    end = math.atan2(y - centre[1], x - centre[0])
    while theta < end:
        move(*list(map(round, (centre[0] + r*math.cos(theta), centre[1] + r*math.sin(theta)))))
        theta += speed/100
        time.sleep(0.01)
    move(x, y)


def drag(*args, function = move):
    """
    Drags the mouse along a specified path

    :param args: list of arguments passed to function
    :param function: path to traverse
    :return: None
    """

    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    function(*args)
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click_left(x = None, y = None, hold_time = 0):
    """
    Simulates a mouse left click on pixel (x,y) if x and y are provided
    If x and y are not passed to this function, a mouse click is simulated at the current (x,y)

    :param x: target x-ordinate
    :param y: target y-ordinate
    :param hold_time: length of time to hold the mouse's left button
    :return: None
    """

    if not x or not y:
        cursor = win32api.GetCursorPos()
        if not x:
            x = cursor[0]
        if not y:
            y = cursor[1]
    move(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(hold_time)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click_right(x = None, y = None, hold_time = 0):
    """
    Simulates a mouse right click on pixel (x,y) if x and y are provided
    If x and y are not passed to this function, a mouse click is simulated at the current (x,y)

    :param x: target x-ordinate
    :param y: target y-ordinate
    :param hold_time: length of time to hold the mouse's right button
    :return: None
    """

    if not x or not y:
        cursor = win32api.GetCursorPos()
        if not x:
            x = cursor[0]
        if not y:
            y = cursor[1]
    move(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    time.sleep(hold_time)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)