import socket
import sys

#Find Port From Command line
if len(sys.argv) == 1:
     port = 28333
if len(sys.argv) == 2:
    port = int(sys.argv[1])


s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("localhost", port))

s.listen()
while True:
    client_socket, client_addr = s.accept()
    
    response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!\r\nwhile True:'

    data = b""
    while b"\r\n\r\n" not in data:
        chunk = client_socket.recv(4096)
        data += chunk
    str = data.decode("ISO-8859-1")
    print(str)
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()


