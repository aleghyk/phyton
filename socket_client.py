
import socket
s = socket.socket()
s.connect(('127.0.0.1',10101))
#s.connect(('127.0.0.1',10101))
while True:
    hello = input()
    s.send(hello.encode())



#denys.Zamiatin@gmail.com
#lib for rastr tkinter
