"""
生成图片验证码的示例代码，需要提前安装pillow模块（Python中操作图片中一个第三方模块）
	pip3 install pillow
"""
import random
from PIL import Image, ImageDraw, ImageFont


def create_image_code(img_file_path, text=None, size=(120, 30), mode="RGB", bg_color=(255, 255, 255)):
    """ 生成一个图片验证码 """
    _letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
    _upper_cases = _letter_cases.upper()  # 大写字母
    _numbers = ''.join(map(str, range(3, 10)))  # 数字
    chars = ''.join((_letter_cases, _upper_cases, _numbers))

    width, height = size  # 宽高
    # 创建图形
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)  # 创建画笔

    def get_chars():
        """生成给定长度的字符串，返回列表格式"""
        return random.sample(chars, 4)

    def create_lines():
        """绘制干扰线"""
        line_num = random.randint(*(1, 2))  # 干扰线条数

        for i in range(line_num):
            # 起始点
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            # 结束点
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        """绘制干扰点"""
        chance = min(100, max(0, int(2)))  # 大小限制在[0, 100]

        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_code():
        """绘制验证码字符"""
        if text:
            code_string = text
        else:
            char_list = get_chars()
            code_string = ''.join(char_list)  # 每个字符前后以空格隔开

        # Win系统字体
        # font = ImageFont.truetype(r"C:\Windows\Fonts\SEGOEPR.TTF", size=24)
        # Mac系统字体
        # font = ImageFont.truetype("/System/Library/Fonts/SFNSRounded.ttf", size=24)
        # 项目字体文件
        font = ImageFont.truetype("MSYH.TTC", size=15)
        draw.text([0, 0], code_string, "red", font=font)
        return code_string

    create_lines()
    create_points()
    code = create_code()

    # 将图片写入到文件
    with open(img_file_path, mode='wb') as img_object:
        img.save(img_object)
    return code


code = create_image_code("a2.png", "武沛齐")
print(code)
