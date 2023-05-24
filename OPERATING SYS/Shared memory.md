* Paradigm for cooperating processes, producer process produces information that is consumer [[process]]
	* *unbounded-buffer:* places no practical limit on the size of the buffer.
		* The consumer may have to wait for new items but the producer can always produce new items.
	* **Bounded-buffer** assumes that there is a fixed buffer size.
		* The consumer must wait if the buffer is empty and the producer must wait if the buffer is full.
#OPERATING_SYSTEM 