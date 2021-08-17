import win32gui
import win32api
import win32con
import win32com.client
import time
import keyboard

with open("position.txt", "r") as f:
    strx = f.readline()

position=strx.split(",")
titlename = "PrincessConnectReDive"
hwnd = win32gui.FindWindow(0, titlename)
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('%')
win32gui.BringWindowToTop(hwnd)
win32gui.SetForegroundWindow(hwnd)
L=right-left
W=bottom-top
i=1
f=0
p1x=left+int(L*(315/1280))
p1y=bottom-int(W*(120/760))
p2x=left+int(L*(480/1280))
p2y=bottom-int(W*(120/760))
p3x=left+int(L*(645/1280))
p3y=bottom-int(W*(120/760))
p4x=left+int(L*(805/1280))
p4y=bottom-int(W*(120/760))
p5x=left+int(L*(960/1280))
p5y=bottom-int(W*(120/760))
while i>0:
    if keyboard.is_pressed('f9') or f==1:
        break
    if keyboard.is_pressed('f8'):
        print("start")
        time.sleep(1)
        while i>0:
            if keyboard.is_pressed('f8'):
                print("stop")
                time.sleep(1)
                break
            if keyboard.is_pressed('f9'):
                f=1
                break
            if position[0]=="1" and i==1:
                win32api.SetCursorPos((p1x,p1y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.0001)
            elif position[1]=="1" and i==2:
                win32api.SetCursorPos((p2x,p2y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.0001)
            elif position[2]=="1" and i==3:
                win32api.SetCursorPos((p3x,p3y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.0001)
            elif position[3]=="1" and i==4:
                win32api.SetCursorPos((p4x,p4y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.0001)
            elif position[4]=="1" and i==5:
                win32api.SetCursorPos((p5x,p5y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.0001)
            i=i+1
            if(i>5):
                i=1

