
import socket

TARGET_IP = "10.151.253.11"
TARGET_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes('Andhika Yoga Perdana 05111740000101'.encode()),(TARGET_IP,TARGET_PORT))