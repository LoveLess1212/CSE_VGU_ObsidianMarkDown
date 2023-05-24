# Creating Frames
* The [[Data Link Layer]] does among others
	* Identify the frames in the bit stream of the [[Physical Layer]]
	* pack the data packages of the Network Layer in frames
* It is required that the beginning of each frame is highlighted
	* Without markings, the receiver cannot detect the frame boundaries
* Different ways exist to mark the frames borders
	* **Character count in the header
	* **Byte/Character stuffing
	* **Bit stuffing
	* **Line code violation** of [[Physical Layer]] with illegal signals
* All these different procedures have advantages and drawbacks
# Character Count in the Frame Header
* The header of the frame contains among others the character count in the frame
* An example for a [[Data Link Layer]] [[Protocol]] that specifies the frames border with a length information in the frame header is the byte-oriented **Digital Data Communications Message [[Protocol]] (DDCMP)** of DECnet
* In each frame, the field Count contains the number of bytes payload inside the frame
 ![[Pasted image 20221206094601.png]]
* *Potential issue*: If the filed Count is modified during transmission, the receiver is unable to correctly detect the end of the frame
# Byte/Character stuffing
* A [[Protocol]], which highlights the frames border with special characters, is the byte- oriented (character-oriented) [[Protocol]] **Binary Synchronous Communication (BISYNC)**, which was invented by IBM in the 1960s
* ![[Pasted image 20221206094741.png]]
* Control characters(*Sentinel characters*) highlight the structure of the frames
* If the payload contains an ETX char, it must be **Protected** by a stuffed [[DLE]] in the [[Data Link Layer]]
* The [[DLE]] character is represented in the payload by sequence [[DLE]]
* The method is called Byte Stuffing or Character Stuffing, because the 
	* Sender *inserts*(stuffs) extra characters into the payload
	* Receiver *removes* the stuffed characters from the received payload, before passing it to the Network Layer
* Drawback:
	* Strong relationship with the ASCII character encoding
		* More recent protocols of this layer no longer operate byte-oriented, but bit oriented because this allows using any character encoding
# Bit Stuffing
* When bit-oriented protocols are used, each frame begin and end with a special bit pattern
* Examples: The [[Protocol]] [[HDLC]] and [[PPP]] which implements [[HDLC]]
	* Each frame begins and ends with the sequence 01111110
	* ![[Pasted image 20221206101038.png]]
* If the [[HDLC]] [[Protocol]] in the [[Data Link Layer]]
	* of the sender discovers 5 consecutive 1-bits in the bit stream from the Network Layer, it stuffs a 0-bit in the outgoing bit stream
	* of the receiver discovers 5 consecutive 1-bits, followed by a 0-bit in the bit stream from the [[Physical Layer]], it removes the 0-bit
* Advantages
	* Ensures that the start/ end sequence does not occur in the payload
	* Every character encoding can be used with this framing method
# Line Code Violations
* Depending on the line code used in the [[Physical Layer]], illegal signals can be used to highlight the frame boundaries
* If Token Ring is used, frames start with a byte (starting delimiter) which contains 4 line code violations
# Framing in current Computer Networks - Ethernet
![[Pasted image 20221206104202.png]]
* Up-to-date [[Data Link Layer]] protocols (e.g. Ethernet and WLAN) work bit-oriented and not byte-oriented  
	* Reason: This way, every character encoding can be used
* Preamble is a 7 bytes long bit sequence 101010 ... 1010 
	* Is used in bus networks (topologies) to synchronize the receiver with the clock and to identify clearly the beginning of the frame  
	* Is followed by the SFD (1 byte) with the bit sequence 10101011
* The fields for the physical addresses (MAC addresses) of sender and destination are 6 bytes long each  
* The 4 bytes long optional VLAN tag contains, among others. . .  
	* a 12 bits long VLAN ID (=⇒ see slide set 4)  
	* and a 3 bits long field for the priority information  
* The field Type contains the information what [[Protocol]] is used in the next upper [[Protocol]] layer

* If IPv4 is used, the field Type has value 0x0800  
* If IPv6 is used, the field Type has value 0x86DD  
* If the payload contains an [[ARP]] message, the field Type has value 0x0806
* Minimum size of an Ethernet frame: 72 bytes  
* Maximum size (including preamble and SFD): 1526 bytes  
* The VLAN tag increases the maximum size by 4 bytes

* Each frame can contain a maximum of 1500 bytes payload  
	* With the [[Pad field]], the frame length can be increased to the minimum frame size (72 bytes) when needed  
		* This is required to get the collision detection via CSMA/CD working  (=⇒ slide set 6)  
* The last field contains a checksum (32 bits) for all fields, except the preamble and SFD
* The Interframe Spacing or Interframe Gap is the minimum idle period between the transmission of Ethernet frames via the transmission medium  
* The minimum idle period is 96 bit times (12 bytes)  
	* It is 9.6 microseconds when using 10 Mbps Ethernet  
	* It is 0.96 microseconds when using 100 Mbps Ethernet  
	* It is 96 nanoseconds when using 1 Gbps Ethernet  
* Some network devices allow to reduce the Interframe Spacing period  
	* Benefit: Better data rate is possible  
	* Drawback: For the receiver it may become impossible to detect the frames’ borders (=⇒ the number of collisions may rise)
* In [[Physical layer]], the [[Protocol]] adds. . .  
	* a preamble to synchronize the receiver including a SFD  
		* The Short Preamble Format is an optional standard which is not supported by all devices  
* a Signal field, which specifies the data rate (Mbps)  
* a Service field, which may contains some information about the modulation method used  
* a Length field, which specifies the time in microseconds which is required to transmit the frame  
* a [[CRC]] field, which contains a checksum over the fields Signal, Service and Length
* `Maximum size of a WLAN frame (only the DLL part): 2346 bytes
* The field Frame Control (2 bytes) contains several smaller fields  
	* Among other things, here is the [[Protocol]] version specified and it is specified what sort of frame (e.g. data frame or beacon) this frame is and if the frame is encrypted with the WEP method  
* The field Duration ID (2 bytes) contains a duration value for the update of the counter variable Network Allocation Vector ([[NAV]])
* The content of the 4 address fields depends on whether the WLAN network runs in **infrastructure mode** or **ad-hoc mode** and if the frame has been sent from a terminal device or an Access Point  
* The MAC addresses are called **Basic Service Set Identifier** ([[BSSID]]) in this context
* Possible values (MAC addresses in the address fileds)
	* MAC of sender **Source add
	* MAC of Receiver **Destination add
	* MAC of next station on the route to the destination **Receiver add
	* MAC of last station which forwarded the frame **Transmitter Add
* The field Sequence Control (2 bytes) consists of a fragment number (4 bits) and a sequence number (12 bits)  
	* If a frame has been split into several fragments, the sequence number is equal for all fragments  
* The final field contains a [[CRC]] checksum (32 bits) for all fields, except the payload
#COMPUTER_NETWORK 