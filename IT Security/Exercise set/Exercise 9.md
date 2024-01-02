---
tags:
  - IT_SECURITY
---

1. Describe the following terms briefly in 3-4 sentences
  1. [[Firewall]]
    1. [[Firewall]] is a network security system that [[monitors]] and controls the incoming and outgoing network traffic based on predetermined security rules. A [[firewall]] typically establishes a barrier between a trusted internal network and untrusted external network, such as the Internet.
  2. Packet filter
    1. Packet filter is a [[firewall]] technique used to control network access by monitoring outgoing and incoming packets and allowing them to pass or halt based on the source and destination IP addresses, protocols and ports.
  3. Application level gateway
    1. Application level gateway is a [[firewall]] system that works at the application layer of the OSI model and can monitor all traffic that passes through it for valid application layer [[protocol]] activity. It is also known as a proxy [[firewall]] or application proxy.
  4. Demilitarized zone
    1. is a physical or logical subnetwork that contains and exposes an organization's external-facing services to a larger and untrusted network, usually the Internet. The purpose of a DMZ is to add an additional layer of security to an organization's local area network (LAN); an external network node can access only what is exposed in the DMZ, while the rest of the organization's network is firewalled.
  5. Tunnel
    1. A tunnel is a virtual path or route between two end points through the internet. It is used to protect confidential data being sent over a public network. It is also used to implement [[VPN]].
2. How a packet filter works?
	1. Consist of many Rule chain and default action. Packet come to rule chain before come to default action
		1. Rule: It a feature that a packet can or can't have. If it can't compare with this rule, it will keep compare with the next rule until the end of the rule chain. If they don't match with any rule, Default action will be executed
		2. Default action: 
			1. Default Accept: accept any packet that have this feature
			2. Default Denied: deny any packet that have this feature
		3. Feature: Port number, Ip source or dest, ip ranges, which interface, flag, [[protocol]], date and time...
	2. Static and dynamic:
		1. Static: Only the packet are considered and solely dependent on the packet itself
			* Downside: Attacker could [[spoof]] a [[ACK]] packet and gain info, this can be solved using dynamic packet filter.
		* Dynamic: Information from previous packet might be taken into account
3. Explain NAT and how it works
	1. Because there are not enough IPv4 to use and private IP address should not be routed in public network. -> NAT: Network Address translation, is a technique used in computer networking to translate multiple private IP address -> single public IP address to communicate with external network.
4. Describe inherent weaknesses and vulnerabilities in the concept "[[Firewall]]"
	1. Limit:
		1. No user specific or application specific filtering possible, they solely see the IP
		2. the only way to identify application protocols is to use [[Transport Layer]] info
		3. Fragmentation can be come problematic, some info might not be present in the packet
		4. Application with vary port numbers:
		5. Tunneling: Some protocols allow tunneling, some encapsulates, info from one [[protocol]] to another [[protocol]]. With packet filters that take only header information as face value can lead to wrong conclusions
		6. Encryption: once encryption happen, packet filter might have no clue what might actually be inside the packet
5. 
  1. Describe how a static packet filter distinguishes between incoming and outgoing [[TCP]]-connections. Denote the corresponding rules in pseudo-notation or verbally.
	  1. Based on packet flag, TCP for example, intranet does not take any syn from the internet, but it can sent syn to the internet.
  2. Describe how a dynamic packet filter distinguishes between incoming and outgoing [[TCP]]-connections. Denote the corresponding rules in pseudo-notation or verbally.
	  1. Based on previous packet
6. A packet filter:  

