import requests

res = requests.get(
    url='https://video.pearvideo.com/mp4/adshort/20210105/cont-1715046-15562045_adpkg-ad_hd.mp4'
)

# 视频总大小（字节）
file_size = int(res.headers['Content-Length'])

download_size = 0
with open('xxx.mp4', mode='wb') as file_object:
    # 分块读取下载的视频文件（最多一次读128字节），并逐一写入到文件中。 len(chunk)表示实际读取到每块的视频文件大小。
    for chunk in res.iter_content(128):
        download_size += len(chunk)
        file_object.write(chunk)
        file_object.flush()

        message = "视频总大小为：{}字节，已下载{}字节。".format(file_size, download_size)
        print(message)

    file_object.close()

res.close()