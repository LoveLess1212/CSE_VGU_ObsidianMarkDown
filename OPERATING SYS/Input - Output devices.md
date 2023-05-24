
# Character devices & Block devices
	devices  for cpt sys are distinguised via their min transfer unit:
## Character Devices
* On arrival/req of each signle character, communication with the CPT always take place
* Ex: mouse keyboard, printer ..
## Block devices
* data transfer takes place only when an entire block is present
* Ex: HDD, [[SSD]], [[CD]] ...
# Busy Waiting
* The driver sends the req to the dev and waits in an infinite loop until the controller indicates that the data is availablle
	* if the data is available it is written into the memory and the execution of the [[process]] continues
* Benefit:
	* no additional hardware required
* Drawback:
* causes CPU workload
* Slows down simultaneous execution of multiple processes
	* reason: the CPU muse check periodically whether the data is availabel
# interrupt- driven
* Precondition: An interrupt controller and a line of the control bus 
* The driver initializes the I/o operation and waits for 
	* an interrupt and the operation system can assign the CPU to other processes
* If an interrupt occurs, the driven
# Direct Memory Access
* Need: DMA controller
	* can transfer data directly between main mem and the I/o devices
	* triggers an interrupt after the data is transferred
	* Benefits:
		* reading data causes no CPU workload
		* simultaneous execution of multiple processes is not slowed down
	* Drawbacks:
	* additional hardware is required
# Computer Data Storage
* Stores the data and the executables
* Different computer storage is connected via different bus systems -> **Memory hierarchy**
* **Reason** for existence the **memory hierarchy:** price performance ratio -> the better the performance of a computer data storage is, the higher is the acquisition cost and the smaller is the capacity
## Digital Data Storage
* *Random access* means that the medium does not need to be searched sequentially from the beginning - such as with magnetic tapes to locate a specific record.
	* the heads of magnetic disks or a laser can jump to every point of the medium within a known maximum period
* *movable part* always shitty :V "Chris. Baun"
## Mechanical Data Storage
* Each punch card usually represents a single line of text with 80 characters or a corresponding number of binay data
* The punched tape in the image has 8 holes for data and narrower holes to feed the tape
	* 1 bytes per row can be stored
* Data is represented on CDs/ DVDs by pits and lands, which are applied to a plastic material
## Magnetic Data Storage
* Data is stored on a magnetizable material
* Via read and write heads, the magnetization of the material is detected and modified
* Read and write heads may be movable or fixed
*  *Rotating data storage:
	* hard disk drive, floppy disk, Drum memory
* *Non_rotating data storage:
	* Mag core memory
## Magneto-optical Data Storage
* Rotating storage medium
* Write operation are carried out magnetically
* Before the magnetization can be modified the medium must be heated until the Curie point is reached
	* *advance*: intensive to magnetic fiels
	* The heating takes place via laser beam
* Read operations are carried out optically
	* Differently magnetized areas reflect light differently
## Electric Data Storage
* Static Random-Access Memory
	* Information is stored as a change of state of flip-flop circuits
	* iinformation can be stored as long as the operating voltage is available
	* Faster and more expensive than Dram
	* Used for **[[cache]]** and CPU-internal **registers
* Dynamic Random-Access Memory
	* information is stored in capacitors
	* Req periodic refresing of the information
## Memory hierarchy
* Primary storage and secondary storage are permanently connected to the commputer
	* Advantage: Stored data can be accessed Quickly
* Primary storage: The CPU has direct access to this storage
* Sec storage: Storage, which is accessed via a controller
* Tertiary storage: Not permanently connected to the computer. Main purpose is archiving
	* Near-line storage: Is automatically and without human intervention connected to the system.
	* Off-line storage:media are stored in cabinets or storage rooms and must be connected manually to the system
## Functioning of the Memory Hierarchy
* when a record is accessed for the first time, a copy is created and this copy travels along the memory hierarchy to the top layer
* If the record is modified, the modification must be passed down at some point in time
	* During write back, the copies of the record must be updated at all layers in order to avoid inconsistence
	* Modification
## [[Cache]] Write Policies
* Write through: Modifications are immediately propagated to lower storage layers 
	* Advantage: consistency is ensured
	* Drawback: Lower performance
* Write back: Modifications are propagated when the correspondgin page is removed from the [[cache]]
	* Ad: Better performance
	* Drawb: Mod get lost in case of a system failure
#OPERATING_SYSTEM 