# Ethernet (IEEE 802.3)
	- Several Ethernet standard exist 
		- Differ among  others in the data rate and the transmission medium used
	- Connection type to the medium is passive
# Variants
	- all variants are extensions of Thick Ethernet (10BASE5)
	- 2 diff transmission modes exist:
		1. Baseband (BASE)
		2. Broadband (BROAD)
### BASE
> in short:
> Baseband systems provide just a single channel

- Almost all Ethernet use BASE
- Cheapest possible band
- Have no carrier frequencies
	- data is directly trans on the transmission medium
- single band
### BROAD
- Data is modulated to a carrier frequency
	- allows to transmit mul signal at the same time in different frequency ranges (band)
- only 1-BOARD36 uses the broadband method
- THIS CONCEPT WAS NO SUCCESS **but** the concept is used many areas today in comm and telecommunication
## Token Ring
- Standard for LANS, in which the terminal devices are logically connected as a ring
- rate: 4mbps or 16mbps
- A **token** circles in the ring
	- It is passed from one node to the next one
- The **connection type** to the medium is **active**
	- This  means the network stations participate actively in the token passing
#### Function of Token ring
- Passed from one node to the next one
	- if a terminal dev wants to send data, it wais for the token frame
		- the terminal appends payload at the token
		- add the required control signals
		- set token bit from 0 to 1
	- If a data frame token reaches its destination, receiver copies the payload data and acknowledges the receive
		- The sender receives and sends token with next payload or puts a **free** token on ring
### WLAN

#COMPUTER_NETWORK