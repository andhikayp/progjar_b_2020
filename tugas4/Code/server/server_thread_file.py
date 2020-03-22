from socket import *
import socket
import threading
import logging
import json

from file_machine import FileMachine
pm = FileMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        data=""
        while True:
            recv_file = self.connection.recv(16)
            data = data + recv_file.decode()
            if recv_file[-2:].decode() == "\r\n":
                data = json.loads(data)
                if data['aksi']=="transfer":
                    f = open(data['file'], 'wb')
                    l = self.connection.recv(1024)
                    while (l):
                        f.write(l)
                        l = self.connection.recv(1024)
                    f.close()

                hasil = pm.proses(data)
                hasil=hasil+"\r\n"
                self.connection.sendall(hasil.encode())
                break
        self.connection.close()

class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 8889))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)

def main():
    svr = Server()
    svr.start()

if __name__ == "__main__":
    main()