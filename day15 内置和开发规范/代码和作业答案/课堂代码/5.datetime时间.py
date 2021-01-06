from datetime import datetime, timezone, timedelta

v1 = datetime.now()  # 当前本地时间
print(v1, type(v1))  # 2021-01-04 16:56:56.099010

v2 = datetime.utcnow()
print(v2)  # 2021-01-04 08:57:38.998133

tz = timezone(timedelta(hours=7))  # 当前东7区时间
v2 = datetime.now(tz)
print(v2)

val = v1.strftime("%Y-%m-%d %H:%M:%S")
print(val, type(val))  # "2021-01-04 17:14:01"
