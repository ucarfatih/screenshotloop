import win32gui
import win32ui
import win32con
import win32api
import datetime
import numpy as np
import keyboard

# shell = win32com.client.Dispatch("WScript.Shell")

# grab a handle to the main desktop window
hdesktop = win32gui.GetDesktopWindow()

# determine the size of all monitors in pixels
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN) -566
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)-168
left = 283 #win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = 100 # win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

print(width, height, left, top)

# create a device context
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)

# create a memory based device context
mem_dc = img_dc.CreateCompatibleDC()

# create a bitmap object
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(screenshot)

# fname  = "ScreenShot"
# imgOld = np.zeros((1, 1))

while 1:
    # copy the screen into our memory device context
    if keyboard.is_pressed('q'):
        mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

        signedIntsArray = screenshot.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (height, width, 4)

        screenshot.SaveBitmapFile(mem_dc, 'c:\\workspace\\ss\\' + datetime.datetime.now().strftime("%H_%M_%S__%b_%d_%Y") + '.jpg')




