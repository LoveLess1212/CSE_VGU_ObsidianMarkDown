* Sub-systems must exchange data. This may be done in two ways:
	* Shared date is held in a central database or repository and may be accessed by all sub-systems:
	* Each sub-system maintains its own database and passes data explicitly to other sub-systems.
* When large amounts of data are to be shared, the repository model of sharing is mostly commonly used bcs this is an efficient data sharing mechanism
# Description
* All data in a system is managed in a central repository that is  accessible to all system components. Components do not interact directly, only through the repository.
# Example
* The next is an example of an IDE where the components use aa repository of system design information. Each software tool generates information which is then available for use by other tools.
* ![[Pasted image 20230823153656.png]]
# When used
* You should use this patter when you have a system in which large volumes of information are generated that has to be stored for a long time. You may also use it in data-driven systems where the inclusion of data in the repository triggers an action or tool.
# Advantages
* Components can be independent- they do not need to know of the existence of other components. Changes made by one component can be propagated to all components. All data can be managed consistently as it is all in one place.
# Disadvantages
* The repository is a single point of failure so problems in the repository affect the whole system. May be inefficiencies in organizing all communication through the repository. Distributing the [[Repository]] across several computers may be difficult.
* 
#SOFTWARE_ENGINEERING 