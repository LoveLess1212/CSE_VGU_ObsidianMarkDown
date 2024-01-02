---
tags:
  - IT_SECURITY
---
# POP-Auth
* When you fetch a email, you will tell the server your username, the user keyword and the server will reply with the ok. Then you will send out the password phrase(secret) then the server will reply with another ok again, then you are logged in
# Email
* Sender first contact the sender's  by a protocol called [[SMTP]], then the sender's mail send to recipient's mail server also using [[SMTP]] protocol, and the mail will be stored in this server. When the recipient want to read the email, the recipient will contact that mail server to get the mail by a protocol called POP & IMAP
# App layer encryption
* Before send out the email, convert it to ciphertext and then proceed the normal email sending procedure. When the email is arrived at the final destination at the other end, the email will then be decrypted
# [[Secure shell]]

# [[TLS SSL]]
# Dynamic content
* Content that constantly or regularly changes based on user interactions, timing and other parameters that determine what content is delivered to the user (like Facebook)
# S/MIME
* A standard for public key encryption and signing of MIME(MIME is an internet standard that extends the format of email messages to support text in character sets other than ASCII, as well as attachments of audio, video images, and application programs. Message bodies may consist of multiple parts, and header information may be specified in non-ASCII character sets. Email messages with MIME formatting are typically transmitted with standard protocols such as the [[SMTP]] [[POP]] and the [[IMAP]])
* S/MIME provides the following cryptographic security services for electronic messaging applications:
	* [[Authentication]] 
	* Message Integrity
	* Non-repudiation of origin (using digital signatures)
	* Privacy
	* Data security (using encryption)
# [[Pretty Good Privacy]]