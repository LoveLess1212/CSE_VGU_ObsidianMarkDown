---
tags:
  - BLOCKCHAIN
---
Unspent transaction output

* Value on the blockchain resides in the UTXO, which are protected cryptographically by a private key held by the owner. These keys can be used to redeem the output, and so to use them as inputs to new transactions, which can be seen as spending the value in the inputs. Users  typically keep track of their private keys, and the values attached to them, in a cryptographically-secure wallet.
* Alternatively, UTXOs can be protected by a script, and that is essentially what a contract is, a script that protects and [[UTXO]], can it can propagate itself throughout a chain of transactions.
* To interact with a contract running on the [[Blockchain]], users will need to use the Marlowe REST API or the Marlowe CLI. This, in turn, will interact with users wallets to authenticate transactions that spend crypto-assets, since deposits are made from users wallets, and payments received by them.
* Note, however, that these are definitely off-chain actions that need to be initiated by code running off chain, typically this will be with the Marlowe REST API or Marlowe CLI: They cannot be made to happen by the contract running on chain itself.