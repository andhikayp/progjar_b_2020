import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 10001)
print(f"connecting to {server_address}")
sock.connect(server_address)
try:
    data = 'GET / HTTP/1.0'+"\r\n\r\n"
    sock.send(data.encode())
    recv_msg = ""
    while True:
        msg = sock.recv(32)
        if (msg):
            recv_msg = msg.decode()
            if recv_msg[-4:]=='\r\n\r\n':
                print("Message: " + recv_msg)
                break
finally:
    print("closing")
    sock.close()