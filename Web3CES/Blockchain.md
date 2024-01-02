---
tags:
  - CES
---
* A type of distributed ledger that organizes data in blocks, and updates the entries using an append-only structure
* Cryptocurrencies, such as bitcoin, pioneered blockchain tech
* While [[Marlowe]] is designed to work with blockchains in general, some details of how it interacts with the blockchain are relevant when describing the semantics and implementation of [[Marlowe]].
* A [[UTXO]]-based [[Blockchain]] is a chain of blocks, each of which contains a collection of transactions. Each transactions has a set of inputs and outputs, and the blockchain is built by linking unspent transaction outputs ([[UTXO]]) to the inputs of a new transactions. At most one block can be generated in each slot, which are one second long.
* The mechanisms by which these blocks are generated, and by whom, are not relevant here, but contracts will be expressed in terms of POSIX time.