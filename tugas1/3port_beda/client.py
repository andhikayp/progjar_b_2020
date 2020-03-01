import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 31002)
print(f"connecting to {server_address}")
sock.connect(server_address)
try:
    message = '31002'
    print(f"sending {message}")
    sock.sendall(message.encode())
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f"{data}")
finally:
    print("closing")
    sock.close()