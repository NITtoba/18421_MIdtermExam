import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as bbbbb:
    bbbbb.sendto(b'from client message', ('127.0.0.1', 50007))
    