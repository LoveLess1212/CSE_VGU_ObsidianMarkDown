Authentication and authenticity:
- Unambiguous identification of the sender of information or a communication peer
## Factors for Authentication
- What you know
	- Password
	- Other example: Personal Identification Number (PIN), Bank Account Number, Credential Address, Date of Birth, etc.
- What you have
	- Token
	- Other example: Banking card,  Smart card, Credit card
- What you are
	- Biometry 
## Password Security
Depends on:
- Size of password domain, choice of password and password policies
- Security of storing passwords (users and systems)
- Security when entering/transmitting passwords
### Size of Password Domain
![[Pasted image 20230620073211.png]]
Length and number of characters matter
### Challenge-Response using Password
![[Pasted image 20230620111251.png]]
### Authentication by Symmetric Key
![[Pasted image 20230620111343.png]]
### Authentication by Public Key Cryptography
![[Pasted image 20230620111427.png]]
## Digital Signature
- Aims:
	- Authenticity 
	- Integrity
	- Nonrepudation
- Mostly realized by public key cryptography
	- Sender signs message with private key
	- Public key is used for validation
- Important practical improvement:
	- Only a "fingerprint" of the message is digitally signed, not complete message
#IT_SECURITY 