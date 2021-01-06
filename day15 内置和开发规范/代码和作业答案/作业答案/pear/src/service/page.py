"""
分页看新闻（每页显示10条），提示用户输入页码，根据页码显示指定页面的数据。
    - 提示用户输入页码，根据页码显示指定页面的数据。
    - 当用户输入的页码不存在时，默认显示第1页

"""
import config


def get_page_data(page_num, per_page_count):
    """ 根据页码获取要展示的数据列表
    :param page_num:页码
    :param per_page_count:每页数据条数
    :return:数据列表
    """
    start_index = (page_num - 1) * per_page_count
    end_index = page_num * per_page_count

    data_list = []
    read_row_count = 0
    with open(config.VIDEO_FILE_PATH, mode='r', encoding='utf-8') as file_object:
        for line in file_object:
            if start_index <= read_row_count < end_index:
                data_list.append(line.strip())
            if read_row_count >= end_index:
                break
            read_row_count += 1
    return data_list


def show_table(page_num, per_page_count, data_list):
    """ 在页面展示分页信息（输出）
    :param page_num:页码
    :param per_page_count:每页数据条数
    :param data_list:
    :return:
    """
    index = (page_num - 1) * per_page_count + 1
    for num, line in enumerate(data_list, index):
        row_list = line.split(',')
        print(num, row_list[1])


def execute():
    """ 分页看新闻 """
    print("分页看新闻（每页显示10条）")

    # 每页显示10条 & 总数据999条
    per_page_count, total_count = 10, 999

    # 计算页码最大值
    max_page_num, remainder = divmod(total_count, per_page_count)
    if remainder:
        max_page_num += 1

    while True:
        num = input("输入页码[范围{}~{}]（Q/q退出）：".format(1, max_page_num))
        if num.upper() == 'Q':
            break
        if not num.isdecimal():
            print("页码错误，请重新输入！")
            continue
        num = int(num)
        if num < 1 or num > max_page_num:
            num = 1
        page_string = "第{}页".format(num)
        print(page_string)

        data_list = get_page_data(num, per_page_count)
        show_table(num, per_page_count, data_list)
