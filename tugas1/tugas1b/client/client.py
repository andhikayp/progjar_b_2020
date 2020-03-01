import os
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10006)
print(f"connecting to {server_address}")
sock.connect(server_address)
try:
    message = input("Find file in server: ")
    print(f"finding {message}...")
    sock.send(message.encode())
    with open(message, 'wb') as f:
        print('file opened')
        while True:
            data = sock.recv(1024)
            if not data:
                print("File accessible!")
                break
            f.write(data)
    f.close()
    # if data.decode('utf-8') == "error":
    #     print("File not found in server!")
    #     f.close()
    #     os.remove(message)
    #     break
finally:
    print("closing")
    sock.close()