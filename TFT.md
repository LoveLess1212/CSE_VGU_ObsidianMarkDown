# Champ
## 1 Cost
Best: Yasuo, Ahri, Darius, Garen
Worst: kogmaw, chogath, Reksai
## 2 Cost
Best: Gnar(BT, Claw or double titan BT), Temmo 
## 3 Cost
Best: Yone Bard Amumu Illaoi
## 4 Cost
Best: Galio with stoneplate
Sylas with TG
Mor with morello
Lilia
# Trait
 * Behemoth not that good
  * warden OP as Fuck

# Comp
## Reroll
Sena gnar aaxtrox cait jax reksai

Flex Trait
Sage
Warden OP AF

Dạ, đầu tiên là file BPMN XML sẽ đi từ IPFS tới Dapp, cùng với thông tin của Transaction n-1 từ cloud DB ( dùng cái này để extract output eUTxO). DApp sẽ extract thông tin từ BPMN cũng như từ cái eUTxO, để tạo ra 1 transaction n mới (consume input, to create output).

Transaction đó sẽ được đẩy xuống blockchain, và sẽ được áp dụng nếu validator chạy thành công.

Transaction n (được off chain tạo ra): 
Input: reference của eUTxO được extract ra từ Transaction n-1
Output: proposed eUTxO from off chain component


Làm sao để thể hiện là 

---

Provider --- Actor, ...

Mở rộng Dapp

đổi màu chữ, hoặc đổi style 

chữ transaction để to ra
![[Pasted image 20250903204412.png]]
We conceptually describe a per-task transaction and its eUTxOs in Cardano. **The thick arrow connecting the current choreography task of the derived choreography process to the transaction is more conceptual than literal.** To establish this link, we include the hash values of the previous, current, and next tasks in the input eUTxO. The transaction’s output eUTxO then contains the hash values of a tuple representing three choreography tasks, with the new current task positioned in the middle of this sequence.

In Figure \ref{fig:on-off-chain-eUTXO}, let us investigate the on-chain storage (lower part of the figure) and off-chain storage (upper part of the figure) of the blockchain platform of our choice, Cardano. Note that we adhere to the fundamental principles of the Cardano platform, which prioritize minimizing on-chain storage while maximizing off-chain components.

---
The diagram explain show a proposed architecture to process and stores process info in Cardano. 

- What: Architecture to process off-chain and store BPMN steps ?? on-chain
- How:
	- Store: 
		- On chain: Stores previous, current, next task and hash of BPMN files on transaction output. 
		- Off chain: IPFS, cloud database sync with on chain Tx and analytical data
	- Process: 
		- Info of previous Tx from DB and current task from IPFS -> Tx builder
		- Both parties sign the transaction
		- Validate on Smart contract -> Transaction, input last eUTxO (previous Task), output, new eUTxO (current task)



The immutable transactions and blocks created in the blockchain storage provide a verifiable log for the choreography tasks of a penalty rule. However, <span style='color: red'>on-chain storage</span> is notoriously known for high latency and is inherently designed not to handle an unstructured log. To make the rule execution trail even more auditable, we capture extended data associated with each choreography task, such as 
user interface and multimedia records, and store them in a <span style='color: blue'>cloud database</span>. In circumstances where we need to investigate a specific choreography task of a penalty rule that has already been enacted, we employ a blockchain indexer API (e.g., Blockfrost, Koios) to retrieve its task-level log item from the designated <span style='color:red'>cloud database</span>. 

data bên ngoài


2. At Least One Honest Participant must be present in the channel to contest faulty state transitions. 
3. Always Online: State channels require participants to remain online during the entire lifecycle of the channel to prevent execution forks [10], in which a malicious actor starts the dispute phase and submits stale state to the blockchain, e.g., statei−1. Honest participants must notice such an attempt and submit statei . 1