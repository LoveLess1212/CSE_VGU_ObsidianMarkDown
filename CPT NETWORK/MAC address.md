>[!in short]
>Address of [[data link layer]]
>AKA physical network address (nothing related to logical address)

* Ethernet uses the **Address Resolution [[Protocol]]** ([[ARP]]) to resolute the logical address of the [[Network Layer]](IPv4 addresses) to MAC addresses
	* For IPv6, the **Neighbor Discovery [[Protocol]]**(NDP) provides the identical functionality and operates in a similar way
* MAC addresses have a **length** of **48 bits** (6 bytes)
	* -> total $2^{48}$ possible addresses
* In order to make the representation compact and human- friendly to read, MAC addresses are usually **written in hexadecimal notation**
	* The bytes are separated from each other with dases ( - ) or colons ( : ) 
>Example of the notation: 00-16-41-52-DF-D7
* Each MAC address is intended to be permanently assigned to a network device and unique
	* But it is often possible to modify MAC addresses by software
		* However, this modification applies only until the next reboot of the computer
* **MAC broadcast address**
	* If a network device wants to send a frame to all other devices in the same physical network, it inserts MAC broadcast address in the destination address field of the frame
	* All 48 bits of this MAC address have the value 1
	* Hexadecimal notation: FF-FF-FF-FF-FF-FF
	* Bridges and Switches do not forwarded frames to other physical networks, that contain the MAC broadcast address in the destination address field
# Uniqueness of MAC Addresses
* The first 24 bits of the MAC address space are managed by the Institute of Electrical and Electronics Engineers (IEEE)
	* These 24 bits long addresses are called MA-L (MAC Address Block Large) or OUI (Organizationally Unique Identifier)
	* The OUIs can bet checked in this IEE database:
* The remaining 24 bits are specified by the hardware vendors independently for their network devices
	* That address space allow $2^{24}=16,777,216$ individual device addresses per OUI
* Smaller address spaces are available too: **MA-S** (MAC Address Block Small) and **MA-M** (MAC Address Block Medium)
# Security Aspects of MAC Addresses
* For WLAN, MAC filters are often used to protect the Access Point
	* In principle, this makes sense, because the MAC address is the unique identifier of a network device
* However, the security level of MAC filters is low because MAC addresses can be modified via software
	* The method is called **MAC spoofing**
>[!Working with MAC addresses under Linux]
>- Read out the own MAC address(es): ip link of ifconfig
>- Read out the MAC addres(es) of the neighbors (mostly the Routers): ip neigh
>- Set MAC address: ip link set dev "Interface" address "MAC Address"
>- Alternative: ifconfig "interface" promisc 
>- and next: ifconfig "Interface" hw ether "MAC Address"



#COMPUTER_NETWORK 