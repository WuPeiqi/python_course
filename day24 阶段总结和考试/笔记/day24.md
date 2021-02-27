# day24 阶段总结

课程目标：对第三模块   阶段的知识点进行总结和考试，让学员更好的掌握此模块的相关知识。

课程概要：

- 知识补充
- 阶段总结（思维导图）
- 考试题



## 1. 知识点补充

我们来分析如下代码：

```python
import socket
import threading
import select


def process(request, client_address):
    print(request,client_address)
    conn = request
    while True:
        data = conn.recv(1024)
        print(data)

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('127.0.0.1',8002))
sk.listen(5)

while True:
    r, w, e = select.select([sk,],[],[],1)
    if sk in r:
        request, client_address = sk.accept()
        t = threading.Thread(target=process, args=(request, client_address))
        t.daemon = False
        t.start()

sk.close()
```

上述代码集成了：线程、网络编程、IO多路复用，实现了一个支持并发的服务端（可以同时接受多个客户端的连接）。



socketserver，是Python中的内置模块。该模块内部基于线程、进程 + socket + IO多路复用，帮我们实现了上述的功能（写的更加严谨）。

- 服务端

  ```python
  import socketserver
  import threading
  
  
  class MyRequestHandler(socketserver.BaseRequestHandler):
  
      def handle(self):
          conn = self.request
          while True:
              data = conn.recv(1024)
              if not data:
                  break
              print("收到消息:", data.decode('utf-8'), threading.current_thread())
  		conn.close()
  
  
  obj = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), MyRequestHandler)
  obj.serve_forever()
  
  ```

- 客户端

  ```python
  import socket
  
  client = socket.socket()
  client.connect(('127.0.0.1', 9000))
  
  while True:
      content = input(">>>")
      if content.upper() == 'Q':
          break
      client.sendall(content.encode('utf-8'))
  
  client.close()
  ```



在很多的框架和模块中已集成了并发相关的内容，让程序员可以只关注业务功能的开发，避免重复造轮子了（Stop Trying to Reinvent the Wheel）。



## 2. 阶段总结

思维导图



## 3. 考试题

考试题的目的是让大家对自己近期知识点学习练习 以及 自测，请大家务必【独立】完成（切勿翻看笔记 & 切勿网上搜索 ）。

- 第一步：自己独立完成（编程题目可以在pycharm中编写）

- 第二步：做完之后，翻看自己笔记去修改和更正。

- 第三步：觉自己做的没问题了，最后再去看考试题的参考答案和讲解。

  

详情见附件《第三阶段考试题.md》文件。



