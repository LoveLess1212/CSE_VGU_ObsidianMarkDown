1. Describe the following Term briefly in 3-4 sentences:
	1. VPN
		- VPN is a technology that create a secure and encrypted connection over a public network, such as the internet. Allow seemingly direct connection between two station using unsecure/ unsafe network as a connection media
	2. RAS (Remote Access Service)
		*  is VPN temporary connection from a VPN client in the public network to a VPN server that is inside the private network to create a secure connection
	1. Site to site VPN
		* is a (permanent) connection setup between multiple networks. This could be a corporate network where multiple offices are connected to each other.
2. Explain and describe how [[IPSec]] works in detail. In your explanation, the terms **[[Authentication header]]**, **[[Encapsulating security payload]]**, **Tunnel Mode** and **transport mode** should be addressed. Also, describe what the Sequence number in [[Authentication header|AH]] and [[Encapsulating security payload|ESP]] is used for.
	1. [[IPSec]] is a [[protocol]] suite for secure IP communications that authenticates and encrypts each IP packet of a communication session. Placed in the [[Network Layer]] of OSI model
	2. Component:
		1. [[Authentication header|AH]]: add a header that contains sender auth data and protects the packet contents from modification by unauth parties. It alerts the recipient of possible manipulations of the original data packet
		2. [[Encapsulating security payload|ESP]]: perform encryption on the entire IP packet or only the payload. [[Encapsulating security payload|ESP]] adds a header and trailer to the data packet upon encryption
		3. [[Internet Key Exchange|IKE]]: is a [[protocol]] that establishes a secure connection between two devices on the internet. Both devices set up security association (SA), which involves negotiating encryption keys and algorithms to transmit and receive subsequent data packets.
	3. Tunnel mode
		1. the [[IPSec]] tunnel mode is suitable for transferring data on public networks as it enhances data protection from unauthorized parties. The computer encrypts all data, including the payload and header, and append new header to it.
	4. Transport mode
		1. [[IPSec]] transport mode encrypts only the data packet's payload and leaves the IP header in its original form. The unencrypted packet header allows routers to identify the destination address of each data packet. Therefore, [[IPSec]] transport mode is used in a close and trusted network, such as securing a direct connection between two computers.
	5. The sequential number assigned to each data packet and performs checks to detect signs of duplicate packets.
3. Explain and describe how [[OpenVPN]] works in detail. In your explanation, the terms tun-device and tap-device should be addressed 
	1. Open VPN is a virtual private network system that implements techniques to create secure [[point-to-point]] or site-to-site connections in routed or bridged configurations and remote access facilities.
	* [[OpenVPN]] works by creating virtual interfaces in user space under linux. It setup 2 virtual interfaces, which are [[point-to-point]] interfaces connecting 2 routers. this is how [[OpenVPN]] displayed in the router.
		* in fact, there is no [[point-to-point]] connection, but it is encrypted and encapsulated and sent over the public interface by using [[TLS SSL|SSL]]/[[TLS SSL|TLS]] transport connection
	* Is very flexible and can transfer traffic either from the network layer as well as from the data link layer:
		* If used on network layer -> tun devices
		* If used on data link layer -> tap device