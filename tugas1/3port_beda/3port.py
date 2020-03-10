import socket
import threading
from queue import Queue

host ='localhost'
def connection(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(90000)
    try:
        server_address = (host, port)
        print(f"starting up on {server_address} ")
        sock.bind(server_address)
        sock.listen(1)
        while True:
            print("waiting for a connection")
            connection, client_address = sock.accept()
            print(f"connection from {client_address}")
            while True:
                data = connection.recv(32)
                print(f"received {data}")
                if data:
                    print("sending back data")
                    connection.sendall(data)
                else:
                    break
    except:
        connection.close()

def c_port():
    connection(que.get())

if __name__ == '__main__':
    que = Queue()
    for port in range(31000,31003):
        que.put(port)
    for x in range(1,4):
        t = threading.Thread(target=c_port, daemon=True)
        t.start()
    que.join()