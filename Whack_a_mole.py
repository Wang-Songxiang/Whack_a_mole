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
print(left)
print(top)
print(right)
print(bottom)
i=1
while i>0:
    if keyboard.is_pressed('s'):
        break
    if position[0]=="1" and i==1:
        win32api.SetCursorPos((left+int(L*(315/1280)),bottom-int(W*(120/760))))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.001)
    elif position[1]=="1" and i==2:
        win32api.SetCursorPos((left+int(L*(480/1280)),bottom-int(W*(120/760))))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.001)
    elif position[2]=="1" and i==3:
        win32api.SetCursorPos((left+int(L*(645/1280)),bottom-int(W*(120/760))))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.001)
    elif position[3]=="1" and i==4:
        win32api.SetCursorPos((left+int(L*(805/1280)),bottom-int(W*(120/760))))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.001)
    elif position[4]=="1" and i==5:
        win32api.SetCursorPos((left+int(L*(960/1280)),bottom-int(W*(120/760))))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.001)
    i=i+1
    if(i>5):
        i=1

