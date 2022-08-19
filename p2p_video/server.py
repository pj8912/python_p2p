import socket
import threading
import sys
import base64
import numpy as np
import cv2
import imutils
import time


class Server:

    def __init__(self):
        try:


            # define a socket
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)

            self.connections = []

            # make a list of peers
            self.peers = []

            # bind the socket
            self.s.bind(('127.0.0.1', 5000))

            # listen for connection
            self.s.listen(1)

            print("-" * 12 + "Server Running" + "-" * 21)

            self.run()
        except Exception as e:
            sys.exit()

    """
    This method deals with sending info to the clients
    This methods also closes the connection if the client has left
    :param: connection -> The connection server is connected to
    :param: a -> (ip address, port) of the system connected
    """

    def handler(self, connection, a):
        vid = cv2.VideoCapture(0)  # replace 'rocket.mp4' with 0 for webcam
        fps, st, frames_to_count, cnt = (0, 0, 20, 0)

        try:
            while True:
                # server recieves the message
                data = connection.recvfrom(65536)
                WIDTH = 400
                for connection in self.connections:
                    while(vid.isOpened()):
                        _, frame = vid.read()
                        frame = imutils.resize(frame, width=WIDTH)
                        encoded, buffer = cv2.imencode(
                            '.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
                        message = base64.b64encode(buffer)
                        self.s.sendto(message, a)
                        frame = cv2.putText(
                            frame, 'FPS: '+str(fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        cv2.imshow('TRANSMITTING VIDEO', frame)
                        key = cv2.waitKey(1) & 0xFF

                        # The peer that is connected wants to disconnect
                        if data and data.decode('utf-8')[0].lower() == 'q':
                            # disconnect the peer
                            self.disconnect(connection, a)
                            return

                        if cnt == frames_to_count:
                            try:
                                fps = round(frames_to_count/(time.time()-st))
                                st = time.time()
                                cnt = 0
                            except:
                                pass
                        cnt += 1

        except Exception as e:
            sys.exit()

    """
        This method is run when the user disconencts
    """

    def disconnect(self, connection, a):
        self.connections.remove(connection)
        self.peers.remove(a)
        connection.close()
        self.send_peers()
        print("{}, disconnected".format(a))
        print("-" * 50)

    """
        This method is use to run the server
        This method creates a different thread for each client
    """

    def run(self):
        # constantly listeen for connections
        while True:
            connection, a = self.s.accept()

            # append to the list of peers
            self.peers.append(a)
            print("Peers are: {}".format(self.peers))
            self.send_peers()
            # create a thread for a connection
            c_thread = threading.Thread(
                target=self.handler, args=(connection, a))
            c_thread.daemon = True
            c_thread.start()
            self.connections.append(connection)
            print("{}, connected".format(a))
            print("-" * 50)

    """
        send a list of peers to all the peers that are connected to the server
    """

    def send_peers(self):
        peer_list = ""
        for peer in self.peers:
            peer_list = peer_list + str(peer[0]) + ","

        for connection in self.connections:

            data = b'\x11' + bytes(peer_list, 'utf-8')
            connection.send(b'\x11' + bytes(peer_list, 'utf-8'))
