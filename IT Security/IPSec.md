---
tags:
  - IT_SECURITY
  - ongoing
---
1. IPsec is a protocol suite for secure IP communications that authenticates and encrypts each IP packet of a communication session. Placed in the [[Network Layer]] of OSI model
	2. Component:
		1. [[Authentication header|AH]]: add a header that contains sender auth data and protects the packet contents from modification by unauth parties. It alerts the recipient of possible manipulations of the original data packet
		2. [[Encapsulating security payload|ESP]]: perform encryption on the entire IP packet or only the payload. ESP adds a header and trailer to the data packet upon encryption
		3. [[Internet Key Exchange|IKE]]: is a protocol that establishes a secure connection between two devices on the internet. Both devices set up security association (SA), which involves negotiating encryption keys and algorithms to transmit and receive subsequent data packets.
	3. Tunnel mode
		1. the IPsec tunnel mode is suitable for transferring data on public networks as it enhances data protection from unauthorized parties. The computer encrypts all data, including the payload and header, and append new header to it.
	4. Transport mode
		1. IPsec transport mode encrypts only the data packet's payload and leaves the IP header in its original form. The unencrypted packet header allows routers to identify the destination address of each data packet. Therefore, IPSec transport mode is used in a close and trusted network, such as securing a direct connection between two computers.
# Protocols that belong
* IP
* TCP
* AH
* EPS
* [[TLS SSL|TLS]]
* UDP
* ESP
* Ethernet