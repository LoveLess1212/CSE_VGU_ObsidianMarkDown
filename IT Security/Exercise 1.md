1. **Define the term "IT-Security"**
* IT-Security is the protection of information and information systems from unauthorized access and modification and availability of information system services for legitimate users, including measures to thwart, discover or log threats. Protection against unauthorized access must be ensured during storage, processing or in transit
2. **What are the aims of "IT-Security"?**
* Confidentiality: Only authorized persons can access information
* Integrity: Information is not changed by unauthorized persons
* Availability: Information is available to authorized persons
* Authenticity and authentication: Unambiguous identification of the sender and recipient of information
* Non-repudiation: The sender of information cannot deny having sent it
* Authorization: Access to resources is limited to certain group of (authenticated) users
3. **What are passive and active attacks and why is the distinction between them helpful in practice?**
* Passive attacks: 
    * Attacker does not actively interfere with the communication between two parties
    * Difficult to detect
    * Preventive means of protection against active attacks
    
* Active attacks: 
    * Attacker actively interferes with the communication between two parties
    * Manipulation of data or systems
    * Attacker often leaves traces
    * Prevention and detection possible
* The distinction is helpful in practice because it helps to determine the appropriate countermeasures for the respective attack.
4.  Quiz
>[!quiz]
A company uses a firewall for which a new vulnerability was just discovered. The company could immediately fix the vulnarability by employing an external consultant for EUR 19.000,–. In a month, a patch fixing the vulnerability will be available at no cost from the firewall vendor. The IT department estimates that the cost of an attack exploiting the vulnerability is EUR 200.000,–. The probability of a successful attack within the next month is p.
Calculate the cost for both alternatives as a function of p and advise which alternative to choose if the cost is to be minimized.
* There are two options:
    * Option 1: Fix the vulnerability immediately
    * Option 2: Wait for the patch
* The cost of option 1 is 19.000€
* The cost of option 2 is 200.000€ * p
	* The probability for option 2 to be cheaper than option 1 is  $p < 0.095$
* **Conclusion**
    * If the probability of an attack is less than 9.5%, it is cheaper to wait for the patch (option 2)
    * If the probability of an attack is greater than 9.5%, it is cheaper to fix the vulnerability immediately (option 1)
