import requests


def download(title, url):
    """ 下载并保存视频 """
    res = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
        }
    )

    with open('{}.mp4'.format(title), mode='wb') as f:
        f.write(res.content)


# 读取文件
with open('db.csv', mode='r', encoding='utf-8') as file_object:
    for line in file_object:
        line = line.strip()
        row_list = line.split(',')
        # download(row_list[0], row_list[1])
        download(*row_list)
