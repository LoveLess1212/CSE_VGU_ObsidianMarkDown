* Exercise 1: **outline the presented model of a cryptographic system**
    * **Cryptographic system** is a system that uses cryptographic algorithms to provide security services.
* Exercise 2: **Explain the differences between public key and symmetric encryption schemes. Also, explicate the respective advantages and disadvantages.**
    * **Symmetric encryption** uses the same key for encryption and decryption. It is faster than asymmetric encryption, but the key has to be shared between the sender and the receiver.
    * **Asymmetric encryption** uses different keys for encryption and decryption. It is slower than symmetric encryption, but the key does not have to be shared between the sender and the receiver.
* Exercise 3: **Define ther term "hybrid encryption scheme" and outline the sequence thereof**
    * **Hybrid encryption scheme** is a combination of symmetric and asymmetric encryption. The sender encrypts the message with a symmetric key and encrypts the symmetric key with the public key of the receiver. The receiver decrypts the symmetric key with his private key and decrypts the message with the symmetric key.
* Exercise 4: **Explain the term "mode of operation" and outline encryption and decryption for at least two different modes**
    * **Mode of operation** is a technique that allows to encrypt a message of arbitrary length with a block cipher. It is used to avoid repetition in the ciphertext.
    * **Electronic Codebook (ECB)**: The message is divided into blocks of the same size. Each block is encrypted separately. The same plaintext block always results in the same ciphertext block.
    * **Cipher Block Chaining (CBC)**: The message is divided into blocks of the same size. Each block is XORed with the previous ciphertext block before encryption. The first block is XORed with an initialization vector (IV). The same plaintext block does not always result in the same ciphertext block.
* Exercise 5: **Explain what conditions must be met for conducting a brute force attack**
    * **Brute force attack** is an attack that tries all possible keys until the correct key is found.
    * The key space must be small enough to be searched in a reasonable time.
    * The key space must be known.

* exercise 6: **What percentage of all possible binary keys with key length 128 bits can be tried in 1.000.000 years if 10.000.000 keys can be tested per second**
    * 10.000.000 keys per second -> 10.000.000/(2^128) = 10.000.000/3.4028237e+38 = 2.9387358770557188e-29 correct key per second -> 2.9387358770557188e-29 * 60 * 60 * 24 * 365 * 1.000.000 = 9.274663e-13 correct keys per year -> 9.274663e-13 * 100 = 9.274663e-11% correct keys per year -> need 1/9.274663e-11 = 1.078e+10 years to try all keys -> 1.078e+10/1.000.000 = 1.078e+4 million years to try all keys
* exercise 7: **Explain how One Time Pads operate and explain why a message encrypted by this method cannot be recovered without knowing the used encryption key**
    * **One Time Pad** is a symmetric encryption scheme that uses a key that is as long as the message. The key is only used once and must be shared between the sender and the receiver. The key is XORed with the message to encrypt it and XORed with the ciphertext to decrypt it. The key is random and cannot be guessed.
    * Without knowing the key, all possible messages are equally likely
* exercise 8: **Explain how Electronic Code Book(ECB) operates and explain advantages and disadvantages of this method. Also, explain under which circumstances ECB can be used and when not.**
    * **Electronic Code Book (ECB)**: The message is divided into blocks of the same size. Each block is encrypted separately. The same plaintext block always results in the same ciphertext block.
    * Advantages:
        * Parallelization
        * Error propagation is limited to one block
    * Disadvantages:
        * Same plaintext block always results in the same ciphertext block
        * No integrity protection
    * ECB can be used when:
        * The message is divided into blocks of the same size
        * The same plaintext block always results in the same ciphertext block
        * No integrity protection is needed
    * ECB cannot be used when:
        * The message is not divided into blocks of the same size
        * The same plaintext block does not always result in the same ciphertext block
        * Integrity protection is needed
* Exercise 9:

    * Ciphertext -> plain text
        * 0000 -> 0111
        * 0001 -> 1011
        * 0010 -> 1001
        * 0011 -> 0011
        * 0100 -> 0110
        * 0101 -> 1100
        * 0110 -> 1110
        * 0111 -> 1111
        * 1000 -> 0100
        * 1001 -> 1000
        * 1010 -> 0010
        * 1011 -> 0101
        * 1100 -> 0001
        * 1101 -> 1010
        * 1110 -> 0000
    * find encryption for 0010 1111 1001 0100 1100 -> 1010 0111 0010 1000 
    * Find decryption for 1101 0101 0110 0001 0110 -> 1010 1100 1110 1011 1110  
    * for CBC, IV 1101 find encryption for 0010 1111 1001 0100 1100
        * 0010 XOR 1101 = 1111 -> 0111
        * 1111 XOR 0111 = 1000 -> 1001
        * 1001 XOR 1001 = 0000 -> 1110
        * 0100 XOR 1110 = 1010 -> 1101
        * 1100 XOR 1101 = 0001 -> 0001
        * we have the encryption 0111 1001 1110 1101 0001
    * for CBC, IV 1101 find decryption for 1101 0101 0110 0001 0110
        * 1101 -> 1010 XOR 1011 -> 0001
        * 0101 -> 1100 XOR 0001 -> 1101
        * 0110 -> 1110 XOR 1101 -> 0011
        * 0001 -> 1011 XOR 0011 -> 1000
        * 0110 -> 1110 XOR 1000 -> 0110
        * we have the decryption 0001 1101 0011 1000 0110
    * For output feedback mode with n=1 what would be the encryption for 0010 1111 1001 0100 1100 with IV 1101 ?
        * 