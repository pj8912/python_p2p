import socket
import threading
import sys

# from peer import Peer


class Client: 

    def __init__(self, addr):
       
       self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
       self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

       self.s.connect((addr, 5000))

       self.previous_data = None
    
       
       i_thread = threading.Thread(target=self.send_message)
       i_thread.daemon = True
       i_thread.start()

    

       while True:

           r_thread = threading.Thread(target=self.recieve_message)
           r_thread.start()
           r_thread.join()

           data = self.recieve_message()

           if not data:
               
               print("-" * 21 + " Server failed " + "-" * 21)
               break

           elif data[0:1] == b'\x11':
               print("Got peers")
               
               self.update_peers(data[1:])




    def recieve_message(self):
       try:
           print("Recieving -------")
           data = self.s.recv(1024)

           print(data.decode("utf-8"))

           return data
       except KeyboardInterrupt:
           self.send_disconnect_signal()



    def update_peers(self, peers):
   
        p2p.peers = str(peers, "utf-8").split(',')[:-1]
    

    def send_message(self):
        try:              
            self.s.send("req".encode('utf-8'))

                # check if the user wants to quit the connection
                #if data[0:1].lower() == "q":
                #    self.send_disconnect_signal()

        except KeyboardInterrupt as e:
            self.send_disconnect_signal()
            return




    def send_disconnect_signal(self):
       print("Disconnected from server")
       self.s.send("q".encode('utf-8'))
       sys.exit()
