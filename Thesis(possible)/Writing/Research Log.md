
* Fig. 2 => needs to be reviewed given your new programming experience in Aiken

* Fig. 5 & Fig .6 : could they be listed as (a) and (b) of the same figure instead of two consecutive ones?

* I am a bit concerned about the smart contract as an object in your sequence diagram, especially in the registration phase. I reckon the list of providers and consumers is handled off-chain. Do we need to describe the big picture of rule registration and execution?

On the solution, there are 2 things to identify Provider and Consumer that are stored on-chain, which is the (public key hash) of them. ( with the BENCH-32 standard of Cardano, so I don't think they need more encrypting) ( We could always trace back the wallet address from the public key hash )
About the other data that stored on the blockchain 
- current state of the task (incoming,outgoing,current) - they are all hashed 
- The price - unhashed
- BPMNXML -> Hashed
-

```
{
	Price - Int (remain untouched)
	workflow
	{
		Current -> Hashed
		Incoming -> list<hashed>
		Outgoing -> list<hashed>
	}
	bpmnxml -> Hashed
}
```
---
implementation 

validator, call hàm này, rồi trong hàm đấy làm gì
pseudocode for implementation, theo hàm



The demos is realized by using new cutting edge Technology for Cardano writing in Aiken for On-chain validator and MeshJs for Off-chain transaction builder. 
The Validator contain three action(redeemer) based on specific stages(write 3 stages when the bottom part of smart contract) of the process that could be (called ??) when firing the transaction.  The ... is presented in the listing ... 

```
validator bpmnRuleEnactment {

  spend(
    _datum: Option<BpmnEscrowDatum>,
    redeemer: EscrowBpmnActions,
    self: Transaction,
    utxo: OutputReference,
  ) {
    when redeemer is {
      Start -> {
      // the input eUTxO contain actor (provider) public credential, BPMN XML hashed, and the current state is of the first task
      }
      Task(next_task) ->{
      // next_task is a feasible next task using outgoing from previous task
      // the datum of the new eUTxO is updated correctly with the state now is the state of next_task
      // both parties signed(agree on) this transaction 
      }
	  
      Cancel -> {
      //  the transaction contain the signature of either actors
      }
      Finalize ->{
      // the current state is of the last task
      // both parties signed this transaction
	  }
  }
}
```


The smart contract is then successful applied to Cardano pre-production network. Which resembles a mainnet environment used explicit for testing before deploying the app.

hash that task ID - with the bpmn xml ?

how to ensure that, no one could be able to submit an invalid task?

not in outgoing ? what if provider try to create a new Utxo that contain an invalid outgoing ?