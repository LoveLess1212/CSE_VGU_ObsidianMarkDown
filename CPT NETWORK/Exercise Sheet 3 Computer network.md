1. Bridge:
	1. Connect two physical network by forward frame from one physical network to another physical network
2. How many port does a bridge provide:
	1. 2 
3. Diff between bridge and layer-2-switches:
	1. Layer-2-switches provide more port from 4- 48 interface
4. Why do Bridges and Layer-2-Switches not require physical or logical addresses?
	1. Because they are not actively participate in communication 
5. 2 implementation 
	1. WLAN Bridge - Modem
6. Advantage of *lerning bridge* in compare with dump bridge
	1. Bridge need to learn which devices connected through which port because it is not useful when Bridge forwards every frames
7. What information is stored in *Forwarding table*
	1. which devices connected through which port
8. What happens, if for a network device, no entry exists in the forwarding table of a Bridge?
	1. the Bridge will forward all frames
9. Why do Bridges try to avoid loops?
	1. Loop can reduce performance and can even lead to netowrk failure
10. What protocol use Bridges to handle loops?
	1. Spanning tree protocol
11. Explain spanning tree
	1. Spanning tree is a subgraph of of the graph that cover all node but remove edges to make cycle free 
12. What information contains the Bridge ID according to the IEEE?
	1. Bridge priority and address of mac address of the bridge port with lowest port ID
13. What is the difference between the Bridge ID according to the IEEE and the Cisco extended version of the Bridge ID?
	1. In Cisco extended version of Bridge ID, the Bridge ID now include Bridge priority (4 bits) and VLAN tag(16 bits) instead of 16 bits bridge priority
14. How many priority values can be encoded with the Bridge ID according to the IEEE?
	1. 65536 values
15. How many priority values can be encoded with the Cisco extended version of the Bridge ID?
	1. 2^4 = 16 values
16. Explain what a Bridge Protocol Data Unit (BPDU) message is and for what purpose it is used.
	1. The Bridge exchange information about the Bridge IDs and path cost via speacial frames, calles Bridge Protocol Data Unit (BPDU). The message is used by Spanning Tree Protocol.
17. What is the selection criteria for determining, whether a Bridge becomes the Root Bridge?
	1. Select the bridge with the lowest priority
**18. What is a Designated Bridge and what is its task?
	1. For each physical network, a single one of the directly connected Bridges needs to be selected  as responsible for forwarding the frames towards in the direction of the Root Bridge. This Bridge is called Designated Bridge for this network.**
19. How many Designated Bridges does a computer network contain?
	1. For each network,a single designated network exist
20. What is the selection criteria for determining, whether a Bridge becomes a Designated Bridge?
	1. Designated Bridge is **a bridge on each LAN that provides the minimum root path cost**.
21. What is the impact of Bridges and Layer-2-Switches on the collision domain?
	1. Bridges and Layer 2 Switches split the collision domain
22. Explain what a switched network is
	1. A fully switched network is a network where each port of the switches connect with only one network device -> no collision 
# Ex 5
1. How are physical network addresses called?
	1. Mac address (Media Access Control)
2. What protocol uses Ethernet for the address resolution?
	1. Ethernet uses the ARP - (Address Resolution Protocol)  to resolute the Logical address of the Network Layer (IPv4 address) to MAC addresses
	2. For IPv6, NDP (Neighbor Discovery Protocol) provides the identical functionality and operates similar way
3. Who receives a frame with the destination address FF-FF-FF-FF-FF-FF?
	1. This is broadcast address -> everyone in the network receive this frame
4. What is MAC spoofing?
	1. MAC address can be modified via software
# Ex 6
1. One way to mark the frames’ borders is via character count in the frame header. Name a potential issue that can arise from this method
	1. If the field count is modified during transmission, the receiver is unable to correctly detect the end of the frame
2. One way to mark the frames’ borders is via Byte Stuffing. Name a drawback of this method.
	1. Strong relationship with the ASC II encoding 
3. Advantage of Bit stuffing in compare with byte stuffing
	1. because they can use any character encoding 

# Ex 11
1. Why do computer networks use protocols for media access control?
	1. With Ethernet and WLAN, the network devices or stations use a shared transmission medium. Media Access Control Protocol needed to coordinate the media access to avoid collisions. 
2. Why use Ethernet and WLAN different media access control methods?
	1. In WLAN it is not guaranteed that all stations can detect all collisions
	2. In Ethernet with a shared transmission medium, each participant receives transmission of all other participant.
3. How do ethernet devices react, when they detect a collision?
	1. Stop the frame and sent jam signal to announce collision, If the maximum attempt not reached, wait a random amount of time and retransmit the frame
4. Explain why it is important that the transmission of a frame is not completed when a collision occurs in an Ethernet network.
	1. if the frame is completed, the network device might be finished with sending the frame and assumes that the transmission was successful 
5. How the network can ensure that the transmission of a frame is not completed when a collision occurs in an Ethernet network ??
	1. Each frame must have a certain minimum length. It must be dimension in a way that the transmission duration for a frame with minimum length does not fall below the maximum [[RTT]], this ensure the collision reach back to the sender before the transmission finished
6. Name the two special characteristics of the transmission medium in wireless networks that cause undetected collisions at the receiver.
	1. Hidden terminal problem
		1. When two device reach an access point, but between them have an object that they cant reach each other
	2. Fading
		1. When the access point in the middle of two device, so they can both reach the access point, but the length between them is too far, so they cant reach each other (decreasing signal strength due to obstacles or in free space )
7. done 
8. NAV is counter variable that each devices in the network manages by itself, 
9. Contention window is the time used to calculate the backoff time , to make the network not biased. The backoff time is is random value between min and max value of contention window. after the backoff time expired, the frame is transmitted.
10. Advantage and disadvantage of [[RTS]]/[[CTS]]
	1. Advantage
		1. fewer collision, because it solve the problem of hidden terminal
		2. Less energy consumption, because no transmission attempt during [[NAV]]
	2. Disadvantage
		1. reservation of the transmission medium cause delay
		2. [[RTS]] and [[CTS]] frames are [[overhead]]
# Exercise 12
1. What is Address Resolution Protocol?
	1. ARP is use to resolve IP address from [[Network Layer]] to [[Mac Address]] of Data Link Layer
2. What is [[ARP]] Cache?
	1. [[ARP]] cache is a table, contain IP address and [[Mac Address]] that go together. It is used to speed up the [[ARP]] process 
#COMPUTER_NETWORK 