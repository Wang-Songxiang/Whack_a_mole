import win32gui
import win32api
import win32con
import xlrd
import time

def str2sec(t):
    m, s = t.strip("#").split(":")
    return int(m)*60 + int(s) 

titlename = "PrincessConnectReDive"
hwnd = win32gui.FindWindow(0, titlename)
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
win32gui.SetForegroundWindow(hwnd)
print(left)
print(top)
print(right)
print(bottom)

# worksheet = xlrd.open_workbook('shijianzhou.xls')
# sheet_name= worksheet.sheet_names()
# sheet = worksheet.sheet_by_name('Sheet1')
# times = sheet.col_values(0) 
# position = sheet.col_values(1)
# x=len(times)
# print(x)
# for i in range(x):
#     times[i]=str2sec(str(times[i]))

# print(times)
# print(position)
# time.sleep(90-times[0])
i=1
while i>0:
    if(i==1):
        win32api.SetCursorPos((left+280,bottom-120))
    elif(i==2):
        win32api.SetCursorPos((left+440,bottom-120))
    elif(i==3):
        win32api.SetCursorPos((left+610,bottom-120))
    elif(i==4):
        win32api.SetCursorPos((left+760,bottom-120))
    elif(i==5):
        win32api.SetCursorPos((left+920,bottom-120))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    i=i+1
    if(i>5):
        i=1
    time.sleep(3)
    # if(i<x-1):
    #     time.sleep(times[i]-times[i+1])


# win32api.SetCursorPos([30,150])
# #执行左单键击，若需要双击则延时几毫秒再点击一次即可
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# #右键单击
# win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


#win32教程https://blog.csdn.net/qq_33371343/article/details/78916751
#Python IO编程：读取excel数据及读取示例https://blog.csdn.net/weixin_44322399/article/details/104418522