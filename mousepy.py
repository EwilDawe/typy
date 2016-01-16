import win32api, win32con

def moveMouse(x, y): #Jumps to x,y - no fluid motion yet
	"""
	Moves the cursor to (x, y)
	"""
	
	win32api.SetCursorPos((x, y))
	
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