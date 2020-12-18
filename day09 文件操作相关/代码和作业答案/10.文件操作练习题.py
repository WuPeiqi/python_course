# 1.下载视频
"""
import requests
res = requests.get(
    url="https://f.video.weibocdn.com/000pTZJLgx07IQgaH7HW010412066BJV0E030.mp4?label=mp4_720p&template=1280x720.25.0&trans_finger=1f0da16358befad33323e3a1b7f95fc9&media_id=4583105541898354&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=2&ot=h&ps=3lckmu&uid=3ZoTIp&ab=3915-g1,966-g1,3370-g1,3601-g0,3601-g0,3601-g0,1493-g0,1192-g0,1191-g0,1258-g0&Expires=1608204895&ssig=NdYpDIEXSS&KID=unistore,video",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
)
# 视频的文件内容
with open('nba.mp4',mode='wb') as file_object:
    file_object.write(res.content)
"""

# 2.日志计数
"""
total_count = 0
ip = "223.73.89.192"
with open('files/access.log',mode='r',encoding='utf-8') as file_object:
    for line in file_object:
        if line.startswith(ip):
            total_count += 1
print(total_count)
"""
"""
total_count = 0
ip = "223.73.89.192"
with open('files/access.log', mode='r', encoding='utf-8') as file_object:
    for line in file_object:
        if not line.startswith(ip):
            continue
        total_count += 1
print(total_count)
"""

# 3.日志计数升级版
"""
user_dict = {}
with open('files/access.log',mode='r',encoding='utf-8') as file_object:
    for line in file_object:
        user_ip = line.split(" ")[0]
        if user_ip in user_dict:
            # user_dict[user_ip] = user_dict[user_ip] + 1
            user_dict[user_ip] += 1
        else:
            user_dict[user_ip] = 1
print(user_dict)
"""

# 4.筛选出股票 当前价大于 20 的所有股票数据。
"""
with open('files/stock.txt', mode='r', encoding='utf-8') as file_object:
    # 1.跳过第一行
    file_object.readline()
    # 2.接着往下读
    for line in file_object:
        text = line.split(',')[2]
        price = float(text)
        if price > 20:
            print(line.strip())
"""

# 5.根据要求修改文件的内容
"""
- 文件读到内存，再通过replace（适用于小文件，不适用大文件）
- 挨个位置读文件的内容，遇到luffycity将其替换成pythonav。（不可取）
- 同时打开两个文件，读+写。（适用于小文件，适用大文件）
"""
with open('files/ha.conf', mode='r', encoding='utf-8') as read_file_object, open('files/new.conf', mode='w',
                                                                                 encoding='utf-8') as write_file_object:
    for line in read_file_object:
        new_line = line.replace("luffycity", 'pythonav')
        write_file_object.write(new_line)

# 重命名
import shutil

shutil.move("files/new.conf", 'files/ha.conf')
