> [!def]
> Unambiguous(exact) identification of the sender of information or a communication peer

* In physical world 
	- Passport - contain biometrical info, govern info, photo of your face that is similar with the one who you claimed to be with the authorization
	- Signing a document 
* In principle very similar to the cyber world
## Factors for Authentication
* What you know 
	* Password
		* is a shared secret that only the auth system and user known
	* Personal Identification number (PIN)
	* 
* What you have 
	* Token
		* Some devices that show you a six digit number by LCD, that number changing every ... minutes, the number on the LCD can be calculated using cryptographic.
	* Smart card
	* Credit card ...
		* You need these thing to do authentication, that exist only one of this.
* What you are
	* Biometry
	* Physical property of a person
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
