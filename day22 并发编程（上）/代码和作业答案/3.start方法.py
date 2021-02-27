import threading

loop = 10000000
number = 0


def _add(count):
    global number
    for i in range(count):
        number += 1


def _sub(count):
    global number
    for i in range(count):
        number -= 1


t1 = threading.Thread(target=_add, args=(loop,))
t2 = threading.Thread(target=_sub, args=(loop,))
t1.start()
t2.start()

t1.join()  # t1线程执行完毕,才继续往后走
t2.join()  # t2线程执行完毕,才继续往后走

print(number)