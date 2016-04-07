from os import path
import time
import win32api
import win32con
import pickle

with open(path.join(path.abspath(path.dirname(__file__)), 'data', 'codes.dat'), 'rb') as file:
    codes = pickle.load(file)


def press(*keys):
    """
    Simulates a key-press for all the keys passed to the function

    :param keys: list of keys to be pressed
    :return: None
    """

    for key in keys:
        win32api.keybd_event(codes[key], 0, 0, 0)
        release(key)


def hold(*keys, hold_time = 0, hold_while = None):
    """
    Simulates the holding of all the keys passed to the function
    These keys are held down for a default period of 0 seconds before release

    :param keys: list of keys to be held
    :param hold_time: length of time to hold keys
    :param hold_while: hold keys while hold_while returns True
    :return: None
    """

    for key in keys:
        win32api.keybd_event(codes[key], 0, 0, 0)
    if callable(hold_while):
        while hold_while():
            pass
    else:
        time.sleep(hold_time)
    release(*keys)


def release(*keys):
    """
    Simulates the release of all the keys passed to this function

    :param keys: list of keys to be released
    :return: None
    """

    for key in keys:
        win32api.keybd_event(codes[key], 0, win32con.KEYEVENTF_KEYUP, 0)


def write(s = ''):
    """
    Automates the process of typing by converting a string into a set of press() and hold() calls

    :param s: string to be written
    :return: None
    """

    for char in s:
        if char.isupper():  # Handles uppercase
            hold('shift', char.lower())
        elif char == " ":  # Handles spaces
            press('spacebar')
        elif char == "\n":  # Handles newline
            press('enter')
        elif char in (')', '!', '@', '#', '$', '%', '^', '&', '*', '('):  # Handles shift & number
            hold('shift', str((')', '!', '@', '#', '$', '%', '^', '&', '*', '(').index(char)))
        elif char in ('{', '}', '<', '>', '?', ':', '"', '_', '+', '~'):
            hold('shift', ('[', ']', ',', '.', '/', ';', "'", '-', '=', '`')[('{', '}', '<', '>', '?', ':', '"', '_',
                                                                              '+', '~').index(char)])
        else:
            press(char)
