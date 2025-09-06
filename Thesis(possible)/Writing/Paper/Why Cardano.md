* https://www.researchgate.net/publication/358290823_Blockchain_scalability_for_smart_contract_systems_using_eUTXO_model - reason why to choose eUTxO(Cardano) instead of original UTXO(Bitcoin) or account-based(Ethereum) by considering blockchain trilema
* https://www.researchgate.net/publication/343486401_The_Extended_UTXO_Model - This paper talk about the rationale why eUTXO is created. Combine the simplicity and security of UTXO model of Bitcoin with the expressiveness of Account-model of Ethereum
Those paper claim  
* eUTXO provides an optimal balance by combining:
	1. The scalability benefits of UTXO
	2. Smart contract capabilities similar to account-based systems
	3. Maintaining simpler state management
	4. Supporting parallel processing
---
sample
The permissionless mode of public blockchains (e.g. Ethereum) is at the expense of privacy, performance, and scalability. A private blockchain eliminates this problem by running as a permissioned blockchain with flexible, extensible consensus and access control techniques. As such, public blockchain networks are not suitable for launching the decentralized program for a business solution [160]. Businesses  
can collaborate with distributed ledger developers to launch their business-to-business and cross-industry applications using a private blockchain. In line with this approach, we chose Hyperledger Fabric for its modular architecture,  
which facilitates future scalability. Most notably, the latter versions of Hyperledger Fabric come with Byzantine Fault Tolerance consensus mechanism to ensure system integrity by mitigating the influence of malicious nodes and ensuring continued operation despite failures or malicious actions.

---
1. Why not choosing the other - ethereum - account-based model
2. what is the benefit of our approach
	1. An eUTxO model eliminates this problem providing a ...
3. comeback to the first reason why
4. how real life approach
5. come to the name and more reason why to pick cardano
6. recent update
--- 
Public blockchains built on the account-based model, such as Ethereum, face fundamental challenges in transaction ordering and state management when handling concurrent operations, leading to scalability limitations and unpredictable execution costs [Citation 1]. The eUTxO model addresses these challenges by providing a deterministic approach to transaction validation and state management, while maintaining the smart contract expressiveness needed for penalty rule enforcement [Citation 2]. This approach is particularly valuable for implementing choreographed penalty workflows, as it allows for precise tracking of transaction dependencies and state transitions. In line with these requirements, we chose Cardano's eUTxO model for its ability to support complex business logic while maintaining high throughput and predictable transaction costs. Furthermore, the recent introduction of Hydra Head technology as a layer-2 scaling solution enhances the network's capacity to handle intensive business process choreography while maintaining the security guarantees of the main chain.

---
I'm still struggle on that part, I've already search through weber's paper and some related but I can't found any kind of similar diagram that could support me to do that. They are all barebone diagram, such as ERD or similar.


làm sao thể hiện liên kết giữa log ở off chain db với data ở trên Tx.
- log on off chain data <-> Tx data
	- Tx hash
vẽ input output 

The smart contract on the system consist of 2 parts: On chain component and off chain component.

The off-chain component responsible for gathering the information of the interaction between user - wallets and the system, to construct the transactions for the on chain component to process. The process could could be simplified to gathering information - translate it to Blockchain-readable format (CBOR) - construct transaction - acquire signatures - send to on-chain component.

The on-chain component responsible for validate 

1 cái hình tờ giấy gấp nếp