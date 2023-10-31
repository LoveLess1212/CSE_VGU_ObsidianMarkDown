---
tags:
  - CES
---

# Foundation
*  [[Software Architecture Style]] AKA architecture pattern
* Several fundamental pattern appear again and again throughout the history of software architecture because they provide a useful perspective on organizing code, deployments, or other aspects of architecture.
## Monolithic Architecture 
* [[Layered Architecture]]
* [[Pipeline architecture ]]
* [[Microkernels architecture]]
## Distributed Architecture 
* Service-based architecture
* Event-driven architecture
* Space-based architecture
* Services-oriented architecture
* Microservices architecture
### Considerations
* The network is not reliable
* Latency is not zero
* Bandwidth is not infinite
* The network is not secure
* The network topology can change at any time
* There is more than one administrator
* Remote access costs money
* The network is not homogeneous
* Distributed logging
	* Dozens to hundreds of different logs, different place and all with a different format
* Distributed transactions
	* Distributed architectures rely on what is called eventual consistency to ensure the data processed by separate deployment units is at some unspecified point in time all synchronized into a consistent state
* Contract maintenance and versioning
	* Even more complex are the communication models needed for version deprecation
	* 
