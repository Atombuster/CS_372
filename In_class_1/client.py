import socket

s = socket.socket()

server = ('localhost', 3001 )

s.connect(server)

#data = s.recv(100)

#str = data.decode()

#print(str)


i = 0
while i <= 10:

    data = s.recv(100)

    #str = data.decode()
    if data == b'':
        break
    print(data)

    i += 1