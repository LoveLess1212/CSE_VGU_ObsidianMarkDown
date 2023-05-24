> a *database* is a collection of data, which are saved in  a data basis. A DB also has a DBMS that handles all user requests to the database.

> A Database system is an application with a unique DBMS, which allows the user to implement the different [[databases]]. The data basis of this [[databases]] are all administrated with the native DBMS

## Three levels of DB
### Internal level: (Physical storage)
	is not relational - stirage takes place in the same way as all other databases models
* It exists only one 'single' intern level - in contrast to the external level
* Only take care of the physical storage of data, which was defined in the conceptual level
* Aim:
	* save datasets persistent and to find them as fast as possible
> 	if there are done any changes on the internal level and the user do not notice anything and the software is not affected, the DBMS guarantees **Physical indep 

* This kind of data independences are very important and are expected by the user
* Also improtant for the developer, otherwise there have to be quiet a lot of adaptions due to every change
### External level: (diff view that end user has on the data)
	Can, but do not have to be relational
* Level of the individual user
* Every user comm with the system in diff lang (e.g. operators with Java)
* A part of such lang is the data language
* The *data language* work on processes which have to do with data and operations
	* aka *embedded data lang
	* controls all actions to the database
* A *data language* 2 part
	* Data Definition Language **(DDL)**
		Definition of database objects to administrate and structure the database
	* Data Manipulation Language **(DML)**
		actual access on the data
### Conceptual level: (administrates the connection between intern and extern level)
	is strictly relational
* is fundamental set of rules and structure of a database
	* defines tables,
	* describes the possible relations between the entities
* All extern levels have to go through this level
	* several extern level, only one conceptual level
> if there are done any changes on the conceptual level and the user do not notice anything and the software is not affected, the DBMS guarantees **Logical data independent

## DBA 2.0
* #### Detailed description of the tasks:
* Design of the conceptual level
		* Conceptual schema
		* Logical database design
* Design of the intern level
	* Internal schema
	* Physical database design
* User support
	* create update of [[databases]]
## DBMS 2.0
* The DBMS is software systems, via the whole communication in between all three levels takes place
* Decisive for the quality of a software
* It characterizes the design and functionalities for each users
* Has to support at least the following fields:
	* Data definition (DDL)
	* Data manipulation (DML)
* **Optimization of manipulation instructions
	* Queries should be results- oriented
	* Results show exactly update or search requestions
	* Several solution are available and the DBMS can find the optimal solution
	* **Data security and data integrity**
> **Definition***(general)
> A transaction is an activity which is completed within itself in a system 

> **Definition** *(context with [[databases]])*
> Before and after a transaction the database system has to be consistent

#DATABASES 
