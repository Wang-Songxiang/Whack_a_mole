#include<stdio.h>
#include<windows.h>
#include<string.h> 
#include<unistd.h>
#include<conio.h>

int main(){
    HWND hwnd;
    RECT rect;  
    int i=1;
    int f=0;
    int tmp,tmpf;
    FILE *fp;
    char txt[12];
    fp=fopen("position.txt","r");
    if(!fp){
        printf("can't open file\n");
    }
    while (!feof(fp))
    {
        fgets(txt,12,fp);
        // printf("%s\n", txt);
    }
    fclose(fp);
    hwnd=FindWindow(NULL,"PrincessConnectReDive");
    GetWindowRect(hwnd,&rect);
    int W=rect.right-rect.left,H=rect.bottom-rect.top;
    int py=rect.bottom-H*120/760;
    int p1x=rect.left+W*315/1280;
    int p2x=rect.left+W*480/1280;
    int p3x=rect.left+W*645/1280;
    int p4x=rect.left+W*805/1280;
    int p5x=rect.left+W*960/1280;
    int key=0;
    BringWindowToTop(hwnd);
    SetForegroundWindow(hwnd);
    // printf("%d %d\n",W,H);
    // printf("%d %d\n",p1x,py);
    // printf("%d %d\n",p2x,py);
    // printf("%d %d\n",p3x,py);
    // printf("%d %d\n",p4x,py);
    // printf("%d %d\n",p5x,py);
    // printf("读取配置完毕，摁f8启动或关闭连点(有一秒cd，启动有一秒延迟)，退出摁f9\n");
    printf("compelete reading file.\npress F8 to open or close the function.(1s delay)\npress f9 to finish.");
    while(i>0){
        sleep(0.00001);
        tmp=GetKeyState(VK_F8);
        tmpf=GetKeyState(VK_F9);
        if(tmpf<0||f==1){
            break;
        }
        if(tmp<0){
            sleep(1);
            while(i>0){
                tmp=GetKeyState(VK_F8);
                if(tmp<0){
                    sleep(1);
                    break;
                }
                tmpf=GetKeyState(VK_F9);
                if(tmpf<0){
                    f=1;
                    break;
                }
                if(i==1&&txt[0]=='1'){
                    SetCursorPos(p1x,py);
                    mouse_event(MOUSEEVENTF_LEFTUP | MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
                    sleep(0.0001);
                }
                else if(i==2&&txt[2]=='1'){
                    SetCursorPos(p2x,py);
                    mouse_event(MOUSEEVENTF_LEFTUP | MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
                    sleep(0.0001);
                }
                else if(i==3&&txt[4]=='1'){
                    SetCursorPos(p3x,py);
                    mouse_event(MOUSEEVENTF_LEFTUP | MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
                    sleep(0.0001);
                }
                else if(i==4&&txt[6]=='1'){
                    SetCursorPos(p4x,py);
                    mouse_event(MOUSEEVENTF_LEFTUP | MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
                    sleep(0.0001);
                }
                else if(i==5&&txt[8]=='1'){
                    SetCursorPos(p5x,py);
                    mouse_event(MOUSEEVENTF_LEFTUP | MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
                    sleep(0.0001);
                }
                i++;
                if(i>5){
                    i=1;
                }
            }
        }
    }
    return 0;
}