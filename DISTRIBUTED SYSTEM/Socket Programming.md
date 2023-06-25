# Machine to machine
- One machine **communicates** with one another, we need to know
	- The **location** of machine
		- E.g., 138.37.94.248:8080 or vgu.vn:8080
	- The communication **protocol**
		- E.g., TCP/IP or UDP
# Process to process
- Process A communicates with Process B
	- A **sends** a message to the destination
	- B **receives** the message
- Message passing
	- Send operation
	- Receive operation
- A queue is employed at the destination
# Sockets
- A **socket** is one endpoint of a **two-way communication link** between two programs running on the network.
- A socket is **bound** to a **port** number so that the TCP layer can identify the application to which data is destined to be sent.
![[Pasted image 20230625171726.png]]
- Socket primitives
![[Pasted image 20230625171828.png]]
- The server listens to the socket
- The client knows: hostname and port number of the server
- The client requests connection to the server
- The server accepts and get a new socket bound to a port
![[Pasted image 20230625172030.png]]
# Java IDE Tools
- Netbeans
	- https://netbeans.apache.org/download/index.html
- Eclipse
	- https://www.eclipse.org/downloads/
- Or any of your choice
# Socket Programming with Java
## Aims
- Getting to know the **basic programming** with Java.
- Getting to know how to **get network information**.
- Getting to know how to create a **connection** between a **server** and a **client**.
## Overview
- A **process** is a program running in a computer.
- Processes in different machines communicate with one socket by **socket**.
- A **socket** is one endpoint of a **two-way communication** link between two programs running on the network. A socket is **bound** to a **port number** so that TCP layer can identify the application that data is destined to be sent to.
- Two applications playing the part of **Client** and **Server**
- Two types of socket: **Server socket** and **Client socket**
- Communication by socket
	- Server application is running, and Server socket is listening
	- Client application tries to connect to the Server via the Server socket
	- Server accepts the connection 
	- Communication takes place between the two machines
	- The connection is closed
- The **java.net package** in the Java platform provides a **class**, **Socket**, that implements one side of a two-way connection between your Java program and another program on the network. By using the **java.net.Socket class** instead of relying on native code, your Java programs can communicate over the network in a platform-independent fashion.
- Additionally, java.net includes the **ServerSocket class**, which implements a socket that servers can use to listen for and accept connections to clients.
- There are two types of IP traffic: **TCP** (Transmission Control Protocol) and **UDP** (Universal Datagram Protocol). TCP is a connection-oriented protocol while UDP is a connectionless protocol.
## Preliminaries
### Java exception
- An exception is an **event** that occurs **during the execution** of a program that disrupts the normal flow of instructions.
	- E.g., NumberFormatException, ArrayIndexOutOfBoundsException, FileNotFoundException, IOException
- How to use: two ways
![[Pasted image 20230626003258.png]]
