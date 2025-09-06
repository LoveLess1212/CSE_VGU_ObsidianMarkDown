## Background

before coming to the technical implementation of the approach itself, let's review a few key concepts that are important to understand the approach and all the technologies involved on the approach.

First, lets talk about UTxO model, this is the model that Bitcoin used to manage the balance of the users. In this model, the balance of the user is represented by a set of unspent transaction outputs (UTxOs). Each UTxO has an amount of coins and a reference to the transaction that created it. It work like a cash system, where you have a set of coins and you can spend them by giving them to someone else. When you spend a coin, you need to spend the whole coin, and you will receive a new coin as change. This model is very simple and efficient, but it has some limitations, like the lack of support for smart contracts.

you could see it at the example here:
I want to buy a bag on a store that cost 10 coin, and I have a coin of 50. I will give the store the coin of 50, and the store will give me a coin of 40 as change and the bag. In the end, I have a coin of 40 with the bag and the store has a coin of 10. you might see the change in the example is quite abnormal, it is because the store doesn't have to pay the change in the transaction, the blockchain will automatically split the coin of 50 into 2 coins of 40 and 10.

---

## eUTxO model

The eUTxO model is an extension of the UTxO model that adds support for smart contracts. In this model, the output have one more field, the datum. They also support a piece of parameter called redeemer. The datum is a piece of data that is associated with the output and can be used by the smart contract to validateI the transaction. The smart contract is a piece of code that is executed when the transaction is validated, and it can read the datum of the output and use it to decide if the transaction is valid or not. this model solve the limitation of the UTxO model, and allow the blockchain to support smart contracts.
