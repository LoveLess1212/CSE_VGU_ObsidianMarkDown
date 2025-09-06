---
tags:
  - BLOCKCHAIN
  - Thesis
aliases: []
---
* Is very different from ether - it take some time more useful

> *extended* Unspent [[Cardano Transaction|transaction]] output

# Ethereum-style smart contracts
* When a [[Cardano Transaction|transaction]] occurs on an account [[blockchain]], the balance of the sender's account is directly decremented and that of the recipient is incremented, similar to how conventional bank accounts work.
* Contracts interact with these balances and run via the EVM (Ethereum Virtual Machine). The EVM can be thought of as a global on chain computer on which smart contracts take turns running, before their results are added to the chain.
# The eUTxO model
* In the eUTxO model [[tokens]] are stored in UTxOs. A [[UTxO]] is like (electronic)-cash where each individual bundle of bills (Ada and native-[[tokens]]) is stored separately
* A [[Cardano Transaction|transaction]] in the [[UTxO]] model takes one or more UTxOs as *[[Cardano Transaction|transaction]] inputs*, which are destroyed, and creates one or more UTxOs as *[[Cardano Transaction|transaction]] outputs*
* Transactions in an *account-based model*(Ether) mutate the data-points storing the total balances. This is very risky. In the [[UTxO]] model only the "bills" that participate in a given [[Cardano Transaction|transaction]] can potentially be affected.
* 
