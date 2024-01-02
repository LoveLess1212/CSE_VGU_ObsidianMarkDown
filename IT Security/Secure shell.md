---
tags:
  - IT_SECURITY
aliases:
  - SSH
---
* The SSH [[protocol]] (also referred to as Secure Shell) is a method for secure remote login from one computer to another
* The [[protocol]] works in the client-sever model, which means that the connection is established by the [[Secure shell]] client connecting to the SSH server.
* The SSH client drives the connection setup [[process]] and uses public key [[cryptography]] to verify the identity of the SSH server. After the setup phase the SSH protocols uses strong symmetric encryption and hashing algorithm to ensure the privacy and integrity of the data that is exchanged between the client and server
# SSH command forwarding
```bash
ssh -L local_port:remote_host:remote_port -g user@ssh_server

this is the command for local port forwarding
- ssh: secure shell
- -L: local port forwarding
- local_port: the port on the local machine that will be forwarded
- remote_host: the host on the remote machine that the data will be forwarded
- remote_port: the port on the remote machine that the data will be forwarded
- -g: allow other host connect to 
- user: the user that will be used to connect to the remote host
- ssh_server: the ssh server that will be used to connect to the remote host

example: ssh -L 8888:10.2.4.37:80 -g 10.2.4.99
connect to machine with ip 10.2.4.99 and forward connection from port 8888 on my machine to port 80 on 10.2.4.37 machine, also allow other user to connect to the forwarded port

```

