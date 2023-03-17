import socket
import threading

class BootNode:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.peers = []

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        print("Bootnode listening on {}:{}".format(self.host, self.port))
        self.run()

    def run(self):
        while True:
            connection, addr = self.server_socket.accept()
            print("Connection from:", addr)

            client_thread = threading.Thread(target=self.handle_client, args=(connection, addr))
            client_thread.start()

    def handle_client(self, connection, addr):
        try:
            while True:
                data = connection.recv(1024).decode('utf-8')
                if data == 'join':
                    self.peers.append(addr)
                    connection.send(b'\x11' + ','.join(['{}:{}'.format(*peer) for peer in self.peers]).encode('utf-8') + b',')
                    print("Current peers:", self.peers)
                    break
        finally:
            connection.close()

if __name__ == "__main__":
    bootnode = BootNode()