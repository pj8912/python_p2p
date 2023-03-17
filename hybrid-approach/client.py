import socket
import threading
import sys

class ClientConnection: 

    def __init__(self, addr):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.connect((addr, 5000))
        self.previous_data = None

        self.request_peers()

        while True:
            data = self.receive_message()
            if not data:
                print("-" * 21 + " Server failed " + "-" * 21)
                break
            elif data[0:1] == b'\x11':
                print("Got peers")
                self.update_peers(data[1:])
                print("\n", data[1:], "\n")

    def request_peers(self):
        self.s.send("join".encode('utf-8'))

    def receive_message(self):
        try:
            data = self.s.recv(1024)
            return data
        except KeyboardInterrupt:
            self.send_disconnect_signal()

    def update_peers(self, peers):
        p2p.peers = str(peers, "utf-8").split(',')[:-1]

    def send_disconnect_signal(self):
        print("Disconnected from server")
        self.s.send("q".encode('utf-8'))
        sys.exit()
