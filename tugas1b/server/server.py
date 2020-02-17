import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 10006)
print(f"starting up on {server_address}")
sock.bind(server_address)
sock.listen(1)
while True:
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")

    data = connection.recv(1024)
    print(f"received {data}")
    if data:
        try:
            f = open(data, 'rb')
            l = f.read()
            connection.sendall(l)
            f.close()
        except IOError:
            message = "error"
            print("error")
            # connection.sendall(message.encode())
        finally:
            print("closing")
    else:
        print(f"no more data from {client_address}")
        break
    connection.close()