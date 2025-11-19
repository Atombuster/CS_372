# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select

def run_server(port):
    
    read_fds = set()
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('',port))
    s.listen()
    read_fds.add(s)
    while True:
        socketreadready, _, _ = select.select(read_fds,{},{})
        for sock in socketreadready:
            if sock == s:
                sock_client_socket, sock_client_addr = sock.accept()
                read_fds.add(sock_client_socket)
                print(f"({sock_client_socket},{sock_client_addr}): connected")
            else:
                data = sock.recv(4096)
                if data == b"":
                    print(f"{sock.getpeername()}: disconnected")
                    read_fds.remove(sock)
                else:
                    print(f"{sock.getpeername()}{len(data)} bytes: b'{data.decode('utf-8')}'")


    print()


#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
