**Variation:** Mobile Code, Two Tier
#DISTRIBUTED_SYSTEM 
#IT_SECURITY 
# Description
* In a [[Client-Server]] architecture, the functionality of the system is organized into services, with each service delivered from a separate server. Clients are users of these services and access servers to make use of them.
# Example
* Figure in the next slide is an example of a film and video/DVD library organized as a [[Client-Server]] system.
* ![[Pasted image 20230823154027.png]]
# When used
* Used when data in a shared [[Database]] has to be accessed from a range of locations. Because servers can be replicated, may also be used when the load on a system is variable.
# Advantage
* The principal advantage of this model is that servers can be distributed across a network. General functionality can be available to all clients and does not need to be implemented by all services
# Disadvantages
* Each service is a single point of failure so susceptible to denial of service attacks or server failure. Performance may be unpredictable because it depends on the network as well as the system. May be management problems if servers are owned by different organization
#SOFTWARE_ENGINEERING 