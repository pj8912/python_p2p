import socket
import threading
import sys

class ServerConnection: 

    def __init__(self, msg, bootnode_address):
        self.msg = msg
        self.bootnode_address = bootnode_address

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.connections = []
        self.peers = []

        self.s.bind(('0.0.0.0', 0))
        self.s.listen(1)

        self.register_to_bootnode()

        print("-" * 12+ "Server Running"+ "-" *21)
        self.run()

    def register_to_bootnode(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as bootnode:
                bootnode.connect(self.bootnode_address)
                bootnode.send("join".encode('utf-8'))
        except Exception as e:
            print("Failed to register with the bootnode:", e)

    def handler(self, connection, a):
        while True:
            data = connection.recv(1024)
            for connection in self.connections:
                if data and data.decode('utf-8')[0].lower() == 'q':
                    self.disconnect(connection, a)
                    return
                elif data and data.decode('utf-8') == "req":
                    connection.send(self.msg)

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
            count = 0
            for peer in self.peers:
                print(count, peer[0], "", peer[1])
                count += 1

            c_thread = threading.Thread(target=self.handler, args=(connection, a))
            c_thread.daemon = True
            c_thread.start()
            self.connections.append(connection)
            print("{}, connected".format(a))
            print("-" * 50)
