
import sys
import socket
import time
import random
import threading
import json

from chatui import init_windows, read_command, print_message, end_windows


def usage():
    print("usage: select_client.py name host port", file=sys.stderr)



def receiving_thread(mysocket):
    while True:
        #print_message("call recv")
        data = mysocket.recv(4096)
        
        #print_message(data.decode())

        response = json.loads(data.decode('utf-8'))
        if response["type"] == "join":
            print_message(f"*** {response["nick"]} has joined the chat")
        elif response["type"] == "leave":
            print_message(f"*** {response["nick"]} has left the chat")
        elif response["type"] == "chat":
            print_message(f"{response["nick"]}: {response["message"]}")

def main(argv):
    try:
        name = argv[1]
        host = argv[2]
        port = int(argv[3])
    except:
        usage()
        return 1

    # Make the client socket and connect
    s = socket.socket()
    s.connect((host, port))



    t = threading.Thread(target=receiving_thread, args=(s,), daemon=True) 

    t.start()

    init_windows()

    hello_payload = json.dumps({"type": "hello", "nick": name})
    hello_encode = hello_payload.encode('utf-8')
    s.sendall(hello_encode)

    # Loop forever sending data at random time intervals
    while True:


        chat_message = read_command(f"{name}> ")
        if chat_message == "/q":
            sys.exit()

        chat_payload = json.dumps({"type": "chat", "message": chat_message})
        chat_encode = chat_payload.encode('utf-8')

        s.sendall(chat_encode)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
