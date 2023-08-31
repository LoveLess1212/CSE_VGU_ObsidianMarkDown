* Concerned with:
	* How a software system should be organized and designing the overall structure of that system 
* The critical link between design and requirements engineering
	* As it identifies the main structural components in a system and the relationships between them.
* Agile?
	* An early stage: Design an overall systems architecture
	* Refactoring the system architecture is usually expensive
# Architectural Abstraction
* Architecture in the small
	* Is concerned with the architecture of individual programs
* Architecture in the large
	* Is concerned with the architecture of complex enterprise systems that include other systems, programs, and program components.
> Software architecture is important because it affects the performance, robustness, distribute-ability, and maintain-ability of a system
> 	Non f. req: individual components
> 	Non-func. reqs: depend on the system architecture
# Advantage of Explicit Architecture
* Stakeholder communication
	* Architecture maybe used as a focus of discussion by system stakeholders.
* System analysis
	* Means that analysis of whether the system can meet its non-func requirements is possible
* Large-scale reuse
	* The architecture may be reusable across a range of systems
	* Product-line architectures may be developed
# Architectural Representations
* Mostly use: Simple, informal block diagrams showing entities and relationships
	* Problem: lack semantics
* Box and line diagrams:
	* Very abstract - do not show the nature of component relationships nor the externally visible properties of the sub-systems.
	* However, useful for communication with stakeholders and for project planning
# Use of Architectural Models
* As a way of facilitating discussion about the system design
	* A high-level architectural view is useful for communication with system stakeholders and project planning
* As a way of documenting an architecture that has been designed
	* To produce a complete system model that shows the different components in a system, their interfaces and their connections.
# Architecture Decomposition
* Software systems:
	* complexity problem <= inter-relationship
* Goals:
	* Maximizing [[cohesion]]
	* Minimizing [[coupling]]
#SOFTWARE_ENGINEERING 