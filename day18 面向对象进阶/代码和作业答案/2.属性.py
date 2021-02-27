import requests
from requests.models import Response
# 内部下载视频，并将下载好的数据分装到Response对象中。
# res = Response(.....)
res = requests.get(
    url="https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg",
    headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
    }
)

print(type(res)) # requests.models.Response
# 去对象中获取text，其实需要读取原始文本字节并转换为字符串
with open("xx.mp4", mode='wb') as f:
    f.write(res.content)
