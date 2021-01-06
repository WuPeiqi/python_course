import json
import requests

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=5&page_start=20"

res = requests.get(
    url=url,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
)

# json格式
print(res.text)

# json格式转换为python数据类型
data_dict = json.loads(res.text)
print(data_dict)
for item in data_dict['subjects']:
    print(item)
