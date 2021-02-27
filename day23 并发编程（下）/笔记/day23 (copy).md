# day23 并发编程（下）

![image-20210226164423992](assets/image-20210226164423992.png)

课程目标：掌握多进程开发的相关知识点并初步认识协程。

今日概要：

- 多进程开发
- 进程之间数据共享
- 进程锁
- 进程池
- 协程













## 1. 多进程开发

```python
from multiprocessing import Process


def task(arg):
    print("执行中...")


if __name__ == '__main__':
    p = Process(target=task, args=('xxx',))
    p.start()

    print("继续执行...")
```

```python
from multiprocessing import Process


def task(arg):
    print("执行中...")


def run():
    p = Process(target=task, args=('xxx',))
    p.start()
    print("继续执行...")


if __name__ == '__main__':
    run()
```



进程的常见方法：

- `p.start()`，当前进程准备就绪，等待被CPU调度（工作单元其实是进程中的线程）。

- `p.join()`，等待当前进程的任务执行完毕后再向下继续执行。

  ```python
  import time
  from multiprocessing import Process
  
  
  def task(arg):
      time.sleep(2)
      print("执行中...")
  
  
  if __name__ == '__main__':
      p = Process(target=task, args=('xxx',))
      p.start()
      p.join()
  
      print("继续执行...")
  ```

- `p.daemon = 布尔值`，守护进程（必须放在start之前）

  - `p.daemon =True`，设置为守护进程，主进程执行完毕后，子进程也自动关闭。
  - `p.daemon =False`，设置为非守护进程，主进程等待子进程，子进程执行完毕后，主进程才结束。

  ```python
  import time
  from multiprocessing import Process
  
  
  def task(arg):
      time.sleep(2)
      print("执行中...")
  
  
  if __name__ == '__main__':
      p = Process(target=task, args=('xxx',))
      p.daemon = True
      p.start()
  
      print("继续执行...")
  
  ```

- 进程的名称的设置和获取

  ```python
  import time
  import multiprocessing
  
  
  def task(arg):
      time.sleep(2)
      print("当前进程的名称：", multiprocessing.current_process().name)
  
  
  if __name__ == '__main__':
      p = multiprocessing.Process(target=task, args=('xxx',))
      p.name = "哈哈哈哈"
      p.start()
  
      print("继续执行...")
  
  ```

- 自定义进程类，直接将线程需要做的事写到run方法中。

  ```python
  import multiprocessing
  
  
  class MyProcess(multiprocessing.Process):
      def run(self):
          print('执行此进程', self._args)
  
  
  if __name__ == '__main__':
      p = MyProcess(args=('xxx',))
      p.start()
      print("继续执行...")
  
  ```

  

## 2. 进程数据共享

进程是资源分配的最小单元，每个进程中都维护自己独立的数据，不共享。

```python
import multiprocessing


def task(data):
    for i in range(10):
        data.append(i)
    print("子进程中处理后的结果：", data)


if __name__ == '__main__':
    data_list = []
    p = multiprocessing.Process(target=task, args=(data_list,))
    p.start()
    p.join()

    print("主进程：", data_list)

```

如果想让进程间做数据共享，可以借助一些特殊的数据类型，例如：

- Value

  ```python
  from multiprocessing import Process, Value
  
  
  def f(n):
      n.value = 3.1415927
  
  
  if __name__ == '__main__':
      num = Value('d', 0.0)
  
      p = Process(target=f, args=(num,))
      p.start()
      p.join()
  
      print(num.value)
  
  ```

  ```
      'c': ctypes.c_char,  'u': ctypes.c_wchar,
      'b': ctypes.c_byte,  'B': ctypes.c_ubyte,
      'h': ctypes.c_short, 'H': ctypes.c_ushort,
      'i': ctypes.c_int,   'I': ctypes.c_uint,
      'l': ctypes.c_long,  'L': ctypes.c_ulong,
      'f': ctypes.c_float, 'd': ctypes.c_double
  ```

- Manager

  ```
  A manager object returned by Manager() controls a server process which holds Python objects and allows other processes to manipulate them using proxies.
  
  A manager returned by Manager() will support types list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array. For example,
  ```

  ```python
  import multiprocessing
  
  
  def task(data):
      for i in range(10):
          data.append(i)
      print("子进程中处理后的结果：", data)
  
  
  if __name__ == '__main__':
      manager = multiprocessing.Manager()
      data_list = manager.list()
  
      p = multiprocessing.Process(target=task, args=(data_list,))
      p.start()
      p.join()
  
      print("主进程：", data_list)
  
  ```

