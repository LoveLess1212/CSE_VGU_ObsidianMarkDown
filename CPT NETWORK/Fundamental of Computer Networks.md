
## Required Components
	- >= 2 terminal dev with network service running
	- Transmission medium
	- network protocols
Communication between computer are possible via parallel and serial

## Parallel Data transmission
	- in addition to the control lines, multiple data lines exist
	- Benefit: Higher throuhgput
	- Drawback: Lot of lines are necessary
	- Usage: local bus system

## Serial Data transmission
	- bits are transmitted one after another via the bus
	- Benefit: can be used for long range distance, few line require
	- Drawback: lesser throughput
	- Usage: local bus system and computer networks

# Directional Dependence of Data Transmission
## Simplex
	- one direction
	- after a transmission, The comm channel can be used by another sender 
## Duplex
	- both direction
## Half-duplex
	- both direction but not simultaneously

>[!Topologies of Computer Network]
	- Determines how the communication partners are connected with each other
	- Affects its reliability A LOT

* The Structure of large scale networks is often a combination of different topologies
* Physical and logical [[topology]] may differ
	* **Physical [[topology]]:** describes the wiring
	* **Logical [[topology]]:** Describes the flow of data between the terminal devices
* Topologies are graphically represented with nodes and edges
| Name                 | Description                                                                                    | Advantage                                                     | Drawback                                                                           |
| -------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [[Bus Network]]      | All terminal devices are connected via a shared cable - the bus                                | Cheap to implement                                            | Shared cable files -> Network fails / Only single node can send data at each point |
| [[Ring Network]]     | connects node to node, all data is transferred from nodes to nodes until reach the destination | Large-sized rings(transmission medium dependent) are possible | Disruption of a single link -> network fail                                        |
| [[Star Network]]     | All nodes are connected directly with a central component (HUB or Switch)                      | Expandability and stability                                   | Failure of the central component leads to a failure of the network itself          |
| [[Mesh Network]]     | Each node is connected with one or more other nodes                                            | Failure safe (depends on the cabling effort)                  | Cabling effort and energy consumption                                              |
| [[Tree Network]]     | see in pages :')'                                                                              | see in pages :')'                                             | see in pages :')'                                                                  |
| [[Cellular Network]] | Implemented by wireless networks                                                               | Failure of nodes do not affect the network itself             | Maximum dimension is limited by the number of base station and their positions     |


> [!Current situation:]
> **Bus** and **Ring** are seldom use
> **Ethernet** with **Switches** using **Star [[topology]]**
> ***Connecting Hubs and switches*** using **Tree [[topology]]**
> **Standard wireless network** using **Cellular [[topology]]**
> **Mesh [[topology]]** is one possible use case of wireless netoworks and it is the l**ogical [[topology]] between routers**
> 

## [[Data Signal]]






#COMPUTER_NETWORK