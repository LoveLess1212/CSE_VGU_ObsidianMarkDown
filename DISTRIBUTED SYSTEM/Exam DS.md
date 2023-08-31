Open book cover all lecture
Structure:
1.  Multiple choice
2. True/False
3. Short Ans - 3 5 sentences - dont explain too much
5. Essay - explain in tab, show solution
# Sample test
* 1.s part
	*  the openness challenge determines:
		* 
	* key distinction between SOAP and REST
		* A REST send and receives documents while soap uses remote procedures
		* REST must use JSON to encode its data
		* REST is architecture independent
		* Operations are encoded in the document with SOAP but in the URL in REST
	* Which system or app is there mostly with P2P model
		* Google search engine
		* BitTorrent ..
		* Webservice
		* Domain Name system
	* Which implement over TCP:
		* FTP ..
		* DHCP
		* DNS
		* VOIP
	* Which is false
		* In grid Computing all machines on the network work under the same protocol and act like a virtual supercomputer
		* Infrastructure as a service PAAS and Saas ARE SERVICE MODELS IN COULD COMPUTING
		* spark is es useful for parallel processing of distributed data with iterative algorithm
		* Getrerogeneous Distributed Databases are all the databases sites which use identical DBMS and operating system while homogeneous Distributed Databases are diff databases sites that have ..
		
* 2. 
	* TCP implements reliable communication on UDP, which is unreliable
	* Sockets are not needed for UDP bcs UDP is stateless
	* MQTT is a lightweight messaging protocol
	* Map reduce is a parallel programming ..
	* SOAP REST :))) different
	* CORBA is a middleware solution enabling the exchange of information, independent of hardware platforms programming language and operating system
	* TPM, RPC,MOM,ORB are not basic types of [[Middleware]] 
	* Docker is a set of platforms that is useful for running applications in an isolated environment
	* Elasticsearch employs inverted indexes for its search operation
	* The goals of hybrid system exclude scalability, failure tolerance and ro
* 3.
	* Explain 3 challenges with which a DS has to deal
	* Draw one possible three-tiered client server architecture and explain the placement of component in the 3 tiered architecture 
	* A P2P architecture is always more efficient than a centralized architecture. ? agree?? justify your ans
	* Some could computing services like AWS and Azure provide their end users with Virtual machine rather than allocated physical machine. Doing so bings at least three benefits to the provicers. Explain what these 3 benefits are. ?
* 4. Complete ans
	* Given a [[multicast]] program as below. Fill in the blank 
```java
//Mọi người tự coi lại bài UDP rồi bỏ parameter ra nha :') khum thi hồi t làm xong để t chuyueenr qua cho

```
* Nyan wants to find the max sales of a very long list of sales numbers . The input numbers are split up into a set of 581987 files of stored in HDFS. Each file stores many numbers with one number per line. The output should be a single number (i.e the maximum number)
	* Design a map-reduce paradigm to find the maximum. Explain what your map and Reduce function do
		* Hint draw your map reduce model. What do MAP and REDUCE function do. What are their input and output
		* With your des, how many times does MR Nyan call your REDUCE function
		* Assume that each mapper will process one data split. Run your map reduce paradigm with the sample data, which has been partitioned into 3 slits below
		* 1: 8 8 21
		* 2: 13 4 59
		* 3: 3 11