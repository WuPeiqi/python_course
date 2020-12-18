"""
import requests

res = requests.get(
    url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
)

# 网络传输的原始二进制信息（bytes）
# res.content

file_object = open('files/log1.txt', mode='wb')
file_object.write(res.content)
file_object.close()
"""

"""
import requests

res = requests.get(
    url="https://hbimg.huabanimg.com/c7e1461e4b15735fbe625c4dc85bd19904d96daf6de9fb-tosv1r_fw1200",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
)

# 网络传输的原始二进制信息（bytes）
# res.content

file_object = open('files/美女.png', mode='wb')
file_object.write(res.content)
file_object.close()
"""