import sys
from client import ClientConnection
from server import ServerConnection
import time

class p2p:
    peers = ['127.0.0.1']  # Replace 'bootnode_address' with the actual bootnode address

def main():
    msg = "test message".encode('utf-8')
    bootnode_addr = p2p.peers[0]
    local_addr = '127.0.0.1'
    
    try:
        print("-" * 21 + "connecting" + "-" * 21)
        client = ClientConnection(bootnode_addr)
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass

    try:
        server = ServerConnection(local_addr, msg)
        server.update_bootnode(bootnode_addr)
    except KeyboardInterrupt:
        sys.exit()
    except:
        pass

    while True:
        try:
            time.sleep(1)  # Sleep for a second, can be adjusted as needed
        except KeyboardInterrupt:
            sys.exit()

if __name__ == "__main__":
    main()
