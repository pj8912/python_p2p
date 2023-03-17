# python_p2p
Peer-to-Peer network in python

This is a peer-to-peer network built using Python programming language. The network enables direct communication between nodes (peers) in the network without the need for a central server.

## Requirements
- Python 3.x
- Required packages:
  - `socket`
  - `threading`


## Quick Start 
  - Write `python3 peer.py ` on terminal to start.



- The peer.py file combines both the `server` and the `client` files together to create a `Peer` in the network. 
- This program starts creating a peer as the Server and then when the server is disconnected this program takes care making another peer as the server.
- This is done by constantly looping over the peers in list and try make all peers as clients and then try making itself as the server.



## Features
- Direct communication between nodes in the network.
- Dynamic discovery of other nodes in the network.
- Ability to send messages to other nodes in the network.

## Limitations
- The network does not support secure communication and is vulnerable to hacking and eavesdropping.


## Hybrid approach

In a hybrid approach, both client and server components play a role in managing the peer list and maintaining the P2P network. 
Check out [Hybrid approach](https://github.com/pj8912/python_p2p/tree/main/hybrid-approach)



## Contribute
- If you are interested in contributing to the development of the P2P network, you can create a pull request with your changes. All contributions are welcome and appreciated.
