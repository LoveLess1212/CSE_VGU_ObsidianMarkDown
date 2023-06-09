> [!def]
> Unambiguous(exact) identification of the sender of information or a communication peer

## Factors for Authentication
* What you know 
	* Password
* What you have 
	* Token
* What you are
	* Biometry
## Password Security
* Depends on 
	* Size of password domain, choice of password and password policies
	* Security of storing passwords (user and systems)
	* Security when entering/transmitting passwords
### Size of Password Domain
* ![[Pasted image 20230620001032.png]]
* Length and number of characters matter
## Digital Signature
* Aims:
	* Authenticity
	* Integrity
	* Nonrepudiation
* Mostly realized by public key [[IT Security/Cryptography|Cryptography]]:
	* Sender signs message with private key
	* Public key is used for validation
* Important practical improvement:
	* Only a "fingerprint" of the message is digitally signed, not complete message 7kp['']
## Cryptographic Hash Functions
- Compute characteristic patter ("fingerprint ") of fixed length for each message
- Mostly 128 or 256 bits
- It should be impossible
	- To find a message yielding a given hash value
	- Tod find two messages with the same hash value
- Widely used algorithms: MD5 and SHA
#IT_SECURITY 
