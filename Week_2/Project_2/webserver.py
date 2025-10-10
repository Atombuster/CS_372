import socket
import sys
from webMIME import mime
from webfileread import read_file


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
    
   

    data = b""
    while b"\r\n\r\n" not in data:
        chunk = client_socket.recv(4096)
        data += chunk
    str = data.decode("ISO-8859-1")

    file_path_get = str.split("\r\n")[0]
    file_path = file_path_get.split(" ")[1]
    mime_type = mime(file_path)
    file = file_path.split('/')[-1]
    file_data = read_file(file).decode("utf-8")
    #print (file_data)
    #print(mime_type)
    file_len = len(file_data)

    http = '200 OK'
    if file_data == '':
        http = '404 Not Found'
        mime_type = "text/plain"
        file_len = "13"
        file_data = '404 not found'
    print(file_data)
    print(mime_type)
    print(file_len)
    response = f'HTTP/1.1 {http}\r\nContent-Type: {mime_type}\r\nContent-Length: {file_len}\r\nConnection: close\r\n\r\n{file_data}\r\nwhile True:'
    print(str)
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()


