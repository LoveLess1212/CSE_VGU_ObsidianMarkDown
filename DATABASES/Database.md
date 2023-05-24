* 3 requirements of databases
	* Persistently save
		* The data is independent on run time of program or switch on - off
	* Free of redundancies
		* Redundancy make data inconsistent, affect performance of the database. Because it store a value multiple time. It also cause others problem like waste space in the memory, hard to search ... 
	* Administration function
		* User can perform query on the data, creates new tables or even delete the table.
* Redundancies - consequences:
	* Redundancy is a multiple existence of a single value in data.
	* Redundancy make it hard to find & change the data in the database
		*  Example
			* The data "Frankfurt" is also stored as "FFM" or "Frankfurt am Main"
* Compare two database model:
	* Hierarchic database model
		* no flexibitity when changes on structure of the database
		* memory have to be reserved for pointer
	* Relational database model
		* very flexibility when changes in structure
		* no need to reserve space memory for pointer because there are no pointer
* 3 Level of a database
	* Intern Level
		* Intern level is when we talk about physical memory
	* Extern Level
		* Is the way that the user see the database, the view that the end user have on the database
	* Conceptual Level
		* Is rules - connection between intern and extern level
* Relational requirements of level in database
	* The intern level is not relational, because the intern level is just about how the data, communicate with the operating system, so it not relational, bcs relational provide flexible  & strutured way of store data, that the  computer sytstem don't need
	* The extern level can be relational, but not have to be. It depend on the language - the application that the end user use
	* The conceptual level have to be relational because it form the rule of the database - this database is realtional :V
* Types of database language
	* DML - Data manipulation language:is to manipulate data like insert, select
	* DDL - Data definition language: is to define the database like create a new table.
	* Database language can be found on the external level
* Independence
	* The database must be design in a way that the user or the program can not realize or not affected by the change in the conceptual level or intern level
	* benefit: 
		* Operator: no source code adaptation when changes in the internal level
		* user : no training needed when change in the conceptual level
* Requirements of a DBMS 
	* Data security and data integrity
		* rules compliance
	* DDL
		* creating, changing, deleting tables\ attributes
	* DML
		* searching, inserting, changing, deleting of data set
	* Optimization of manipulation and instructions
		* to implements command optimal
* Characteristic of Relational Database Model
	* Structural Aspect
		* Data must be change - view in form of table
	* Manipulative aspect
		* Data is provided in table, can be manipulated in anyway, but in the end the user get the result in form of table
	* Integrity condition must be fulfilled
* Primary key and characteristic
	* Is a attribute or combination of attribute 
	* has to be unique for every dataset
	* If it is a combination of attribute, it have to be minimal as posisble - (irreducibility)
* Why do you need primary key
	* Clearly identify a data set
	* Manage relationship between tables
* NULL:
	* Advantage: beneficial when adding missing information
	* Dis: should be treated seperately
* Give two differences between relations and tables, discuss consequence
	* Every element can occur once in a relation
	* no NULL values can occur in a relation
	* The order is strictly defined within cross products, not within tables
	* Infinity of relations
	* Sorting options within tables
*  Union-compatible or type compatible 
	* Two relations are union compatible or type compatible if they are all the subset of the same cross product.
	* example: 
		* Student form Frankfurt Uni
* Eight operator
	* Union
	* Intersection
	* Product
	* Difference
	* Restrict
	* Project
	* Join
	* Divide
* Which operation must be type compatible:
	* Union
	* Difference
	* Intersection
	* *Reason: input are two symmetry classes and you receive one new symmetry class as output
* Explain join.
	* Is a product of two table but with restrict
	* Equijoin - equal 
		* Natural join is equi join but auto join column with the same name
	* Thetajoin - ><,>< ..