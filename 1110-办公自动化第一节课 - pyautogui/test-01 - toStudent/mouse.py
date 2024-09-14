import pyautogui as pg
import time
# 鼠标操作方法

# 1.相对位置移动和绝对位置移动
# 区别：参照点不同，绝对-原点 相对-鼠标当前位置 x-左移 y-上移

# 2. 鼠标移动：

# 绝对位置移动
# moveTo():
# 参数：
# x,y:目标坐标值。None/不传，会以当前鼠标位置作为目标位置
# duration: 单位秒,默认值0s,浮点数 
# 鼠标从当前位置移动到目标位置的时间

# pg.moveTo()
# pg.moveTo(x=100, y=100, duration=2)
# pg.moveTo(x=100, y=100)

# 相对位置移动
# move()
# 参数：
# xOffset：yOffset: 偏移量
# duration: 单位秒,默认值0s,浮点数 
# 鼠标从当前位置移动到目标位置的时间

# pg.move(xOffset=200, yOffset=200, duration=2)
# pg.move(xOffset=-200, yOffset=-200, duration=2)

# 3.鼠标的拖拽
# 鼠标拖拽和鼠标移动区别：鼠标移动-滑动鼠标 鼠标拖拽-按住鼠标键位滑动鼠标

# 绝对位置拖拽

# dragTo()
# 参数：
# x,y:目标坐标值。None/不传，会以当前鼠标位置作为目标位置
# duration: 单位秒,默认值0s,浮点数 
# 鼠标从当前位置拖动到目标位置的时间
# button：占用鼠标键位，默认左键。Str,"left"左键 "right"右键 "middle"中键

# pg.dragTo(100, 100, duration=2)
# pg.dragTo(100, 100, duration=2, button="right")

# 相对位置拖拽
# drag()
# 参数：
# xOffset：yOffset: 偏移量
# duration: 单位秒,默认值0s,浮点数 
# 鼠标从当前位置拖动偏移的时间
# button：占用鼠标键位，默认左键。Str,"left"左键 "right"右键 "middle"中键

# pg.drag(xOffset=100, yOffset=100, duration=2)

# 4. 鼠标点击
# 鼠标单击
# click()
# 参数：
# x,y:目标坐标值。None/不传，会以当前鼠标位置作为目标位置
# clicks:点击次数 Int，默认1次
# duration: 单位秒,默认值0s,浮点数 
# 鼠标从当前位置移动到目标位置的时间
# interval:单位秒,默认值0s,浮点数 
# 单次操作间隔时间
# button：占用鼠标键位，默认左键。Str,"left"左键 "right"右键 "middle"中键

# pg.click(300, 300, duration=2, interval=2, clicks=2, button="right")

# 鼠标双击
# 左键双击
# pg.doubleClick()
# 右键双击
# pg.rightClick()

# 鼠标分步操作

# 占用鼠标键位
# pg.mouseDown()

# 释放鼠标键位
# pg.mouseUp()

# 5.鼠标滚动
# scroll():不同系统，不同平台表现不一样
# 5.1 传正整数向上移动 反之
# 5.2 要在需要滚动的界面聚焦(鼠标点击当前页面)
# pg.scroll()
