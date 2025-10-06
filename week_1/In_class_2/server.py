import socket

s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("localhost", 3001))

s.listen()
client_socket, client_addr = s.accept()
i = 0
while i <= 10:


    print(client_addr)
    client_socket.sendall(f"Some data!{i}\n".encode())
    i = i + 1
client_socket.close()