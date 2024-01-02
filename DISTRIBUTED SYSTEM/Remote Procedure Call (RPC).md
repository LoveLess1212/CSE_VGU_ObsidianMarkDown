---
tags:
  - DISTRIBUTED_SYSTEM
---

- Remote Procedure Call (RPC) is a software communication [[protocol]] that one program can use to request a service from a program located in another computer on a network without having understand the network's details.
- E.g: Java RMI, SOAP, CORBA
- [[RPC uses the client-server model]] 
- RPC is a synchronous operation
    - The requesting program to be suspended until the results of the remote procedure are returned.
- RPC makes distributed computing look like centralized computing

![[RPC - img.png]]