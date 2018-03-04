import socket

s = socket.socket()
print('socket created')
port =1234
s.bind(('',1234)) #empty string means server can listen any computer
print('binding done to 1234')
s.listen(5)
print('listenig')
c,a = s.accept()
print('accepetd a client', a)
c.send(b'thanks for connecting')
c.close()
s.close()
