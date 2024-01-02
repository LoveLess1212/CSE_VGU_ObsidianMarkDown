---
tags:
  - IT_SECURITY
aliases:
  - CA
---
* A security certificate is a small data file used to confirm the [[Authentication]], identity, and reliability of a website or web application.
* Certificate Authority([[CA]]): Take the certificate request which consist of info of the entity (user,web server, ..) along with it's public key, and then it check that this public key is truly belong to that entity. Then [[CA]] will sign this certificate with it's private key(compute the hash, then encrypt the hash with private key)
	* Information about and public key a user digitally signed by a Certificate Authority
* **Root CA**: CA sign its own certificate
* If you don't know the user of the certificate => go look at the certificate authority that signed that certificate
* **Certificate revocation** certificate that is no longer valid because that have been withdrawn
	* Certificate revocation is *the act of invalidating a [[TLS SSL|TLS]]/[[TLS SSL|SSL]] before its scheduled expiration date*. A certificate should be revoked immediately when its private key shows signs of begin compromised. It should also be revoked when the domain for which it was issued is no longer operational.
	* To check the revocation status of an [[TLS SSL|SSL]] [[Certificate]], The client connects to the URLs and downloads the CA's CRLs. Then, the client searches through the CRL for the serial number of the certificate to make sure that it hasn't been revoked.
* [[OCSP]]: When a user requests the validity of a certificate, an [[OCSP]] request is sent to an [[OCSP]] Responder. This checks the specific certificate with a trusted certificate authority and an [[OCSP]] response is sent back with a response of either 'good', 'revoked', or 'unknown'
* [[CSR]]: is a specially formatted encrypted message sent from [[TLS SSL|SSL]] digital [[certificate]] applicant to a [[Certificate|CA]]. The CSR validates the information the [[Certificate|CA]] requires to issue a [[certificate]]
# Advantage and disadvantage
* Advantage: 
	* [[Certificate]] is public, so anyone can have
	* Enhanced academic performance
	* Improved reputation
* Disadvantage
	* Trustworthy only given if the root CA and other CA involved in the Process are trustworthy 
	* CA is compromised and still issuing certificate which might not belong to valid institution
	* Revocation is problematic because sometime this is not checked.
* If you want to access some website -> access proxy -> get to the [[Certificate]] and then be forwarded to the actual website
* alternative for [[Certificate]] : [[Pretty Good Privacy]] 