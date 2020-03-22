import json
import socket
import pandas as pd

def result_list(data):
    res = json.loads(data)
    print(pd.DataFrame.from_dict(res))
    return

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    data=""
    message = json.dumps(dict(aksi="list"))+"\r\n"
    print(f"sending list")
    sock.sendall(message.encode())
    while True:
        recv_file = sock.recv(16)
        data = data + recv_file.decode()
        if recv_file[-2:].decode() == "\r\n":
            if data=="ERRCMD\r\n":
                print("Connection Error")
            else:
                result_list(data)
            break
finally:
    print("closing")
    sock.close()