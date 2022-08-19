import socket
import threading
import sys

# from peer import Peer


class Client: 

    def __init__(self, addr):
       # set up socket
       self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

       # allow python to use recently closed socket
       self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

       # make the connection
       self.s.connect((addr, 5000))

       self.previous_data = None
    
       # create to work on a different thread
       i_thread = threading.Thread(target=self.send_message)
       i_thread.daemon = True
       i_thread.start()

       # send the message requesting data

    

       while True:

           r_thread = threading.Thread(target=self.recieve_message)
           r_thread.start()
           r_thread.join()

           data = self.recieve_message()

           if not data:
               # means the server has failed
               print("-" * 21 + " Server failed " + "-" * 21)
               break

           elif data[0:1] == b'\x11':
               print("Got peers")
               # first byte is the byte '\x11 we added to make sure that we have peers
               self.update_peers(data[1:])




    """
        This thread will deal with printing the recieved message
    """
    def recieve_message(self):
       try:
           print("Recieving -------")
           data = self.s.recv(1024)

           print(data.decode("utf-8"))


        #    if self.previous_data != data:
        #        fileIO.create_file(data)
        #        self.previous_data = data
           #  download the file to the computer
            
           return data
       except KeyboardInterrupt:
           self.send_disconnect_signal()






    """
        This method updates the list of peers
    """
    def update_peers(self, peers):
   
        p2p.peers = str(peers, "utf-8").split(',')[:-1]
    

    """
        This method is used to send the message
        :param: msg -> The optional message to send 
    """
    def send_message(self):
        try:
            #while True:
                # sleep for a little bit as to for the main thread to run
                #data = input("Please enter a message: ")

                # encode the message into bytes
                # other code will run when this happens as the thread is busy
                # request to download the file
            self.s.send("req".encode('utf-8'))

                # check if the user wants to quit the connection
                #if data[0:1].lower() == "q":
                #    self.send_disconnect_signal()

        except KeyboardInterrupt as e:
            # If a user turns the server off due to KeyboardInterrupt
            self.send_disconnect_signal()
            return




    def send_disconnect_signal(self):
       print("Disconnected from server")
       # signal the server that the connection has closed
       self.s.send("q".encode('utf-8'))
       sys.exit()