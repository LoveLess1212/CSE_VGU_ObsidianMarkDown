---
tags:
  - BLOCKCHAIN
---
- [[Marlowe]] is designed to support the execution of financial contracts on [[Blockchain]], and specifically to work on Cardano. Contracts are built by putting together a small number of contracts that can be combined to describe many different kinds of financial contract.
# Contracts
* Contracts in [[Marlowe]] run on a [[Blockchain]] , but need to interact with the off-chain world. The *[[parties]]* to the contract, whom we also call the *[[parties|participants]]*, can engage in various actions: They can be asked to deposit money, or to make a choice between various alternatives. 
* *Notification* is another form of input that is used to tell the contract that a certain condition has been met, anybody can do this, and it tis only necessary because once a contract becomes [[dormant]], it cannot "wake up" on its own, it can only respond to input

* running a contract may also produce external effect, by making payments to [[parties]] in the contract.
# [[parties|participants]], [[Role|roles]], and [[public key]]
* We should separate the notions of [[parties|participant]], [[Role]], and public keys in [[Marlowe]] contract. A 
* represented by tokens and they are distributed to addresses at the time a contract is deployed to the [[Blockchain]]. After that, whoever has the token representing a [[Role]] is able to carry out the actions assigned to that [[Role]], and receive the payments that are issued to that [[Role]]
* This allows roles in running contracts to be traded between [[parties|participants]], through a mechanism of [[tokenization]]. This will be available in the on-chain implementation of [[Marlowe]] but the simulation in the Marlowe Playground simply presents contracts [[Role|roles]].
* [[public key]] [[parties]], are represented by the has of public key (or eventually an addresses). Using [[public key]] to represent parties is simpler because it doesn't require handling tokens, but they cannot be traded, because once you know the private key for a given public key you cannot prove you have forgotten it.
# Accounts
* The Marlowe model allows for a contract to stored assets. All [[parties]] that participate in the contract implicitly own an account with their name. All assets stored in the contract mus be in the account of one of the parties; this way, when the contract is closed, all assets that remain in the contract belong to someone, and so can be refunded to their respective owners. These accounts are local: they only exist for the duration of the execution of the contract, and during that time they are only accessible from within the contract.
# Steps and states
* Marlowe contracts describe a series of steps, typically by describing the first step, together with another (sub-) contract that describes what to do next. For example, the contract ```Pay a p t v cont ``` says "make a payment of value $v$ of token $t$ from the account `a`, and then follow the contract `cont`". We  call `cont` the continuation of the contract.
* In executing a contract, we need to keep track of the current contract (that is, the remaining part of the contract): after making a step in the example above, the current contract is the continuation, `cont`.  We also have to keep track of some other information, such as how much is held in each account: we call this info the state: this potentially changes at each step too. A step can also see an action taking pace, such as money being deposited, or an effect begin produced, e.g. a payment.
# [[Blockchain]]
* While [[Marlowe]] is designed to work with blockchains in general, some details of how it interacts with the blockchain are relevant when describing the semantics and implementation of [[Marlowe]].
* A [[UTXO]]-based [[Blockchain]] is a chain of blocks, each of which contains a collection of transactions. Each transactions has a set of inputs and outputs, and the blockchain is built by linking unspent transaction outputs ([[UTXO]]) to the inputs of a new transactions. At most one block can be generated in each slot, which are one second long.
* The mechanisms by which these blocks are generated, and by whom, are not relevant here, but contracts will be expressed in terms of POSIX time.
# [[UTXO]], wallets and contracts
* Value on the blockchain resides in the UTXO, which are protected cryptographically by a private key held by the owner. These keys can be used to redeem the output, and so to use them as inputs to new transactions, which can be seen as spending the value in the inputs. Users  typically keep track of their private keys, and the values attached to them, in a cryptographically-secure wallet.
* Alternatively, UTXOs can be protected by a script, and that is essentially what a contract is, a script that protects and [[UTXO]], can it can propagate itself throughout a chain of transactions.
* To interact with a contract running on the [[Blockchain]], users will need to use the Marlowe REST API or the Marlowe CLI. This, in turn, will interact with users wallets to authenticate transactions that spend crypto-assets, since deposits are made from users wallets, and payments received by them.
* Note, however, that these are definitely off-chain actions that need to be initiated by code running off chain, typically this will be with the Marlowe REST API or Marlowe CLI: They cannot be made to happen by the contract running on chain itself.
# [[Omniscient simulation]]
The Marlowe Playground supports contract simulation. This is an omniscient simulation, in which the user is able to perform any action for any role, and thus can observe the execution from the perspective of all the users simultaneously. This contrasts with the experience of running a contract using a client, in which each participant sees the contract from their own point of view. In particular, participants are only able to interact with a running contract that is waiting for input from them; if that's not the case, then they will see that the contract execution is waiting for input from another participant.
# Values and tokens
* In previous examples, whenever a `Value` was required, we have exclusively used ada. This makes a lot of sense, as Ada is the fundamental currency supported by Cardano.
* Marlowe offers a more general concept of value, though, supporting custom, native tokens, which can be fungible, non-fungible, or indeed mixed. What is a value in Marlowe?
``` marlowe
newtype Value = Value
	{getValue :: Map CurrencySymbol (Map TokenName Integer)}
```
* The types `CurrencySymbol` And `TokenName` are both simple wrappers around ByteString.
* This notion of value encompasses Ada, fungible tokens (think currencies), non-fungible tokens or NFTs (custom tokens that are not interchangeable with other tokens), and more exotic mixed cases:
	* Ada has the empty `bytestring` as `CurrencySymbol` and `TokenName`.
	* A fungible token is represented by a `CurrencySymbol` for which there is exactly one `TokenName` which can have an arbitrary non-negative integer quantity (of which Ada is special case).
	* A class on non-fungible tokens is a `CurrencySymbol` with several `TokenName`s, each of which has a quantity of one. Each of these names corresponds to one unique of non-fungible token.
	* Mixed tokens are those with several `TokenName`s and quantities greater than one
