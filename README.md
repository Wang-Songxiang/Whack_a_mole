<h1>Whack_a_mole</h1>  

<h1>#因使用该脚本造成的一切包括但不限于封号等后果，作者不负任何责任。。。想好了再用</h1>  

这是一个帮助你在公主连接RE:dive中自动打地鼠的工具。  
使用方法，在position.txt种输入要自动连打的位置要打的地方写1，不打的地方写别的（写0就完了），不要删逗号，修改完后保存  
以管理员身份运行Whack_a_mole.exe  
摁f8开启或关闭自动连打设置的位置（每次点击间隔0.1ms）  
摁f8后延迟一秒才会启动  
f8键开关有一秒冷却时间  
摁f9键退出程序  
运行连打时不能干别的。。。  
  
更新日志  
忘了什么时候 基本功能完成  

2021/8/16 添加了开启/关闭功能的按键  
	  将开关键改为f8，退出键改为f9  
	  每次点击后的等待时间缩短为0.1ms  
2021/8/17  
	  优化了计算逻辑（然而感觉没什么区别）  
2021/8/17.1  
	感觉是python运行慢的缘故于是用c重写了个。。。  
	删除了测试时使用的数据显示，增加了操作说明（因为容易出现乱码所以用工地英语写了）  
2021/8/17.2  
	优化了一下代码看起来更简洁  
2021/8/17.3
	经dalao指点（githubID-KasuganoSora1）将linux下的sleep函数改成windows下的Sleep函数一定程度上解决了使用时游戏画面卡住的问题