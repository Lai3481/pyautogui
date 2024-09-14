import pyautogui as pg

# 4个 1.可以设置button的个数（1个，多个） 
# 2.自带输入框（文本输入框，密码输入框）

# 可以设置button的个数-1个
# title:消息框的标题文本 字符串
# text: 消息框的正文文本内容 字符串
# button: 按钮上的文本 字符串 默认-"确认"

# 返回值
# button传值，不论是点击button还是点击叉号，都会将button设置的值返回
# button不传值，不论是点击button还是点击叉号，OK返回


# button传值
# re_alert = pg.alert(title="可以设置1个button",text="我是可以设置1个button",
#                     button="confirm")

# button不传值
# re_alert = pg.alert(title="可以设置1个button",text="我是可以设置1个button")
# print(re_alert)

# 可以设置button的个数-多个
# title:消息框的标题文本 字符串
# text: 消息框的正文文本内容 字符串
# buttons:list[str] 设置button文本 默认“确定” “取消”

# 返回值
# buttons传值,点击对应的button按钮，就会返回按钮上对应的文本。点击叉号，返回None
# buttons不传值,点击“确定”-button 返回OK 点击“取消”-button,点击叉号 返回Cancel

# buttons传值
# re_confirm = pg.confirm(title="可以设置多个button",text="我是可以设置多个button",
#                         buttons=["confirm","cancel"])

# buttons不传值

# re_confirm = pg.confirm(title="可以设置多个button",text="我是可以设置多个button")
# print(re_confirm)


# 自带文本输入框-消息框
# title:消息框的标题文本 字符串
# text: 消息框的正文文本内容 字符串
# default:文本输入框默认提示

# 返回值：
# 文本输入框有值，点击ok-button，才会将文本输入框的内容返回，其他按钮，叉号返回None
# 文本输入框没有值，点击ok-button，返回空字符串，其他按钮，叉号返回None
# re_prompt = pg.prompt(title="自带文本输入框", text="我是自带文本输入框", default="请您输入")
# print(re_prompt)

# 自带密码输入框-消息框
# title:消息框的标题文本 字符串
# text: 消息框的正文文本内容 字符串
# default:文本输入框默认提示
# mask:密码输入框的遮罩。默认值是*

# 返回值：
# 密码输入框有值，点击ok-button，才会将密码输入框真实的内容返回，其他按钮，叉号返回None
# 密码输入框没有值，点击ok-button，返回空字符串，其他按钮，叉号返回None

# re_password = pg.password(title="自带密码输入框",text="我是自带密码输入框", default="123",
#             )

# re_password = pg.password(title="自带密码输入框",text="我是自带密码输入框", default="123",
#            mask="!")
# print(re_password)