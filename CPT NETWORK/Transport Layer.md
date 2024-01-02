# Mission
* Guaranteed data transmission
* Ensuring the correct delivery order
* Support for data transmissions of any size

> Good for convert network negative characteristics into the positive characteristic
[[Transport Layer]]
# [[Protocol]] 
* [[UDP]]  (User Datagram [[Protocol]])
	* Connectionless Transport Layer [[Protocol]]. Transmission take place without previous connection establishment
	* More simple [[protocol]] in contrast to the connection-oriented [[TCP]].  Only responsible for addressing of the segments. Does not secure the data transmission
* [[TCP]] (Transmission Control [[Protocol]])
	* Connection-oriented Transport Layer [[protocol]]
	* Makes connections via IP reliable in a way that is desired or simply necessary for many applications
	* Guarantees that segments reach their destination completely and in the correct order. Lost or unacknowledged [[TCP]] segments are requested by the receiver at the sender.

![[Pasted image 20230626135503.png]]
	* [[TCP]] use 3 way handshake where both communication partner exchange control information in three steps
	* **Establish**
		* A -> SYN -> B 
		* B -> [[ACK]], SYN -> A
		* A -> [[ACK]] -> B
		* Data
	* **Data Transmission**
	* Data ter

#COMPUTER_NETWORK 