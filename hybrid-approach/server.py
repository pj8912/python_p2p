import socket
import threading
import sys
import time

class ServerConnection: 

    def __init__(self, addr, msg):
        self.msg = msg
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.connections = []
        self.peers = []
        self.s.bind((addr, 5001))
        self.s.listen(1)
        print("-" * 12 + "Server Running" + "-" * 21)
        self.run()

    def handler(self, connection, a):
        try:
            while True:
                data = connection.recv(1024)
                for connection in self.connections:
                    if data and data.decode('utf-8')[0].lower() == 'q':
                        self.disconnect(connection, a)
                        return
        except Exception as e:
            sys.exit()

    def disconnect(self, connection, a):
        self.connections.remove(connection)
        self.peers.remove(a)
        connection.close()
        print("{}, disconnected".format(a))
        print("-" * 50)

    def run(self):
        while True:
            connection, a = self.s.accept()
            self.peers.append(a)
            c_thread = threading.Thread(target=self.handler, args=(connection, a))
            c_thread.daemon = True
            c_thread.start()
            self.connections.append(connection)
            print("{}, connected".format(a))
            print("-" * 50)

    def update_bootnode(self, bootnode_addr):
        while True:
            time.sleep(60)  # Update every 60 seconds
            client = ClientConnection(bootnode_addr)
            self.peers = p2p.peers
