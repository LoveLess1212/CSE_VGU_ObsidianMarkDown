---
tags:
  - IT_SECURITY
---

# Problems and limits of Packet Filter
* There is no user-specific or - application specific filtering possible
	* The only thing we can put into this is Ip address
	* Problem
		* There is a lot of application run on the same IP address
* Possible way is using [[Transport Layer]]  information to identify application
	* information about source port & destination port 
	* Problem
		* There are certain number of app that the port number will change .-.
* Fragmentation can be problematic
	* Certain application for which the port number which are used might change 
		* Ex
			* FTP
			* Port number could be negotiated dynamically through channel
* Application with Varying port number 
* Tunneling and encryption
	* some [[protocol]] allow for tunneling other [[protocol]] by allowing encapsulating information from one [[protocol]] into another [[protocol]]
		 * This time, packet filter might take fake value, wrong conclusion will drawn
	 * Encryption
		 * if encryption happen, then of course packet filter will not in position to break it -> PF will have no clue about the information inside it -> can't make conclusion