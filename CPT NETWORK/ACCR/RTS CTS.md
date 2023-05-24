> Request to send ([[RTS]]) and Clear to Send ([[CTS]])
* [CSMA/CA](CA) reduces the number of collisions
	* but it cannot avoid all collisions
* A **better collision avoidance** implements [CSMA/CA](CA) [[RTS]]/[[CTS]]
	* concept: Sender and receiver exchanged control frames list
		* This way, all stations in the network learn that a transmission will start soon
	* Control frames: [[RTS]] and [[CTS]]
		* both control frames contain a field, which indicates how long the transmission medium will be occupied
* Collisions can only occur during the transmission of [[RTS]] and [[CTS]] frames because of the [[hidden terminal problem]]
## Function
* After [[DIFS]], the sender transmits a [[RTS]] frame to the receiver
	* The [[RTS]] frame contains a field, which specifies the period, the sender wants  to reserve the transmission medium (channel) to transmit the frame
* The receiver [[ACK]] the reservation request by waiting the [[SIFS]] and the transmitting a [[CTS]] frame which also contains the period of time, the sender wants to reserve the transmission medium (channel)
	* The receiver confirms this way the period which is required to transmit the data frame
* After the receiver succ received the data frame, it waits for the period of a [[SIFS]] and transmits and [[ACK]] frame to the sender
* if the transmission medium is occupied, no further station tries to trasmit a frame, until the end of the [[NAV]]
* Ad:
	* **Fewer collisions** bcs solves the problem of hidden terminals
	* **Less energy consumptions** bcs to transmission attempts during [[NAV]]
* Drawback
	* **delay
	* **[[overhead]]**
## in Practice
* Optional for WLAN but mostly implemented
	* it is used for reserving channels for the transmission of large payload changes
* For each station,, a RTS threshold value can be specified
	* This way it can be defined that RTS/CTS is used only when a frame is bigger than the threshold number
* Other the default threshold value is higher than the maximum frame length for IEEE 802.11
	* Then, the RTS/CTS Sequence can be left out for all transmitted payload frames
* #COMPUTER_NETWORK 