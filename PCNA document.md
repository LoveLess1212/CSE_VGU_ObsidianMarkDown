
- sudo ethtool -p enp1s0f0
*- - > choose the right interface to set the link up*
* use cable to connect computer together
- *sudo ip link set enp1s0f0 up*
	* - -> set the link up
- *sudo ip address add 192.168.2.x/24 dev enp1s0f0 (x is for the number of the machine )
	- *example:* 192.168.2.107/24 (24 is for small network)
	- set up ip address *192.168.2.105/24* for the *enp1s0f0* interface
*- identify the interface for the router*
	- *sudo ethtool -p enp2s0f0* // show light  
		Initiates  adapter-specific  action  intended  to  enable an operator to easily identify the adapter by sight.  Typically this involves blinking one or more LEDs on the specific network port. *(linux manual)***
	- sudo ip link set enp2s0f0 up
		* set up ip address *192.168.2.105/24* for the *enp1s0f0* interface
- *sudo ip address add 10.16.0.200/16 dev enp2s0f0*
		- set up ip address for enp2s0f0
* *ip route show*
	* show the routing table
- *sudo ip route add default via 10.16.0.200 dev enp2s0f0*
	- add the default gateway into the routing table
- *sudo sysctl -w net.ipv4.ip_forward=1*
	- enable ip forwarding (for the router)
* *sudo vim /etc/resolv.conf*
	*  change the "nameserver 8.8.8.8" (every cpt)
- Use wireshark
## question2
- ip neighbor
	- Show arp table
- ip a show enp1s0f0
	- show address of enp1s0f0 interface
- ip route 
	- show routing table
- traceroute google.com
	- trace the route from google website
- echo hello | netcat 8.8.8.8 443
	- sent a hello message to google on port 443
- ss -tp 
	- show information about TCP and process
- ss -lnup
	- show list UDP process
-  nmap -p 1-1023 192.168.2.1
	- scan port from range 1-1023 on router 192.168.2.1
-  nmap -p- 192.168.2.0/24
	- scan all port on the routers
- nc -ltv 5342 
	- opening listening tcp server on port 5342
* sudo ip n flush all
	* delete arp table

