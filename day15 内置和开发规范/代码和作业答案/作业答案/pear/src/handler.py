from src.service import download, search, page


def run():
    func_dict = {
        '1': {'title': "分页看新闻", 'func': page.execute},
        '2': {'title': "搜索专区", 'func': search.execute},
        '3': {'title': "下载专区", 'func': download.execute},
    }

    tips = ";".join(["{}.{}".format(k, v['title']) for k, v in func_dict.items()])

    while True:
        print(tips)
        choice = input("请输入序号(Q/q退出)：")
        if choice.upper() == 'Q':
            break
        data_dict = func_dict.get(choice)
        if not data_dict:
            print("序号不存在，请重新输入！")
            continue

        data_dict['func']()
