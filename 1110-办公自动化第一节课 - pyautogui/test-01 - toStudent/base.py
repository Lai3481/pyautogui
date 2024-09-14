import pyautogui as pg
import time


# 基础部分

# 1. 传参方式：位置传参，关键字传参，嵌套传参(位置传参 & 关键字传参)

# 位置传参:位置不能变
# pg.onScreen(100,200)
# pg.onScreen(200,100)

# 关键字传参：键=值，位置可以变(更灵活),键名不能错
# pg.onScreen(x=100, y=200)
# pg.onScreen(y=200,x=100)

# 嵌套传参(位置传参 & 关键字传参):关键字参数不能出现在位置参数前
# pg.onScreen(100, y=200)
# pg.onScreen(y=200,100) # 错误代码

# 2.测量屏幕分辨率(屏幕像素值的宽和高) 整数
# 同学们知道那些可以知道屏幕分辨率的方法吗？
# size()
# 返回值：元组类型 (宽,高)
# my_size = pg.size()
# print(my_size)

# 3.测量当前鼠标的坐标值
# 平面直角坐标系
# position()
# 返回值：元组类型 (x,y)
# my_position = pg.position()
# print(my_position)

# 4.测量坐标值是否在屏幕内
# onScreen()
# 参数1:三种传参方式 1.x,y  2.[x,y]  3.(x,y)
# 返回值:布尔值 True-屏幕内，(0,0)点。 False-屏幕外，边界上。
# 这三行代码干了同一件事
# pg.onScreen(100,100)
# pg.onScreen([100,100])
# pg.onScreen((100,100))

# is_screen = pg.onScreen(100,100)
# print(is_screen) # True

# is_screen2 = pg.onScreen(1920,1080)
# print(is_screen2) # False

# 5.程序暂停：全局暂停 局部暂停
# 全局暂停-属性,字母大写，放在引入第三方库代码的下面，其他普通代码上面
# PAUSE:单位秒，默认值0.1s，浮点数类型数据
# 作用:当前文件中所有的鼠标和键盘的方法执行完后都会暂停设置的描述
# pg.PAUSE = 2

# 局部暂停
# sleep():单位秒，默认值0.0s，浮点数类型数据
# time.sleep(2)
