import os
import requests

with open('files/mv.csv', mode='r', encoding='utf-8') as file_object:
    file_object.readline()
    for line in file_object:
        user_id, username, url = line.strip().split(',')
        print(username, url)
        # 1.根据URL下载图片
        res = requests.get(
            url=url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
        )
        # 检查images目录是否存在？不存在，则创建images目录
        if not os.path.exists("images"):
            # 创建images目录
            os.makedirs("images")

        # 2.将图片的内容写入到文件
        with open("images/{}.png".format(username), mode='wb') as img_object:
            img_object.write(res.content)
