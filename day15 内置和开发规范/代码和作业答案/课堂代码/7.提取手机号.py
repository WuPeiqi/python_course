import re

text = "楼主太牛逼了，在线想要 442662578@qq.com和xxxxx@live.com谢谢楼主，手机号也可15131255789，搞起来呀"
email_list = re.findall("\w+@\w+\.\w+",text,re.ASCII)
print(email_list) # ['442662578@qq.com和xxxxx']