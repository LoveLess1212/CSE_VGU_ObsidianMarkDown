- A multicast operation sends **a single message** from **one process** to **each of the members** of a **group of processes**.
- Usually there is no guarantee about **message delivery** and **ordering**.
- The membership is **dynamic**
	- A member can join and leave anytime
	- A member can join any group
## How is it useful?
- **Fault tolerance** due to replicas
	- A request is sent to group members. When some of members fail, a client can still be served.
- **Better performance** through replicas
	- Resources are replicated in the members of the group to increase the performance.
- **Propagation** of notifications
	- Messages are propagated to the members of the group.
#DISTRIBUTED_SYSTEM 
#COMPUTER_NETWORK 