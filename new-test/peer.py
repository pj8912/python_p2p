import sys
from client import *
from server import *
import time
import socket

class p2p:
    peers = []

def request_peers_from_bootnode(bootnode_address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((bootnode_address, 5000))

    s.send("req".encode('utf-8'))

    data = s.recv(1024)
    s.close()

    if data:
        peer_list = data.decode('utf-8').split(',')
        p2p.peers = [peer for peer in peer_list if peer]

def main():
    msg = "test message".encode('utf-8')
    bootnode_address = '127.0.0.1'  # Replace this with your bootnode's domain or IP address

    while True:
        try:
            print("-" * 21 + "connecting" + "-" * 21)
            time.sleep(2)

            # Request list of peers from the bootnode
            request_peers_from_bootnode(bootnode_address)

            for peer in p2p.peers:
                try:
                    client = ClientConnection(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass

                # become the server
                try:
                    server = ServerConnection(msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

        except KeyboardInterrupt as e:
            sys.exit(0)

if __name__ == "__main__":
    main()
