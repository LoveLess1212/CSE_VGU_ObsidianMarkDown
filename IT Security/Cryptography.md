## Intro
* [[DISTRIBUTED SYSTEM/Cryptography|Cryptography]] is the study of mathematical techniques related to aspects of information security such as confidentiality, data integrity, entity authentication, and data origin authentication 
## Classical Encryption Methods
* Substitution
	* e.g., mono-alphabetical substitution 
* Transposition
	
 * e.g., put message by columns in a matrix and read out by rows
* Product cipher
	* Combination of substitution and transposition 
* Applying multiple substitution and/or transpositions possible
## What should remain secret
* Method and key
* Method public, only key private
* Good reasons for making method public 
* Kerckhoffs' principle: Security should not depend on the secrecy of the method
* Our focus on public methods only
## A Word of Caution
* [[DISTRIBUTED SYSTEM/Cryptography|Cryptography]], i.e. the encryption methods themselves, is a tool that helps to secure networks and systems
* The protocols, applications and environments using cryptography might have conceptual weaknesses, implementation bugs or other caveats that could allow to compromise the protection, e.g.,
	* By evading the cryptographic system
	* by breaking the cryptographic system
* Using a strong cryptosystem does not guarantee security
* Using a weak cryptosystem compromises security
## Encryption methods 
* Substitution Cipher
	* Substitute symbol or group of symbols by other symbols, order is preserved
* Transposition Cipher
	* Retain symbols but change order
* Product Cipher
	* Combination of the above
## Security of Encryption Schemes
* Cryptanalysis
* Brute-Force-Attack
* Statistical properties of cipher text
* In general:
	* Ciphertext-Only-Attack
	* Known-Plaintext-Attack
	* Chosen-Plaintext-Attack
* Brute-Force-Attack: If there are finitely many keys, try them out until one fits
* 
#IT_SECURITY 