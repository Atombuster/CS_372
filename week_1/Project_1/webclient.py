import socket
import sys

#Find Domain and Port From Command line
if len(sys.argv) == 1:
     print('Please enter domain')
     exit()
if len(sys.argv) == 2:
    domain = sys.argv[1]
    port = 80
if len(sys.argv) == 3:
    domain = sys.argv[1]
    port = int(sys.argv[2])

#Make socket and connect to server
s = socket.socket()
server = (domain, port)
s.connect(server)
request = f"GET / HTTP/1.1\r\nHost: {domain}\r\nConnection: close\r\n\r\n"
s.sendall(request.encode('utf-8'))   



#Get a response print it out
while True:

    data = s.recv(4096)

    str = data.decode("ISO-8859-1")
    if data == b'':
        break
    
  
    print(str)
    
s.close()