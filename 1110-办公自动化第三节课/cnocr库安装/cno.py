from cnocr import CnOcr

# 1.单行简单文字识别
# step1:截图，将想要识别的图片截图后保存在当前目录下
# step2:将刚刚截图要识别图片的路径进行保存
# img_simple = "simple.png"
# # step3：将CnOcr类实例化，返回对象，就将他赋值给一个变量
# o = CnOcr()
# # step4：调用返回对象ocr(),并且将保存图片路径的变量传给ocr(),返回识别结果[{},{}]
# out = o.ocr(img_simple)
# print(out)

# 多行简单文字识别
# img_simple2 = "simple2.png"
# ocr = CnOcr(det_model_name='naive_det')
# out = ocr.ocr(img_simple2)
# print(out)

# 竖排文字识别
# 指定模型
# img_fp = "fp.png"
# ocr = CnOcr(rec_model_name='ch_PP-OCRv3')
# out = ocr.ocr(img_fp)
# print(out)

# 竖排文字特殊场景，不指定模型识别效果会更差
# 没有指定模型
# img_fp = "fp.png"
# ocr = CnOcr()
# out = ocr.ocr(img_fp)
# print(out)

# 繁体字识别
# 指定模型
# img_code = "code.png"
# ocr = CnOcr(rec_model_name='chinese_cht_PP-OCRv3')
# out = ocr.ocr(img_code)
# print(out)

# 繁体字识别场景，不指定模型，识别效果更差
# 没有指定模型
# img_code = "code.png"
# ocr = CnOcr()
# out = ocr.ocr(img_code)
# print(out)

# 英文场景识别
# 没有指定模型
# img_en = "en.png"
# ocr = CnOcr(rec_model_name='ch_PP-OCRv3')
# out = ocr.ocr(img_en)
# print(out)

# 指定模型
# img_en = "en.png"
# ocr = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
# out = ocr.ocr(img_en)
# print(out)
