# 1.简述进程和线程的区别以及应用场景。
"""
线程，是计算机中可以被cpu调度的最小单元(真正在工作）。
进程，是计算机资源分配的最小单元（进程为线程提供资源）。
一个进程中可以有多个线程,同一个进程中的线程可以共享此进程中的资源。
由于GIL锁的存在，控制一个进程中同一时刻只有一个线程可以被CPU调度。所以
    - 计算密集型，适合用多进程开发。
    - IO密集型，适合用多线程开发。
"""

# 2.什么是GIL锁
"""
GIL是Cpython解释器特有的一个全局解释器锁，控制一个进程中同一时刻只有一个线程可以被CPU调度。
同时像列表、字典等常见对象的线程数据安全，也得益于GIL。
"""

# 3.单例模式
"""
import threading

class Singleton:
    instance = None
    lock = threading.RLock()
            
    def __new__(cls, *args, **kwargs):

        if cls.instance:
            return cls.instance
        with cls.lock:
            if cls.instance:
                return cls.instance
            time.sleep(0.1)
            cls.instance = object.__new__(cls)
        return cls.instance
"""

# 4.程序从flag a执行到falg b的时间大致是多少秒？
"""
60
"""

# 5.程序从flag a执行到falg b的时间大致是多少秒？
"""
0
"""

# 6.程序从flag a执行到falg b的时间大致是多少秒？
"""
60
"""

# 7.读程序，请确认执行到最后number是否一定为0
"""
结果为0
"""

# 8.读程序，请确认执行到最后number是否一定为0
"""
结果不一定为0
"""

# 9.data.txt 文件中共有 10000 条数据，请为每 100行 数据创建一个线程，并在线程中把当前100条数据的num列相加并打印。
"""
import threading


def task(row_list):
    num_list = [int(row.split(",")[-1]) for row in row_list]
    result = sum(num_list)
    print(result)


def run():
    file_object = open('data.txt', mode='r', encoding='utf-8')
    file_object.readline()
    row_list = []
    for line in file_object:
        row_list.append(line.strip())
        if len(row_list) == 100:
            t = threading.Thread(target=task, args=(row_list,))
            t.start()
            row_list = []  # 千万不要用 row_list.clear()
    if row_list:
        t = threading.Thread(target=task, args=(row_list,))
        t.start()

    file_object.close()


if __name__ == '__main__':
    run()

"""