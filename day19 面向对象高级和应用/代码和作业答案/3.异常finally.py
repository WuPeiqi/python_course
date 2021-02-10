def run(handler):
    try:
        num = handler()
        print(num)
        return "成功"
    except Exception as e:
        return "错误"
    finally:
        print("END")

    print("结束")


res = run(lambda: 123)
