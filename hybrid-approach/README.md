# Hybrid approach

In a hybrid approach, both client and server components play a role in managing the peer list and maintaining the P2P network. This approach is useful for balancing the responsibilities between clients and servers in the network, making it more flexible and resilient.

Here's a basic outline of a hybrid approach:

- When a node starts, it acts as a client and connects to the bootnode to request the peer list.
- The bootnode sends the current peer list to the connecting node.
- After receiving the peer list, the node updates its local peer list and starts acting as a server, listening for incoming connections.
- The server component of the node periodically connects to the bootnode to update its local peer list and also to notify the bootnode about its presence in the network.
- The bootnode maintains an updated peer list based on the information it receives from the nodes in the network.

In this hybrid approach, nodes not only act as clients when connecting to the bootnode but also maintain their server component to listen for incoming connections and update their peer list. This allows for a more dynamic and fault-tolerant network topology, as each node actively participates in maintaining the network.

