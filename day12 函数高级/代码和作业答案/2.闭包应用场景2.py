"""
下载3个视频。
"""

# ############### 原来方式：串行 ###############
"""
import requests
video_list = [
    ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
    ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
    ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
]
for item in video_list:
    res = requests.get(
        url=item[1],
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
        }
    )
    with open(item[0], mode='wb') as file_object:
        file_object.write(res.content)
"""

# ############### 原来方式：并行 ###############
"""
多线程，多个人。
"""
import requests
from concurrent.futures.thread import ThreadPoolExecutor


def task(url):
    res = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
        }
    )
    return res.content


# 下载完成之后，Python的多线程内部会执行的函数。
def outer(file_name):
    def done(arg):
        # 视频内容
        content = arg.result()
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)
    return done


# 线程池10个人
POOL = ThreadPoolExecutor(10)

# 三个视频信息
video_list = [
    ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
    ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
    ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
]
for item in video_list:
    # 去线程池取一个人，让这个人执行去执行task函数（函数内部定义下载逻辑）
    future = POOL.submit(task, url=item[1])
    # 当执行完成task函数（下载完成）之后自动执行某个函数。
    future.add_done_callback( outer(item[0]) )
    print(item)
