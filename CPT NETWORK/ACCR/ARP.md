> Address Resolution [[Protocol]] 
> used to resolve IP address of the [[Network Layer]] of [[MAC address]] of the [[Data Link Layer]]
# function
* If a network device wants to transmit data to a receiver, it uses the receiver's IP address on the Network Layer
* But on the [[Data Link Layer]], the [[MAC address]] is required
	* Therefore, address resolution must be carried out in the [[Data Link Layer]]
	* To find out the [[MAC address]] of a Network device in the LAN, ARP sends a frame with the MAC broadcast address FF-FF-FF-FF-FF-FF-FF as destination address
		* Each network device in the LAN receives and analyzes this frame
		* The frame contains the IP address of the searched network device
	* If a network device has this IP address it send an ARP response to the sender
		* The reported [[MAC address]] stores the sender in it's local **ARP cache**
* **ARP cache** is used to speed up the address resolution
	* It contains a table with these information for each entry:
		* [[Protocol]] type (IP)
		* [[Protocol]] address of the sender (IP address)
		* Hard address of the sender ([[MAC address]])
		* Time To Live (TTL)
	* The TTL is set by the operating system
	* If an entry in the table is used, the TTL is extended
* Modern Linux distributions discard entries after 5 mins
oldest network [[Protocol]] still in use

#COMPUTER_NETWORK 