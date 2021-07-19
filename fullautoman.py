import win32gui
import win32api
import win32con
import xlrd
import time

def str2sec(t):
    m, s = t.strip("#").split(":")
    return int(m)*60 + int(s) 

titlename = "test.png - ペイント"
hwnd = win32gui.FindWindow(0, titlename)
left, top, right, bottom = win32gui.GetWindowRect(hwnd)

print(left)
print(top)
print(right)
print(bottom)

worksheet = xlrd.open_workbook('shijianzhou.xls')
sheet_name= worksheet.sheet_names()
sheet = worksheet.sheet_by_name('Sheet1')
times = sheet.col_values(0) 
position = sheet.col_values(1)
x=len(times)
print(x)
for i in range(x):
    times[i]=str2sec(str(times[i]))

print(times)
print(position)
time.sleep(90-times[0])
for i in range(x):
    if(position[i]==1):
        win32api.SetCursorPos((left+500,top+500))
    elif(position[i]==2):
        win32api.SetCursorPos((left+550,top+510))
    elif(position[i]==3):
        win32api.SetCursorPos((left+560,top+520))
    elif(position[i]==4):
        win32api.SetCursorPos((left+570,top+530))
    elif(position[i]==5):
        win32api.SetCursorPos((left+580,top+540))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    if(i<x-1):
        time.sleep(times[i]-times[i+1])


# win32api.SetCursorPos([30,150])
# #执行左单键击，若需要双击则延时几毫秒再点击一次即可
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# #右键单击
# win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


#win32教程https://blog.csdn.net/qq_33371343/article/details/78916751
#Python IO编程：读取excel数据及读取示例https://blog.csdn.net/weixin_44322399/article/details/104418522