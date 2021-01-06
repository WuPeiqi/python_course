import re

"""
text = "逗2B最逗3B欢乐"
data = re.findall("\dB", text)
print(data)  # ['2B', '3B']
"""

"""
text = "逗2B最逗3B欢乐"
data = re.finditer("\dB", text)
for item in data:
    content = item.group()
    print(content)
"""

# 正则：命名分组 (正则)   (?P<名称>正则)
"""
text = "dsf130429191912015219k13042919591219521Xkk"
data_list = re.findall("\d{6}(\d{4})(\d{2})(\d{2})\d{3}[\d|X]", text)
print(data_list)  # [('1919', '12', '01'), ('1959', '12', '19')]

text = "dsf130429191912015219k13042919591219521Xkk"
data_list = re.findall("\d{6}(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})\d{3}[\d|X]", text)
print(data_list)  # [('1919', '12', '01'), ('1959', '12', '19')]
"""

text = "dsf130429191912015219k13042919591219521Xkk"
data_list = re.finditer("\d{6}(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})\d{3}[\d|X]", text)
for item in data_list:
    info_dict = item.groupdict()
    print(info_dict)
