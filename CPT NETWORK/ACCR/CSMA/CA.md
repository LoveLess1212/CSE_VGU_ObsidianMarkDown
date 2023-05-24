# CSMA/CA

## Functioning of [CSMA/CA](CA) -1/5
* First, the sender listen to transmission medium
* The transmission medium needs to be idle for a short period
	* This period is called [[DIFS]] approx 50 micro seconds
* If the transmission medium í idle for the duration ò 1 DIFS, the station can start sending a frame
* If a station receives a frame, which passes the [[CRC]] check, it waits for a short period
	* This period called [[SIFS]] approx 10 micro second
	* Next, the receiver send an [[ACK]]
* [[DIFS]] and [[SIFS]] guarantee for [CSMA/CA](CA) a minimum spacing, when a sequence of frames shall be transmitted
* If another [[DIFS]] with an idle transmission medium has expired, a **backoff time** is calculated
	* The backoff time is calculated by using a random value between the minimum and maximum **contention window** and multiplying this random value with the slot time
		* after the backoff time is ex, the frame is transmitted
* minimum [[CW]] and maximum CW and slot time
	* After the backoff time has expired, the frame is transmitted
* Minimum CW, maximum CW and slot time depend on the modulation method used and are fixed
* The minimum and maximum CW values are always a power of 2 and from the result, value 1 is subtracted
	* If a WLAN uses e.g. the modulation method OFDM
		* At the 1st attempt to transmit the CW is >=15 and <=31
		* at the 2nd attpent to transmit, the CW is >= 31 and <= 
* 
![[Pasted image 20221207123940.png]]
#COMPUTER_NETWORK 
