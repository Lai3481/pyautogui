import pyautogui as pg

# 键盘操作方法

# 输入字符
# write()
# 参数：
# message:要输入的字符
# interval:输入每个字符间隔时间
# Tips:
# 不支持输入中文(后面结合Pyperclip库输入中文)
# 只能输入字符,不能执行Shift/F1之类的按键
# 输入框光标聚焦时才能输入(可以先单击一下再输入)
# pg.write("HELLO WORLD!")
# pg.write("你好！")

# 按键方法
# press()
# 参数：
# keys: str | Iterable[str] 按键标志符
# presses:按键次数 int,默认1次
# interval:每次按键间隔时间 
# pg.press("enter", presses=3, interval=1)


# 热键(组合键)
# hotkey()
# pg.hotkey("ctrl", "a")
# pg.hotkey("ctrl", "shift", "esc")



