import requests

while True:
    url = input("请输入要下载网页地址：")

    try:
        res = requests.get(url=url)
    except Exception as e:
        print("请求失败，原因：{}".format(str(e)))
        continue

    with open('content.txt', mode='wb') as f:
        f.write(res.content)