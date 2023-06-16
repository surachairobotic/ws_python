import socket, time, requests, math, copy

class GRIPPER():
    def __init__(self, _ip='192.168.12.100'):
        # Gripper init
        self.ip = _ip
        self.port = 63352 #PORT used by robotiq gripper
        
    def open(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #open the socket
            s.connect((self.ip, self.port))
            s.sendall(b'SET POS 0\n')
            data = s.recv(2**10)
    def close(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #open the socket
            s.connect((self.ip, self.port))
            s.sendall(b'SET POS 81\n')
            data = s.recv(2**10)

grip = GRIPPER()
grip.open()