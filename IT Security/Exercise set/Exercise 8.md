---
tags:
  - IT_SECURITY
---
1. Depict potential threats when communication over a network.
	1. Unauthorized 3rd party can stay anywhere in the network and they can:
		1. Manipulate: Change or alter the info that should be 
		2. Disrupt: if you cannot hack it, break it. they can break the communication
		3. [[Spoof]]: Impersonate the sender, but the receiver cannot distinguish it
		4. Intercept: gain access to the info bw the sender and receiver
2. Explain why an attacker might manipulate routing in a network
	1. The information flow to the router bf to the receiver. If an attacker have access to one of the immediate stations, it is very easy for them to do the attack. Many of the attack are based on routing the traffic over a station that is under control of the attacker. The structure of the internet make it easy to do so.
3. Explain the following attack
    1. [[Mac Address]] Spoofing
	    1. This is the technique where the attacker changes the [[MAC address]] of their devices to impersonate other devices on the network. This allows the attacker to Bypass [[MAC address]] filtering and access to the restricted area of the network. 
    2. [[ARP]] Spoofing
	1. aka MitM attack, that help attacker intercept communication between network devices. Where attacker send fake [[ARP]] message over a local network in order to link attacker's [[MAC address]] with the IP address of sender and receiver on the the network. this allow attacker to intercept the traffic bw the sender and receiver.
	    1. To do so, the attacker could do the following:
		    1. must have access to the network
		    2. using some tool to send out forged [[ARP]] response
		    3. the [[ARP]] being sent out and fool both the sender and receiver to connect to your machine instead of each other 
		    4. now the attacker is secretly in the middle of all communication
    3. IP Spoofing
        1. IP spoofing is the technique where the attacker changes the source IP address in the packet header to a fake IP address. This allows the attacker to impersonate other devices on the network or hide the identity of the attacker or both.
        2. IP spoofing can be used to perform DDoS attacks or bypass access control lists - [[firewall]].
    4. [[TCP]] sequence number attack
	    1. A impersonates C in a 3-way handshake. A (impersonating C) sends SYN to server B
	    2. B then responds by sending a SYN-ACK with sequence number = server -> C
	    3. C for some reasons does not responds to B (due to previous attack by A)
	    4. A then guesses the server sequence number and +1 to it as ACK for the ACK respond and SEQ = client number +1 (Previously created by A)
	    5. A successful connection is establish between A and B if A successfully guessed the sequence number
	    6. There were a vulnerability to guess a sequence number
	    7. In the past there were trust relationships between machines. A could use this to add its IP to B's trust relationships, close the connection and uses the trust relationship
	This is no longer available bcs SEQ number is random
    1. Phishing
	    1. Attacker runs a serice that looks like a legitimate service. The attacker then sends out emails to the victim that looks like it is from the legitimate service. The email contains a link to the fake service. The victim then clicks on the link and enters their credentials. The attacker then has the victim's credentials.
    2. Pharming / DNS Spoofing
		1. For pharming, the attacker manipulate/poison the DNS server [[protocol]]. There are vulnerability of the system that can be misused by the attacker. The attacker can manipulate the dns server or the machine( the victim) to redirect the traffic to the attacker's machine. The attacker can then use the victim's machine to do the attack.
5. Discuss advantages and disadvantages of security mechanisms and protocols on all layers of the network reference model and compare them. Also, give an examples for their use.
* **Application layer security**: The application programmer has to take care of all the security needs of the application (CIA) - everything.
	* Advantage: Allow to use networks which are completely unsafe, independent of mechanisms of other layers, the protection is truly between the sender and the receiver
	* Disadvantage: Complexity of application increases, it is difficult to reuse components within the applications, each and every software may have its own mechanism in the worst case
	* examples: email encryption by the use of certificates, if the user would encrypt a file b4 the file is transmitted
* **[[transport layer]] security**: the unencrypted data is handed over from the application layer to the [[transport layer]], the [[transport layer]] transmit the encrypted data through the network, and is decrypted by the receiver's [[transport layer]] and handed over to the application layer
	* Advantage: The application programmer does not have to take care of the security needs of the application, the [[transport layer]] takes care of it (good reuseability)
	* Disadvantage: Not end-to-end, we cannot make sure that the whole [[transport layer]] is encrypted, also the data is unencrypted in the middle of the [[transport layer]]. -> not enough
	* examples: TLS, SSL
* **[[Network layer]] security**: Secure communication between 2 intermediate stations on the [[network layer]] between 2 routers or a router and an endpoint(not end-to-end), transparent to the above layers.
	* advantages: high flexability (possible to provide security on parts of the communication flow), transparet to the above layers (no changes to above layers to deploy these mechanisms)
	* Disadvantage: Transparency is also bad because it is impossible or very difficult to intentionally employ these mechanisms
	* examples: Vitual network machine
* **Data link layer security**: Authentication, authorization and access control
	* Advantage: Allow to control which station are granted access to the Data link layer within the network
	* Disadvantage: Not end-to-end, only between 2 intermediate stations

> [!end to end security meaning]
> the data is encrypted at the sender and decrypted at the receiver. The data is not decrypted in the middle of the communication. 

* Why Network Security happes in Application layer? - We cannot reuse the [[protocol]], but this is also very complex
* Security on [[transport layer]]: Tcp is a transport level [[protocol]] of the internet that provides reliable, end to end communication between two processes. But protect end to end communication is hard, because then all the data need to encrypt from end to end and to make sure that devices communicate with the right endpoints is complicated
You need to use at least 4 encrypted [[protocol]] for sending a message => all of the mechanism are important and must be implemented parallel in order to have a secure communication