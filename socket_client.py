 
>>> import socket
>>> s = socket.socket
>>> s.connect(('127.0.0.1',10101))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.connect(('127.0.0.1',10101))
TypeError: descriptor 'connect' requires a '_socket.socket' object but received a 'tuple'
>>> s = socket.socket()
>>> s.connect(('127.0.0.1',10101))
>>> s.send(b'hello')
denys.Zamiatin@gmail.com
lib for rastr tkinter