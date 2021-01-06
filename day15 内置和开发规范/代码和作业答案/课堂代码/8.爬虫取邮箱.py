import re
import requests
from bs4 import BeautifulSoup

res = requests.get(
    url="https://www.douban.com/group/topic/79870081/",
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    }
)
bs_object = BeautifulSoup(res.text, "html.parser")
comment_object_list = bs_object.find_all("p", attrs={"class": "reply-content"})
for comment_object in comment_object_list:
    text = comment_object.text
    # 请继续补充代码，提取text中的邮箱地址
    email_list = re.findall("\w+@\w+\.\w+", text, re.ASCII)
    if email_list:
        print(email_list)