| Nr. | IP Source  Address | IP Destination Address | [[Protocol]] | set Flags | considered Flags | Action |
| --- | ----------- | -------------- | ------- | ------- | ----------- | ------- | 
| 1   | 10.1.1.0/24 | 192.168.5.1    | TCP     | SYN     | SYN ACK     | DROP    | 
| 2   | 10.1.1.9    | 192.168.5.0/24 | TCP     | SYN ACK | SYN ACK     | DROP    |  
| 3   | 10.1.1.0/24 | 192.168.5.2    | TCP     | SYN ACK | SYN ACK     | ACCEPT  |  
| 4   | 10.1.1.7    | 192.168.5.0/24 | TCP     | SYN ACK | SYN ACK     | DROP    |
| 5   | 192.168.0.0/16 | 10.1.1.8       | TCP     | ACK     | ACK         | DROP    |
Default: ACCEPT
> table explaination:
> set Flags: the flag that the packet has
> considered Flags: the flag that the packet is
Assuming typical behavior (i.e. each TCP segment is transmitted in one IP packet), analyze
whether a TCP connection setup between the following hosts is successful or not.
For EVERY packet sent during connection setup, specify the characteristics of the connection and which of the rules is applied to the packet. Note: Usually, more than one packet is sent.
1. TCP connection setup from 10.1.1.5 to 192.168.5.1
2. TCP connection setup from 192.168.5.3 to 10.1.1.7
3. TCP connection setup from 192.168.5.2 to 10.1.1.7
4. TCP connection setup from 10.1.1.9 to 192.168.5.4
5. TCP connection setup from 192.168.5.9 to 10.1.1.8
1. TCP connection setup from 10.1.1.5 to 192.168.5.1  
    Packet 1:  
    Source IP: 10.1.1.5  
    Destination IP: 192.168.5.1  
    [[Protocol]]: TCP  
    Flags: SYN  
    Applied Rule: 1 (DROP)

The connection fails as the first packet is dropped by rule 1.

2. TCP connection setup from 192.168.5.3 to 10.1.1.7  
  Packet 1:  
  Source IP: 192.168.5.3  
  Destination IP: 10.1.1.7  
  [[Protocol]]: TCP  
  Flags: SYN  
  No matching rule, default ACCEPT applies.

	Packet 2:  
	Source IP: 10.1.1.7  
	Destination IP: 192.168.5.3  
	[[Protocol]]: TCP  
	Flags: SYN-ACK  
	No matching rule, default ACCEPT applies.
	
	Packet 3:  
	Source IP: 192.168.5.3  
	Destination IP: 10.1.1.7  
	[[Protocol]]: TCP  
	Flags: ACK  
	No matching rule, default ACCEPT applies.

The connection succeeds as no packets are dropped.

3. TCP connection setup from 192.168.5.2 to 10.1.1.7  
  Packet 1:  
  Source IP: 192.168.5.2  
  Destination IP: 10.1.1.7  
  [[Protocol]]: TCP  
  Flags: SYN  
  No matching rule, default ACCEPT applies.

	Packet 2:  
	Source IP: 10.1.1.7  
	Destination IP: 192.168.5.2  
	[[Protocol]]: TCP  
	Flags: SYN-ACK  
	No matching rule, default ACCEPT applies.
	
	Packet 3:  
	Source IP: 192.168.5.2  
	Destination IP: 10.1.1.7  
	[[Protocol]]: TCP  
	Flags: ACK  
	No matching rule, default ACCEPT applies.
	
	The connection succeeds as no packets are dropped.

4. TCP connection setup from 10.1.1.9 to 192.168.5.4  
    Packet 1:  
    Source IP: 10.1.1.9  
    Destination IP: 192.168.5.4  
    [[Protocol]]: TCP  
    Flags: SYN  
    Rule 2 applies (DROP)

The connection fails as the first packet is dropped by rule 2.

5. TCP connection setup from 192.168.5.9 to 10.1.1.8  
  Packet 1:  
  Source IP: 192.168.5.9  
  Destination IP: 10.1.1.8  
  [[Protocol]]: TCP  
  Flags: SYN  
  No matching rule, default ACCEPT applies.

	Packet 2:  
	Source IP: 10.1.1.8  
	Destination IP: 192.168.5.9  
	[[Protocol]]: TCP  
	Flags: SYN-ACK  
	No matching rule, default ACCEPT applies.
	
	Packet 3:  
	Source IP: 192.168.5.9  
	Destination IP: 10.1.1.8  
	[[Protocol]]: TCP  
	Flags: ACK  
	Rule 5 applies (DROP)

The connection fails as the third packet is dropped by rule 5.