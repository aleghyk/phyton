
import socket
s = socket.socket()
s.bind(('127.0.0.1',10101))
s.listen(5)
c, a = s.accept()
while True:
    data = c.recv(1024)
    print (data.decode())
    #print (c, a)
