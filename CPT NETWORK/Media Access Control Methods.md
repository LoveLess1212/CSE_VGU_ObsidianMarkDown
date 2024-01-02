*  With Ethernet 10BASE2/5, WLAN, and PowerLAN (Powerline Communication), the network devices or stations use a shared transmission medium (channel) 
	* To coordinate the media access and to avoid collisions, media access  control methods are required  
		* Ethernet uses the media access control method [CSMA/CD](CD)  
		* WLAN and PowerLAN use the media access control method [CSMA/CA](CA)
* Bluetooth is not discussed here, because Bluetooth devices are organized in piconets  
	* In each piconet, the master coordinates the media access
# Function of [CSMA/CD](CD)
* If a network dev wants to transmit frames via Ethernet, it operates according to the following sequence
1. Monitor the transmission medium (channel)
	* Transmission medium (channel) is idle -> step 2
	* Transmission medium (channel) is busy -> step 3
2. Start transs and continue to monitor the transs medium (channel)
	 * Success transmission
		 * Send success message to upper network layers-> step5
	 * collision is detected
		 * Stop frame transmission and send the 48bits long message to announce the collision-> step 3
 3. transmission medium (channel) is busy. Check the number of transmission attempts
	 * Maximum number not yet reached
		 * Wait a random time -> step 1
		 * The random time is calculated using the backoff method
	 * Maximum number is reached -> step 4
 4. Error
	 *  Maximum number of transmission attempts reached
	 *  Send error message to upper network layers -> step 5
 5. Leave transmission mode
![[Pasted image 20221207120215.png]]
# Network Size and Collision Detection
* A collision must be detected by the sender
* Each frame must have a certain minimum length
	* It must be dimensioned in a way, that the transmission duration for a frame with minimum length does not fall below the maximum [[RTT]]
	* This ensures that a collision reaches the sender before its transmission is finished
		* If a sender detects a collision, it knows that its frame has not arrived correctly at the receiver, and can try the trans **again later**

> minimum frame length for Ethernet: 64Bytes
> Maximum length of the physical network depend on the Ethernet standard used

The minimum frame length, where collision detection is still possible is calculated as follow

>$P = 2*U*(\frac{D}{V})$
	P = Minimum frame length in bits
	U = Data rate of the transmission medium (channel) in bits per second
	D = Network length in meters
	V = Signal speed on the transmission medium (channel) in meters per second
[]()
Ex:
![[Pasted image 20221207121812.png]]

# Velocity Factor
* The velocity factor, also called wave propagation speed, depend on transmission medium (channel) and is 
	* 1 for vacuum
	* 0.64 for twisted pair cable cat-5e
	* 0.65-0.66 for coaxial cables RG-58
	* 0.67 for optical fiber
	* 0.77-0.78 for coaxial cables
* Describes the speed of a signal on a transmission medium (channel) relative to the speed of light

* Maximum network size, where collision detection is still possible is calculated as follow

> $2*Smax=V*t-frame$
> Smax = Maximum network size with collision detection
> V = Signal speed of the transmission in meters per second
> t- frame = transmission duration of a frame in seconds

![[Pasted image 20221207122421.png]]

## CSMA/[[CD]] Nowadays
* The media access method [CSMA/CD](CD) **is absolutely necessary** only for Ethernet networks, which implements the **[[Bus Network]] technology**
	* [[Reason]]: in a [[Bus Network]] [[topology]], all network devices are directly connected to a shared transmission medium (channel)
* Almost all Ethernet-based network nowadays are **fully switched networks** and therefore **collision free**
# [[Media Access Control Methods]] of Wlan
* [CSMA/CD](CD) cannot be used with wireless networks
* With CSMA/[[CD]], the sender detects occurring collisions
	* In wired networks with a shared transmission medium (channel), each participant receives the transmission of all other nodes
		* Therefore, each node detects any collision
	* For wireless networks like WLAN, this is not always the case
		* Therefore, the media access method CSMA/[[CA]] is used, which tries to minimize the occurrence of collisions
* Special challenges of the transmission medium (channel) in wireless networks cause undetected collisions at the receiver
	* [[Hidden terminal problem]]
	* [[Fading]]
## Wlan (802.11) Implements 3 diff [[Media Access Control Methods]]
1. [CSMA/CA](CA)
	* Strategy: Listen before talk
	* Collision avoidance via random backoff time
	* Minimum spacing between frames, when a sequence of frames shall be transmitted
	* Acknowledgements - [[ACK]] (not for broadcast)
	* Default method which is implemented in all WLAN dev
2. [CSMA/CA](CA) [[[RTS]]/[[CTS]]](obsidian://open?vault=Study&file=[[RTS]]%20CTS)
	* Solves the problem of hidden terminals
	* Optional method and implemented in most WLAN devices
3. [CSMA/[[CA]] [[PCF]]](CSMA [[CA]] PCF)
	* Access Point controls the access to the transmission medium (channel)
	* Optional method and seldom implemented
# Transmission of Frames
* If a node,which transmits frames, detects a collision via CSMA/[[CD]], it aborts the transmission of the frame
* WLAN does not use collision detection, but with CSMA/[[CA]] it implements collision avoidance (actually it is just a collision minimization)
	* If a station starts transmitting a frame, it will send the entire frame in any case
		* Once a station has started transmitting, there is no turning back
	* The sender must therefore be able to detect if a frame has not arrived correctly at the receiver
		* Solution: The receiver confirms by [[ACK]] that the frame was received

## [CSMA/CA](CA) [[PCF]] 






#COMPUTER_NETWORK 