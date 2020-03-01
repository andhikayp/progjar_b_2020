import socket
import os.path

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10002)
print(f"Starting up on {server_address}")
sock.bind(server_address)
sock.listen(10)
while True:
    print("Waiting for a connection")
    connection, client_address = sock.accept()
    print(f"Connection from {client_address}")
    data = connection.recv(1024)
    if data.decode():
        print(f"Received {data.decode()}")
    try:
        if os.path.isfile(data):
            message = "File Exist! Rename the file!"
        else:
            f = open(data, 'wb')  # Open in binary
            l = connection.recv(1024)
            while (l):
                f.write(l)
                l = connection.recv(1024)
            f.close()
            message = "Success transfer file!"
        print(message)
        # connection.sendall(message.encode())
    except IOError:
        print("Failed, file empty!")
    finally:
        connection.close()