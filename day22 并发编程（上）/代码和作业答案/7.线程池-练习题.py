import os
import requests
from concurrent.futures import ThreadPoolExecutor


def download(image_url):
    res = requests.get(
        url=image_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
    )
    return res


def outer(file_name):
    def save(response):
        res = response.result()
        # 写入本地
        # # 检查images目录是否存在？不存在，则创建images目录
        if not os.path.exists("images"):
            # 创建images目录
            os.makedirs("images")

        file_path = os.path.join("images", file_name)

        # # 2.将图片的内容写入到文件
        with open(file_path, mode='wb') as img_object:
            img_object.write(res.content)

    return save


# 创建线程池，最多维护10个线程。
pool = ThreadPoolExecutor(10)

with open("mv.csv", mode='r', encoding='utf-8') as file_object:
    for line in file_object:
        nid, name, url = line.split(",")
        file_name = "{}.png".format(name)
        fur = pool.submit(download, url)
        fur.add_done_callback(outer(file_name))
