---
tags:
  - Thesis
  - CES
  - BLOCKCHAIN
aliases:
  - transaction
---
> Is  the main data holder of the [[blockchain]]
# Output
* is an **object** describes atleast 2 things:
	* a quantity of assets -- aka value
	* a condition for spending - specify in [[Validator]] 
	* a data payload - [[Datum]] - not compulsory Main storing mechanism 
* Cardano support two kinds of assets:
	* the main [[protocol]] currency (Ada) 
	* user-defined currencies. 
	* *Both live side-by-side in values though slightly different rules apply to each.*
* The address captures the logic that tells the [[protocol]] under what conditions one can utilize the assets at a particular output. It is what defines ownership of the assets. 
# Input
* is a reference to a previous output.
* input's serial number is the hash digest of the transaction that emitted the output it refers to and the position of the output within that transaction. These two elements make each input unique. And because outputs are removed from the available set (the post it note is destroyed) when spent, they can only be spent once. This is ensured by the [[blockchain]] [[protocol]].

The use of [[Blockchain]] in leveraging 