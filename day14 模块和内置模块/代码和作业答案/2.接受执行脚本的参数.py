import sys

print(sys.argv)


# [
#       '/Users/wupeiqi/PycharmProjects/luffyCourse/day14/2.接受执行脚本的参数.py'
# ]

# [
#     "2.接受执行脚本的参数.py"
# ]

# ['2.接受执行脚本的参数.py', '127', '999', '666', 'wupeiqi']

# 例如，请实现下载图片的一个工具。

def download_image(url):
    print("下载图片", url)


def run():
    # 接受用户传入的参数
    url_list = sys.argv[1:]
    for url in url_list:
        download_image(url)


if __name__ == '__main__':
    run()
