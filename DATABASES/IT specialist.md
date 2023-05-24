We need a software which 
	- Allow users to access the data basis
	- Permit users to perform operations on data without having prob
	- Administrates the competitive accesses on the data basis
-> **[[DataBases]].Management.System (DBMS)

# DBMS
* The Access on the data basis has to be managed by a monitoring program
* **Reason**
	* Long way between user and physical data
	* **Road information** are **Administrated by** the **monitoring program**

# Problem
* **Persistent** -> **must** stored on **Hard disk**
* **Hard Disk** slower than **Main memory access** -> **impact on performance**
*
  | Manager                  | Task                                      | View on data basis         |
  | ------------------------ | ----------------------------------------- | -------------------------- |
  | DBMS                     | Determines which [[databases]] to read        | collection of [[databases]]    |
  | File Manager             | Determines which sites to read            | collection of sites, block |
  | Read only Memory manager | Knows the physical location of the requested site &  executes the access | actual physical form       |

# Clustering 
* Take care that often req data are stored physically to each other*
* Aim:
	* Improving access speed on the data
* Support 
	* Sequential reading of several datasheets
	* the reading of several datasets from different files
# Storage structure 
	 storagestructure that can improve the access
* Index process
* Hashing
* Pointer Chains
* Compression processes
# Data - DB administration
* ## Data Administration (DA)
	* describe overall management activity
		* decide which data stored
		* aim of data storage
* ## [[Databases]] Administration (DBA)
	* Implement of wanted concepts
	* Selection & installation of DB System
	* Creating [[Databases]]
	* Data design and data structure
	* Administration of interfaces
	* Responsible for availability and backup
	* Decides data structure
* ### Best practice would be:
	* Immunity of the application concerning storage Structure and access technic changes

#[[DATABASES]] 