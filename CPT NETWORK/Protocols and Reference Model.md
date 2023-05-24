

## Diff forms of communication
 Connectionless comm
		- Analogous to a mailbox
		- Sender transmits messages without prior connection establishment
		- Disadvantage:
			- No validation that segment arrive
		- Benefit: Better throughput, bcs of lesser [[overhead]]
	- Connection-oriented communication
		- Analogous to a telephone
		- Prior data exchange , a connection is established bw sender and receiver
			- the connection is not termination, even if no data is transmitted
		- After all data is exchanged, the connection becomes terminatino by one of the communication parters
		- Immplements flow control and congestion control

## How communication works
-  Vertical communication
	- Mess are packed from top to bottom layer by layer and extracted at the receiver in the reverse layer sequence
	- Data encapsulation and de-encapsulation


# Reference model '
> [!def]
> Communication in computer networks is subdivided into **reference models**

 * Each **layer** of a reference model handless a particular aspect of communication and offers **interfaces** to the overlying layer and underlying layer
 * Each interface consists of a set of **operations**, which together define a **service**
 * In the layers, the data is encapsulated (**encapsulation**)
 * Because each layer is complete in itself, single protocols can be modified or replaces without affecting all aspects of communication
 * The most pop ref models are..:
	 * The **TCP/IP reference model**
	 * **OSI**
	 * **Hybrid**
## TCP/IP Ref model - message structure
- Problem: Too simple
- Each layer adds additional inf as **header** to the message
## Hybrid Ref model (BEST ONES)
- BCS TCP/IP is often presented in literature as a 5-layer model
	-> make sense to split the link layer into 2 layers, bcs they have diff task
- Is extension of TCP/IP
### [[Physical Layer]]
- Transmits the ones and zeros
	- Physical connection to the netowrk
	- Conversion of data in signals
- [[Protocol]] and transmission medium specipy among others
- Devices: Repeater(amplify analog signal), Hub (multiport Repeater)
### [[Data link layer]]
- Ensures errors-free data Exchange frames bw dev in physical networks 
	- Detects tranmission errors with checksum
	- Controls the acces to the transmisstion medium
- [[Protocol]] to ensure only one person send per time
- specify physical nw add ([[MAC address]])
- Devices: Bridges, layer-2-switches
### [[Network layer]]
- Forwards packets bw network
- the nw layer defines logical add (IP addresses)
- Each IP packet is routed indept to its destination and the path is not recorded
- Routers and Layer-3-Switches connect logical networks
- Usually the connecctionless Internet [[Protocol]] (IP)
### Transport Layer
- Transports segments betweek process on diff devices - end to end protocols 
- Addresses processes with port numbers
- Transport implement diff form of communication
### Aplication Layer
- Contains all protocols, that interact with the app (brower or email program)
- Here are the messages (E.g. HTML pages or emails), formated according to the used app [[Protocol]]
- Some app layer protocols: HTTP, FTP, SMTP, POP3, DNS, SSH, Telnel


## OSI Reference Model
- Some years after the TCP/IP ref model OSI was developed from 1979 onwards
	- 1983: Standardized by the intern. Organization for Standardlization(ISO)
	- OSI: Open Sytem Interconnecetion
- Similar to TCP/IP 7 layers
### Session Layer
- Controls the dialogues
	- control wi
	- Provides checkpointing which is useful for longer data trans to enable sync
		- if connection fails, returning to a checkpoint
	- Protocols that meet the required capabilities of the Session layer are Telnet for remote controlling computers and FTP for file transmission
- BUT: THIS [[Protocol]] ARE DEAD
### Presentation layer
- Contains rules for setting the format (presentation) of messages
	- The sender can notify the receiver that a message has a specific format
		- Data types and their length can be def here
		- Compression -
- REAL LIVE NEVER USE

## CONCLUSION:
- The **hybrid_ref_model** illustrates the functioning of computer networks in a relistic way
		- It combines the ad of TCP/IP ref and the OSI ref model, without taking over their drawbacks
		- distinguished bw the [[Physical Layer]] and Data Link Llayer
			- This is useful, bcs obj differ a lot
		- It does not sub divide the Applicationn Layer
			-  This is not useful and does not take plae in practice
			-  Functionalities, whichare intended for Session Layer and Presentation Layer, are provided by Application Layer protocols and services


#COMPUTER_NETWORK