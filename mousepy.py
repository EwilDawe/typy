import win32api, win32con
import time

def moveMouse(x, y): #Jumps to x,y - no fluid motion yet
	"""
	Moves the cursor to (x, y)
	"""
	
	win32api.SetCursorPos((x, y))
	
def moveLine(x, y, speed = 1): #TO BE REFACTORED
	"""
	Moves the cursor in a straight line to (x, y) at a certain speed.
	Speed is measured in pixels per millisecond
	"""
	
	_x, _y = win32api.GetCursorPos()
	if not(x - _x):	#Make sure gradient is defined - stops ZeroDivisionError
		m = (y - _y)/(x - _x)
		c = y - (m*x)
		for a in range(_x, x + 1, speed) if _x <= x else range(_x, x - 1, -speed):
			b = int(m*a + c)
			moveMouse(a, b)
			time.sleep(0.001)
		moveMouse(x, y)
	else:
		for b in range(_y, y + 1, speed) if _y <= y else range(_y, y - 1, -speed):
			moveMouse(x, b)
			time.sleep(0.001)
		moveMouse(x, y)

def moveArc():
	"""
	Moves the cursor in an arc with a specified radius to (x, y) at a specified speed.
	Speed is measured in pixels per millisecond.
	"""
	
	_x, _y = win32api.GetCursorPos()
	

def clickLeft(x = win32api.GetCursorPos()[0], y = win32api.GetCursorPos()[1]):
	'''
	Simulates a mouse left click on pixel (x,y) if x and y are provided.
	If x and y are not passed to this function, a mouse click is simulated at the current (x,y)
	'''
	
	moveMouse(x, y)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
	
def clickRight(x = win32api.GetCursorPos()[0], y = win32api.GetCursorPos()[1]):
	"""
	Simulates a mouse right click on pixel (x,y) if x and y are provided.
	If x and y are not passed to this function, a mouse click is simulated at the current (x,y)
	"""
	
	moveMouse(x, y)
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)	
