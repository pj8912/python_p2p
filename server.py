import socket
import threading
import sys



class ServerConnection: 


    def __init__(self, msg):
        try:
            
            self.msg = msg

            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            self.connections = []
             
            self.peers = []
            
            self.s.bind(('127.0.0.1', 5000))
            
            self.s.listen(1)

            print("-" * 12+ "Server Running"+ "-" *21)
            
            self.run()
        except Exception as e:
            sys.exit()


    def handler(self, connection, a):
        try:
            while True:
                # server recieves the message
                data = connection.recv(1024)
                for connection in self.connections:
    
                    # The peer that is connected wants to disconnect
                    if data and data.decode('utf-8')[0].lower() == 'q':

                        # disconnect the peer 
                        self.disconnect(connection, a)
                        return
                    elif data and data.decode('utf-8') == "req":
                    
                        connection.send(self.msg)
                        
        except Exception as e:
            sys.exit()


    def disconnect(self, connection, a):
        self.connections.remove(connection)
        self.peers.remove(a)
        connection.close()
        self.send_peers()
        print("{}, disconnected".format(a))
        print("-" * 50)



    
    def run(self):
        # constantly listeen for connections
        while True:
            connection, a = self.s.accept()

            # append to the list of peers 
            self.peers.append(a)
            #print("Peers are: {}".format(self.peers) )
            self.send_peers()
            count = 0
            for peer in self.peers:
                print(count ,peer[0], "", peer[1])
                count += 1

            # create a thread for a connection
            c_thread = threading.Thread(target=self.handler, args=(connection, a))
            c_thread.daemon = True
            c_thread.start()
            self.connections.append(connection)
            print("{}, connected".format(a))
            print("-" * 50)



    
    def send_peers(self):
        peer_list = ""
        for peer in self.peers:
            peer_list = peer_list + str(peer[0]) + ","

        for connection in self.connections:
          
            data = b'\x11' + bytes(peer_list, 'utf-8')
            connection.send(b'\x11' + bytes(peer_list, 'utf-8'))
