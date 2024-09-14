import pyautogui as pg

# 屏幕截图
# imageFilename:指定截图保存路径 （后缀名带上）
# region:默认，截全屏。list[left,top,width,height]

# 相对路径
# 截全屏
# pg.screenshot("./all.png")

# 绝对路径
# 有问题代码
# pg.screenshot("C:\Users\edy\Desktop\all2.png")
# r"" 路径字符串
# pg.screenshot(r"C:\Users\edy\Desktop\all2.png")


# 指定区域内进行截屏
# pg.screenshot("./all3.png",region=[100,100,300,300])

# 不指定imageFilename
# re_screen = pg.screenshot()
# print(re_screen)
# re_screen.save("all4.png")


# 图片定位
# 三个定位方法找不到会抛出异常，ImageNotFoundException

# 返回最先找到的目标位置 从左至右，从上至下
# image:目标图片的保存路径
# confidence:精度 浮点数 0.999 0-1 
# 趋近于 1，匹配就越严格，找不到目标定位
# 趋近于 0，匹配就越宽松，返回错误的目标定位
# 配置 0.7-0.8

# 能去减少定位时间
# region:默认，全屏搜锁 1-3s。list[left,top,width,height]
# 可能会返回错误的定位

# 返回值：元组
# try:
#     re_position = pg.locateOnScreen("./weixin.png",confidence=0.8)
#     print(re_position) # Box(left=79, top=203, width=86, height=55)
#     # 返回目标定位的中心点
#     # 返回值：元组
#     weixin_center = pg.center(re_position)
#     print(weixin_center)
# except:
#     print("没有找到目标定位！")

# 返回所有符合目标图片的定位 自己处理下异常
# image:目标图片的保存路径
# confidence:精度 浮点数 0.999 0-1 
# 趋近于 1，匹配就越严格，找不到目标定位
# 趋近于 0，匹配就越宽松，返回错误的目标定位
# 配置 0.7-0.8

# 返回值：generator
# re_all = pg.locateAllOnScreen("./weixin.png",confidence=0.95)
# print(list(re_all))

# 返回目标图片定位的中心点
# image:目标图片的保存路径
# confidence:精度 浮点数 0.999 0-1 
# 趋近于 1，匹配就越严格，找不到目标定位
# 趋近于 0，匹配就越宽松，返回错误的目标定位
# 配置 0.7-0.8

# 返回值：元组
# re_weixin = pg.locateCenterOnScreen("./weixin.png",confidence=0.8)
# print(re_weixin)
