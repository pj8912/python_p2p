import sys
# sys.path.insert(1,'~/Desktop/python_p2p/test')
from client import *
from server import *
import time


class p2p:
    # make ourself the default peer
    peers = ['127.0.0.1']


def main():
    # if the server breks we try to make a client a new server
    #msg = convert()


    msg = "test message".encode('utf-8')
    while True:
        try:
            print("-" * 21 + "Trying to connect" + "-" * 21)
            # sleep a random time between 1 -5 seconds
            time.sleep(2)
            for peer in p2p.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass


                # become the server
                try:
                    server = Server(msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

        except KeyboardInterrupt as e:
            sys.exit(0)

if __name__ == "__main__":
    main()