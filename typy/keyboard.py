import time
import win32api
import win32con
import pickle

with open('data.dat', 'rb') as file:
    keys = pickle.load(file)


def press(*keys):
    """
    Simulates a key-press for all the keys passed to the function.
    """

    for key in keys:
        win32api.keybd_event(keys[key], 0, 0, 0)
        release(key)


def hold(*keys, hold_time = 0):
    """
    Simulates the holding of all the keys passed to the function.
    These keys are held down for a default period of 0 seconds before release.
    """

    for key in keys:
        win32api.keybd_event(keys[key], 0, 0, 0)
    time.sleep(hold_time)
    release(*keys)


def release(*keys):
    """
    Simulates the release of all the keys passed to this function.
    """

    for key in keys:
        win32api.keybd_event(keys[key], 0, win32con.KEYEVENTF_KEYUP, 0)


def write(s = ''):
    """
    Automates the process of typing by converting a string into a set of press() and hold() calls.
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
