---
aliases:
  - TLS
  - SSL
  - Transport Layer Security
  - Secure Sockets Layer
tags:
  - IT_SECURITY
---
* A cryptographic protocols designed to provide communication security over a computer network
* Structure:
	* Lay between application layer and [[Transport Layer]] 
	* Consist of 2 smaller layer in [[TLS SSL|TLS]]/[[TLS SSL|SSL]] [[protocol]]:
		* First 3 [[protocol]] for negotiate of the encrypted connection, 4th one for transferring something
		* [[TLS SSL]] record [[protocol]]: transferring record which are encrypted symmetrical cryptographical mechanism and using digital signature for ensuring integrity of respective record. Then this [[protocol]] will be then used by other specified [[protocol]] for transmission
* How TLS/SSL used: handshake [[protocol]]
* a TLS handshake is [[process]] that kick off a communication session that uses [[TLS SSL|TLS]]. During a TLS handshake, the two communication sides exchange messages to acknowledge each other, verify each other, establish the cryptographic algorithms they will use, and agree on session keys.