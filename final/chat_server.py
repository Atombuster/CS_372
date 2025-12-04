# Example usage:
#
# python chat_server.py 3490

import sys
import socket
import select
import json

def run_server(port):
    nicknames = {}
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
                #print(f"({sock_client_socket},{sock_client_addr}): connected")
            else:
                data = sock.recv(4096)
                client_data = json.loads(data.decode('utf-8'))
                
                if data == b"":
                    print(f"{sock.getpeername()}: disconnected")
                    read_fds.remove(sock)
                    output_data = json.dumps({"type": "leave", "nick": client_data["nick"]})
                    output = output_data.encode('utf-8')
                    client.sendall(output)

                    
                else:
                    
                    print(client_data)
                    output = ''
                    for client in read_fds:
                        if client != s and client != sock:
                            
                            if client_data['type'] == "hello":
                                nicknames[sock] = client_data["nick"]
                                output_data = json.dumps({"type": "join", "nick": client_data["nick"]})
                                output = output_data.encode('utf-8')
                            elif client_data['type'] == "chat":
                                nick = nicknames.get(sock, "unknown")
                                output_data = json.dumps({"type": "chat", "nick": nick, "message": client_data["message"]})
                                output = output_data.encode('utf-8')
                            client.sendall(output)



    print()



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