* Cardano provides a simple way to introduce a new currency by minting it and using minting policy scripts. This effectively embeds Ethereum ERC-20/ERC-721 standards as primitive values in Cardano. In Marlowe we use custom tokens to represent the participants in each contract executing on chain.
# Executing a Marlowe contract
Executing a Marlowe contract on Cardano blockchain means constraining user-generated transactions according to the contract's logic. If, at a particular point of execution, a contract expects a deposit of 100 Ada from Alice, only such a transaction will succeed anything else will be rejected

A transaction contains an ordered list on inputs or actions. The Marlowe interpreter is executed during transaction validation. First, it evaluates the contract step by step until it cannot be changed, any further without processing any input, a condition that is called [[quiescent]]. At this stage we progress through any `When` with timeouts that have passed, and all `If`,`Let`,`Pay`, and `Close` constructs without consuming any inputs

The first input is then processed, and then the contract is single stepped again until [[quiescent|quiescence]], and this process is repeated until all the inputs are processed. At each step the current contact and the state will change, some input may be processed, and payments made.

Such transaction, as shown in the diagram below, is added to the blockchain. What we do next is to describe in detal what Marlowe contracts look like, and how they are evaluated step by step.
We have shown, that the behaviour of a Marlowe is independent of how inputs are collected into transactions, and so when we simulate the action of a contract we don't need to group inputs into transaction explicitly. For concreteness, we can think of each transaction having at most one input. While the semantics of a contract is independent of how inputs are grouped into transactions, the costs of execution may be lower if multiple inputs can be grouped into a singe transactions.

In omniscient simulation available in the Marlowe playground we can safely abstract ây from transaction grouping, since the grouping does not affect the contract's behaviour.