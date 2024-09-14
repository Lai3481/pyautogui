import pyautogui as pg
import time
# 简易版的连点器
# click()  while()

# 漏洞版：一直在一个坐标上点击，弹框就会一直静止
# while True:
#     pg.click(x=100, y=100, clicks=5, interval=0.5, 
#              duration=1, button="right")

# time.sleep(2)
# # for i in range(10):
# #     pg.click()
# #     time.sleep(1)
# #     print(f"这是第{i}次的点击!")

# # 最终版！
# def auto_click(x1,y1,nums):
#     try:
#         for i in range(nums):
#             pg.click(x=x1, y=y1)
#             time.sleep(1)
#             print(f"这是第{i}次的点击!")
#     except:
#         print("程序异常终止！")


# auto_click(None,None,5)