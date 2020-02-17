import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10002)
print(f"connecting to {server_address}")
sock.connect(server_address)
message = input("Send file to server: ")
try:
    f = open(message, "rb")
    sock.sendall(message.encode())
    l = f.read(1024)
    while (l):
        sock.send(l)
        l = f.read(1024)
    print(f"Success transfer file {message}!")
except IOError:
    print(f"Failed transfer file {message}!")
finally:
    sock.close()