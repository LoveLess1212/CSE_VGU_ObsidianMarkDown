> An Web3 that using Cardano along with hydra to enact choreographed [[Process]]
# Use case
* User could choose which service ( represented by text & BPMN) -> active it ( or could known as using a service in real life) 
* Everyone ( both user and provider ) could track the status of the BPMN while there are activating service
* Provider could upload service for user to choose
* See the result of previous services
* See the list of Provider and their services - percent of each services.
# Who will use
* Users (who use the service of the provider)
* providers
# What will be stored on the [[blockchain]]
## [[Cardano Transaction|Transaction]]
* The result of every service (compensated, not compensated ...)
* developed time
* [[parties|participants]]
# Smart contracts
* Calculating provider reputation
* Executing compensation action ?
* Triggering a process choreography - execute it 
# Question
* How should a provider upload the services as BPMN? - chorjs

# Expanding
## Voting
* Service Matching bw the text and BPMN: To ensure the correctness between the services BPMN and the text version of the service, could developed one more [[blockchain]] for user to vote if that service is legit
* Vote the Provider ??

# What have been done before
* The method to map the BPMNs into smart-contracts of the [[blockchain]] ( bpm [[blockchain]]  - event driven ...)
	* When the bpmn is imported, create a [[smart contract]] for that [[blockchain]] and create [[smart contract]] for each data object ? each [[task]]?
	* 
* 
What should be included in the BPMN in order to map into [[smart contract]] ?

# Frontend
## Pages
### Landing pages
* overview, [[wallet]] connect
### Company pages
* upload  a BPMN and mint it like an NFT :))) ??? 
* 
### User Pages
* show list of companies - list of services - where should we store the services ? (store it like NFT maybe?) and show their reputation, will be calculate by a smartcontract.
* when user choose a service, they have to sign a [[Cardano Transaction|transaction]] to say that they have started a contract. and pay a fee for the creator, also the provider of the services. then it will be locked until the provider follow every step of the BPMN. 
	* How does the [[blockchain]] know if provider or user follow that business process or not ? ( there must be some countable asset - bill or proof setted on the [[blockchain]])
	* upon the finish of the bpmn, another [[Cardano Transaction|transaction]] will be signed by user ? automatically created to release fund for provider ( could make an option for the service to fund before or after)
	* *should reserach more about this*

