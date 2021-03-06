import json
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)
try:
    message = input("Get file in server: ")
    print(f"finding {message}...")
    data = json.dumps(dict(aksi="get", file=message))+"\r\n"
    sock.send(data.encode())
    data = sock.recv(60000).decode()
    print(data)
    if data!="null":
        with open(message, 'wb') as f:
            print('file opened')
            while True:
                data = sock.recv(1024)
                if not data:
                    print("File accessible!")
                    break
                f.write(data)
        f.close()
    else:
        print("File not found in server!")
finally:
    print("closing")
    sock.close()