- multiprocessing.Queue

  ```python
  import multiprocessing
  
  
  def task(q):
      for i in range(10):
          q.put(i)
  
  
  if __name__ == '__main__':
      queue = multiprocessing.Queue()
      p = multiprocessing.Process(target=task, args=(queue,))
      p.start()
      p.join()
  
      print("主进程")
      print(queue.get())
      print(queue.get())
      print(queue.get())
      print(queue.get())
      print(queue.get())
  ```

- multiprocessing.Pipe

  ```python
  import time
  import multiprocessing
  
  
  def task(conn):
      time.sleep(1)
      conn.send([111, 22, 33, 44])
      data = conn.recv() # 阻塞
      print("子进程接收:", data)
      time.sleep(2)
  
  
  if __name__ == '__main__':
      parent_conn, child_conn = multiprocessing.Pipe()
  
      p = multiprocessing.Process(target=task, args=(child_conn,))
      p.start()
  
      info = parent_conn.recv() # 阻塞
      print("主进程接收：", info)
      parent_conn.send(666)
  ```

  

上述都是Python内部提供的进程之间数据共享的机制，作为了解即刻。一般在项目开发中很少使用，后期项目中一般会借助第三方的来做资源的共享，例如：MySQL、redis等。

![image-20210220051730124](assets/image-20210220051730124.png)

## 3. 进程锁

如果多个进程抢占式去做某些操作时候，为了防止操作出问题，可以通过进程锁来避免。

```python
import time
import multiprocessing


def task():
    # 假设文件中保存的内容就是一个值：10
    with open('f1.txt', mode='r', encoding='utf-8') as f:
        current_num = int(f.read())

    print("排队抢票了")
    time.sleep(1)

    current_num -= 1
    with open('f1.txt', mode='w', encoding='utf-8') as f:
        f.write(str(current_num))


if __name__ == '__main__':
    for i in range(20):
        p = multiprocessing.Process(target=task)
        p.start()
```



很显然，多进程在操作时就会出问题，此时就需要锁来介入：

```python
import time
import multiprocessing


def task(lock):
    print("开始")
    lock.acquire()
    # 假设文件中保存的内容就是一个值：10
    with open('f1.txt', mode='r', encoding='utf-8') as f:
        current_num = int(f.read())

    print("排队抢票了")
    time.sleep(1)
    current_num -= 1

    with open('f1.txt', mode='w', encoding='utf-8') as f:
        f.write(str(current_num))
    lock.release()


if __name__ == '__main__':
    lock = multiprocessing.RLock()
    for i in range(10):
        p = multiprocessing.Process(target=task, args=(lock,))
        p.start()

    time.sleep(10) # windows系统是spawn模式创建的进程，需要特殊处理。（window系统）- 【也可以通过join等待】
```

```python
import time
import multiprocessing

def task(lock):
    print("开始")
    lock.acquire()
    # 假设文件中保存的内容就是一个值：10
    with open('f1.txt', mode='r', encoding='utf-8') as f:
        current_num = int(f.read())

    print("排队抢票了")
    time.sleep(1)
    current_num -= 1

    with open('f1.txt', mode='w', encoding='utf-8') as f:
        f.write(str(current_num))
    lock.release()


if __name__ == '__main__':
    multiprocessing.set_start_method('fork') # Linux系统fork；mac支持：fork和spawn（python3.8默认设置spawn）。
    lock = multiprocessing.RLock()
    for i in range(10):
        p = multiprocessing.Process(target=task, args=(lock,))
        p.start()
```



## 4. 进程池

```python
import time
from concurrent.futures.process import ProcessPoolExecutor


def task(num):
    print("执行", num)
    time.sleep(2)


if __name__ == '__main__':

    pool = ProcessPoolExecutor(4)
    for i in range(10):
        pool.submit(task, i)

```

```python
import time
from concurrent.futures.process import ProcessPoolExecutor


def task(num):
    print("执行", num)
    time.sleep(2)


if __name__ == '__main__':

    pool = ProcessPoolExecutor(4)
    for i in range(10):
        pool.submit(task, i)
    pool.shutdown(True)

```

```python
import time
from concurrent.futures.process import ProcessPoolExecutor
import multiprocessing

def task(num):
    print("执行", num)
    time.sleep(2)
    return num


def done(res):
    print(multiprocessing.current_process())
    time.sleep(1)
    print(res.result())
    time.sleep(1)


if __name__ == '__main__':

    pool = ProcessPoolExecutor(4)
    for i in range(50):
        fur = pool.submit(task, i)
        fur.add_done_callback(done) # done的调用由主进程处理（与线程池不同）
        
    print(multiprocessing.current_process())
    pool.shutdown(True)

```



注意：如果在线程池中要使用线程锁，则需要结束Manager中的Lock和RLock。

