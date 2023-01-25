# python_p2p
Peer-to-Peer network in python

I use python sockets to create a peer-to-peer network. The server and client files are separate from each other.

## Quick Start 
  - Write `python3 peer.py ` on terminal to start.



- The peer.py file combines both the `server` and the `client` files together to create a `Peer` in the network. 

- This program starts creating a peer as the Server and then when the server is disconnected this program takes care making another peer as the server.

- This is done by constantly looping over the peers in list and try make all peers as clients and then try making itself as the server.

