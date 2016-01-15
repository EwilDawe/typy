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
		
def type(s = ''):
	for char in s:
		if char.isupper():		#Handles uppercase
			hold('shift', char.lower())
		elif char == " ":		#Handles spaces
			press('spacebar')
		elif char == "\n":		#Handles newline
			press('enter')
		elif char in (')','!','@','#','$','%','^','&','*','('): 	#Handles shift & number
			hold('shift', str((')','!','@','#','$','%','^','&','*','(').index(char)))
		elif char in ('{', '}', '<', '>', '?', ':', '"', '_', '=', '~'):
			hold('shift', ('[', ']', ',', '.', '/', ';', "'", '-', '+', '`')[('{', '}', '<', '>', '?', ':', '"', '_', '=', '~').index(char)])
		else:
			press(char)
		