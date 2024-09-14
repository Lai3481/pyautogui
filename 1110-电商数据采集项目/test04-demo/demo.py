import pyautogui as pg
import pyperclip as pc
from cnocr import CnOcr
import json 
import time

# PC端电商信息采集-(淘宝网站-手机页面)-写入到json文件中
# 基础版
# 1. 自动化打开浏览器-对应的淘宝网站页面
# 2. 对要提取文字的模块指定截图
# 3. 对截图进行文字提取
# 4. 筛选提取的文字，<=0.3文字不可信，不要
# 5. 把score>0.3 文字写入到json文件中(数据格式要是json的数据)

# 1. 自动化打开浏览器-对应的淘宝网站页面
# locateCenterOnScreen() click() write() press() copy() hotkey() 
# screenshot() ocr()  json.dump()-会将数据转为json格式数据，并写入到json文件中

# Step1:
# locateCenterOnScreen():识别目标图片在屏幕上的中心点坐标，将其返回
# 参数：1. 目标图片保存路径 2. confidence:精度 0.7-0.8
# google_center = pg.locateCenterOnScreen("google.png", confidence=0.7)
# # print(google_center)

# # Step2:
# # 对Step1返回的目标点进行双击，目的：打开浏览器
# # click():对传的坐标值进行点击
# # 参数：
# # x,y:目标点坐标 None或者不传-会以当前位置作为目标点位置
# # click=1,duration:从当前位置移到目标点位置需要的时间
# pg.click(x=google_center.x, y=google_center.y, clicks=2, duration=1)

# # 引入一个概念：只要涉及到页面加载，我们就要留一些页面加载的时间
# time.sleep(2)
# # Step3:
# # 将淘宝的网址输入进浏览器的地址栏上
# # write():输入方法，将传给它的参数值进行输入
# # 参数:
# # meassage:要进行输入的值 
# # interval:输入单个字符的间隔时间
# pg.write("taobao.com", interval=0.5)

# # Step4:
# # 按enter键 进入淘宝首页
# pg.press("enter")
# time.sleep(2)

# Step5：
# 想往输入框输入中文
# pc.copy("手机")
# pg.hotkey("ctrl", "v")
# pg.press("enter")

# 2. 对要提取文字的模块指定截图
# screenshot:进行屏幕截图
# 参数： 1. 截图后保存路径 2. region：指定在哪个区域进行截图，不传默认截全屏
# img_phone = "phone.png"
# pg.screenshot(img_phone, region=[190, 480, 240, 432])


# 3. 对截图进行文字提取
# ocr = CnOcr()
# out = ocr.ocr(img_phone)
# print(out)  [{"text":"123", "score":0.2},{"text":"456", "score":0.7}]

# 4. 筛选提取的文字，<=0.3文字不可信，不要
# 两种写法来筛选
# 1. for循环
# list_text = []
# for i in out:
#     if i["score"]>=0.3:
#         # print(i["text"])
#         list_text.append(i["text"])
# print(list_text)

# 2. 列表表达式
# list_text2 = [i["text"] for i in out if i["score"]>=0.3]
# print(222, list_text2)

# 5. 把score>0.3 文字写入到json文件中(数据格式要是json的数据)
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(list_text2, f, ensure_ascii=False)


# PC端电商信息采集-(淘宝网站-手机页面)-写入到json文件中
# 升级版-提取十张图片的文字
# 封装两个函数：
# 第一个函数：
# regions_ocr: 1. 定义区域截图位置 2. 对截好的图片进行文字识别，并将文字写入到json文件中

# 第二个函数：
# screen_func: 1. 进行截图
# 接收参数：
# 1. regions_ocr函数传过来的（单张图片）区域截图的位置 
# 2. regions_ocr函数传过来的区域截图保存路径
# 返回值：
# True-对该区域截图成功 False-对该区域截图失败

# 区域滚动，滚动到十张图片文字信息都漏出来
# pg.scroll(-350)

def regions_ocr():
    # regions=[left, top, width, height]
    # 第一排图片的规律：left值呈等差序列，公差是单个模块的宽度+两个模块之间的宽度
    # top，width,height相同
    # 第二排图片的规律：left和第一排图片的left值相同 第二排top，width,height相同，
    # 但是top和第一排的不同
    all_regions = [
        [190, 166, 240, 432],
        [438, 166, 240, 432],
        [686, 166, 240, 432],
        [936, 166, 240, 432],
        [1186, 166, 240, 432],
        [190, 626, 240, 428],
        [438, 626, 240, 428],
        [686, 626, 240, 428],
        [936, 626, 240, 428],
        [1186, 626, 240,428]               
    ]
    # enumerate():让我们可以访问到列表对应的索引值 
    # 第一个变量接收的是当前遍历的元素对应的索引值，变量名可以随意起
    # 第二个变量接收的是当前遍历的元素值，变量名可以随意起
    ocr = CnOcr()
    # 接收10张图的识别文字
    all_text = []
    for index,item in enumerate(all_regions):
        img_path = f"img_fp{index}.png"
        if screen_func(item, img_path):
            out = ocr.ocr(img_path)
            single_text = [i["text"] for i in out if i["score"]>0.3] 
            all_text.append(single_text)
    # print(all_text) 
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(all_text, f, ensure_ascii=False)      





def screen_func(img_region, img_path):
    try:
        pg.screenshot(img_path, region=img_region)
        return True
    except:
        print(f"截图失败{img_region}")
        return False



regions_ocr()