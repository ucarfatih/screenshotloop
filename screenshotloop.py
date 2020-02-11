import win32gui
import win32ui
import win32con
import win32api
import time
import datetime
import winsound
import numpy as np
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")

# grab a handle to the main desktop window
hdesktop = win32gui.GetDesktopWindow()

# determine the size of all monitors in pixels
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN) -566
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)-168
left = 283 #win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = 100 # win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
print(width,height,left,top)
# create a device context
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)

# create a memory based device context
mem_dc = img_dc.CreateCompatibleDC()

# create a bitmap object
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(screenshot)

fname  = "ScreenShot"
imgEski= np.zeros((1,1))

while (1):
    # copy the screen into our memory device context
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

    signedIntsArray = screenshot.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)
    if (imgEski.shape!=(1,1)):
        fark=imgEski - img
        farks = np.sum(fark)
        print(farks)
    # save the bitmap to a file
        if (farks>=100):
            screenshot.SaveBitmapFile(mem_dc, 'c:\\...' + datetime.datetime.now().strftime("%H_%M_%S__%b_%d_%Y") +'.jpg')
            imgEski = img
        else: #stop the operation
            frequency = 2500  # Set Frequency .. Hertz
            duration = 400  # Set Duration To ... ms
            winsound.Beep(frequency, duration)
            break
    else :
        screenshot.SaveBitmapFile(mem_dc,'c:\\...' + datetime.datetime.now().strftime("%H_%M_%S__%b_%d_%Y") + '.jpg')
        imgEski = img

   

    time.sleep(1.5)
    shell.SendKeys("{UP}", 1.5) #Tap up on keyboard

# free our objects
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())
