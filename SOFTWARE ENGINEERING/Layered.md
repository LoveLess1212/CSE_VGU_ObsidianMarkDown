
# Description
* Organizes the system into layers with related functionality associated with each layer. A layer provides services to the layer above it so the lowest-level layers represent core services that are likely to be used throughout the system
# Example
* A Layered model of a system for sharing copyright documents held in different libraries
* ![[Pasted image 20230823105924.png]]
# When used
* When building new facilities on top of existing systems; when the development is spread across several teams with each team responsibility for a layer of functionality; when there is a requirement for multi-level security
# Advantages
* Allow replacement of entire layers so long as the interface is maintained. Redundant facilities can be provided in each layer to increase the dependability of the system
# Disadvantages
* In practice, providing a clean separation between layers is often difficult and a high-level layer may have to interact directly with lower-level layers rather than through the layer immediately below it.
* Performance can be a problem because of multiple levels of interpretation of a service request as it is processed at each layer.

#SOFTWARE_ENGINEERING 