```python
import time
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor


def task(lock):
    print("开始")
    with lock:
        # 假设文件中保存的内容就是一个值：10
        with open('f1.txt', mode='r', encoding='utf-8') as f:
            current_num = int(f.read())

        print("排队抢票了")
        time.sleep(1)
        current_num -= 1

        with open('f1.txt', mode='w', encoding='utf-8') as f:
            f.write(str(current_num))


if __name__ == '__main__':
    pool = ProcessPoolExecutor()
    # lock_object = multiprocessing.RLock() # 不能使用
    m = multiprocessing.Manager()
    lock_object = m.RLock()
    for i in range(10):
        pool.submit(task, lock_object)
```



## 5. 协程

计算机中提供了：线程、进程 用于实现并发编程（真实存在）。



协程（Coroutine），是程序员通过代码搞出来的一个东西（非真实存在）。

```
协程也可以被称为微线程，是一种用户态内的上下文切换技术。
简而言之，其实就是通过一个线程实现代码块相互切换执行。
```

例如：

```
def func1():
    print(1)
    ...
    print(2)
def func2():
    print(3)
    ...
    print(4)
func1()
func2()
```

上述代码是普通的函数定义和执行，按流程分别执行两个函数中的代码，并先后会输出：`1、2、3、4`。

但如果介入协程技术那么就可以实现函数见代码切换执行，最终输入：`1、3、2、4` 。



在Python中有多种方式可以实现协程，例如：

- greenlet

  ```python
  from greenlet import greenlet
  def func1():
      print(1)        # 第1步：输出 1
      gr2.switch()    # 第3步：切换到 func2 函数
      print(2)        # 第6步：输出 2
      gr2.switch()    # 第7步：切换到 func2 函数，从上一次执行的位置继续向后执行
  def func2():
      print(3)        # 第4步：输出 3
      gr1.switch()    # 第5步：切换到 func1 函数，从上一次执行的位置继续向后执行
      print(4)        # 第8步：输出 4
  gr1 = greenlet(func1)
  gr2 = greenlet(func2)
  gr1.switch() # 第1步：去执行 func1 函数
  ```

- yield

  ```python
  def func1():
      yield 1
      yield from func2()
      yield 2
  def func2():
      yield 3
      yield 4
      
  f1 = func1()
  for item in f1:
      print(item)
  ```

  

虽然上述两种都实现了协程，但这种编写代码的方式没啥意义。

这种来回切换执行，可能反倒让程序的执行速度更慢了（相比较于串行）。



**协程如何才能更有意义呢？**

> 不要让用户手动去切换，而是遇到IO操作时能自动切换。
>
> Python在3.4之后推出了asyncio模块 + Python3.5推出async、async语法 ，内部基于协程并且遇到IO请求自动化切换。

```python
import asyncio

async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)
    
async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)
    
tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
```



```python
"""
需要先安装：pip3 install aiohttp
"""
import aiohttp
import asyncio
async def fetch(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('_')[-1]
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)
            
async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
            'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
            'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        await asyncio.wait(tasks)
if __name__ == '__main__':
    asyncio.run(main())
```



通过上述内容发现，在处理IO请求时，协程通过一个线程就可以实现并发的操作。



**协程、线程、进程的区别？**

```python
线程，是计算机中可以被cpu调度的最小单元。
进程，是计算机资源分配的最小单元（进程为线程提供资源）。

一个进程中可以有多个线程,同一个进程中的线程可以共享此进程中的资源。

由于CPython中GIL的存在：
	- 线程，适用于IO密集型操作。
    - 进程，适用于计算密集型操作。

协程，协程也可以被称为微线程，是一种用户态内的上下文切换技术，在开发中结合遇到IO自动切换，就可以通过一个线程实现并发操作。
所以，在处理IO操作时，协程比线程更加节省开销（协程的开发难度大一些）。
```



现在很多Python中的框架都在支持协程，比如：FastAPI、Tornado、Sanic、Django 3、aiohttp等，企业开发使用的也越来越多（目前不是特别多）。



关于协程，目前同学们先了解这些概念即可，更深入的开发、应用 暂时不必过多了解，等大家学了Web框架和爬虫相关知识之后，再来学习和补充效果更佳。有兴趣想要研究的同学可以参考我写的文章和专题视频：

- 文章

  ```python
  https://pythonav.com/wiki/detail/6/91/
  https://zhuanlan.zhihu.com/p/137057192
  ```

- 视频

  ```
  https://www.bilibili.com/video/BV1NA411g7yf
  ```

  

## 总结

1. 掌握进程和进程池的操作
2. 进程之间数据共享
3. 进程锁
4. 协程、进程、线程的区别

























