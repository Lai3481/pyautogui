import pyperclip as pc
import random
import string
# copy():传一个参数，复制到剪切板上
# pc.copy("我爱中国！")

# paste():返回字符串类型的数据，会将剪切版的内容返回
# pc.copy("hello world!")
# re_paste = pc.paste()
# print(re_paste)

# pyperclip剪切板上拼接内容
# text = " Hello world! "
# pc.copy(text + pc.paste())
#  Hello world! 
#  Hello world!  Hello world! 
#  Hello world!  Hello world!  Hello world! 

# 和文件交互-只要涉及到中文 encoding="utf-8"
# 写入文件
# pc.copy("我爱中国！")
# with open("text.txt", "w", encoding="utf-8") as f:
#     f.write(pc.paste())

# 乱码代码
# pc.copy("我爱中国！")
# with open("text.txt", "w") as f:
#     f.write(pc.paste())

# 读取文件
# 第一个参数：要操作文件的相对路径
# 第二个参数：操作文件的模式 "w"-写入文件 "r"-读取文件
# 第三个参数：涉及到中文操作encoding="utf-8" 涉及到英文，
# 第三个参数可以不传
# with open("text.txt", "r", encoding="utf-8") as f:
#     re_read = f.read()
#     print(re_read)
#     pc.copy(re_read)


# 生成随机密码

def product_password(length):
    # string.ascii_letters: a-z (从小写到大写的排序字符串)
    # string.digits: 0-9位数
    # string.punctuation：所有符号
    set_code = string.ascii_letters + string.digits + string.punctuation
    print(set_code)
    # 列表推导式：[expresss for i in range(5) if condition]
    return "".join([random.choice(set_code) for _ in range(length)])
# ['1',"a","3","!","?"]
re_password = product_password(5)
pc.copy(re_password)
# (sf^h -7u_c r8GL; |#(u| ((Q%D  7isbT




