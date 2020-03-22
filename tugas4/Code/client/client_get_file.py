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
    with open(message, 'wb') as f:
        print('file opened')
        while True:
            data = sock.recv(1024)
            if not data:
                print("File accessible!")
                break
            f.write(data)
    f.close()
finally:
    print("closing")
    sock.close()