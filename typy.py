import win32api, win32con
import config

def press(*keys):
	for key in keys:
		win32api.keybd_event(config.code[key], 0, 0, 0)
		release(key)

def hold(*keys):
	for key in keys:
		win32api.keybd_event(config.code[key], 0, 0, 0)
	release(*keys)

def release(*keys):
	for key in keys:
		win32api.keybd_event(config.code[key], 0, win32con.KEYEVENTF_KEYUP, 0)

