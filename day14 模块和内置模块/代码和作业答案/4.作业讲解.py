import os
from moviepy.editor import VideoFileClip


def get_mp4_hour(folder_path):
    # 1.遍历目录下的所有mp4
    total_seconds = 0
    data = os.walk(folder_path)
    for path, folder_list, file_list in data:
        for file_name in file_list:
            file_abs_path = os.path.join(path, file_name)
            ext = file_abs_path.rsplit(".", 1)[-1]
            if ext == "mp4":
                clip = VideoFileClip(file_abs_path)
                total_seconds += clip.duration

    hour = round(total_seconds / 60 / 60, 2)
    return hour


if __name__ == '__main__':
    res = get_mp4_hour("/Users/wupeiqi/Documents/视频教程/路飞Python/mp4/day03")
    print(res)
