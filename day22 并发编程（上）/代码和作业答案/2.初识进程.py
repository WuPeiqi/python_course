import time
import requests
import multiprocessing
multiprocessing.set_start_method('fork')
# 进程创建之后，在进程中还会创建一个线程。
# t = multiprocessing.Process(target=函数名, args=(name, url))
# t.start()


url_list = [
    ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
    ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
    ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
]


def task(file_name, video_url):
    res = requests.get(video_url)
    with open(file_name, mode='wb') as f:
        f.write(res.content)
    print(time.time())


if __name__ == '__main__':
    print(time.time())
    for name, url in url_list:
        # Linux系统fork；win:spawn ; mac支持：fork和spawn（python3.8默认设置spawn）。
        t = multiprocessing.Process(target=task, args=(name, url))
        t.start()


