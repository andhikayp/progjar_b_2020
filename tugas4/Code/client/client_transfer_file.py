import socket
import os
from os.path import isfile, join
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)
mypath = os.path.dirname(os.path.abspath("client_transfer_file.py"))
onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
message = input("Choose file: ")
try:
    size = os.path.getsize(os.path.abspath(message))
    filename, file_extension = os.path.splitext(os.path.abspath(message))
    data = json.dumps(dict(aksi="transfer", file=message, size=size, type=file_extension))+"\r\n"

    sock.sendall(data.encode())
    f = open(message, "rb")
    l_file = f.read(1024)
    while (l_file):
        sock.send(l_file)
        l_file = f.read(1024)

    print(f"Success transfer file {message}!")
except IOError:
    print(f"Failed transfer file {message}!")
finally:
    sock.close()