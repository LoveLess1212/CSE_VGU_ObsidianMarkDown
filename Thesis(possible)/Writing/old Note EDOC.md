
SUBMISSION: 23  
TITLE: Blockchain-Aided Enactment of Choreographed Penalties  
  
  
----------------------- REVIEW 1 ---------------------  
SUBMISSION: 23  
TITLE: Blockchain-Aided Enactment of Choreographed Penalties  
AUTHORS: Lam Son Lê and D.V. Toan Phi  
  
----------- Overall evaluation -----------  
In their paper, the authors propose an approach that ensures that penalty rules are respected in the context of business processes. The paper presents three research questions: RQ1 is about the logical representation and model-based techniques that the authors have to use to represent the penalty rules; in RQ2, the authors question themselves on how they can refine a penalty rule into a conceptual model to enable penalty fulfillment; finally, RQ3 is about the transformation of the conceptual model into smart contract code to run on blockchain.  
With the objective to answer these questions, the authors propose a three-step plan for implementing penalty rules: (i) describe the penalty rule in deontic logic, (ii) transform the deontic logic into a BPMN choreography, and (iii) code the smart contracts that handle the process described in the BPMN.  
(i) Deontic logic is chosen because it is considered the base of process modeling, processes compliance, and its operators are suitable for modeling the contractual modality.  
(ii) BPMN 2.0 standard offers several types of process diagrams. This gives the opportunity to process analysts to model actors’ contractual collaboration.  
(iii) The smart contracts are the coded representation of the BPMN process diagram. In this way, they can perform, among the other actions they can handle, the compensation actions if a penalty rule occurs.  

In my view, the topic is of interest and pertains to a research area in which much work can be conducted. Notably, the paper aims to solve a problem with an impact on academia and business alike.  

The drawbacks of the paper follow.  
  
In Section 3.3, there are three research questions: (RQ1), (RQ2), and (RQ3). While (RQ1) and (RQ2) find an answer in the paper, the (RQ3) is never addressed.  
  
A passage of Section 4.4 reads: "A smart contract is programmed to create a firing block to confirm that a penalty rule has just been kicked off". Do I understand correctly that the authors mean that the smart contract is capable of firing transactions? In what sense does a smart contract fire blocks? Smart contracts cannot send transactions, so there seems to be a major architectural issue here.  
  
*The authors suggest the usage of a private blockchain. I think this choice is because the authors want only certain users to send and read data on-chain. The problem is that even when using a private transaction, all data is public to the users in the network. So, the authors need to encrypt the data; otherwise, anyone within the network can read anything.*  

The authors propose an approach, but no implementation has been reported, no experimental evaluation has been performed, and no data has been collected to support the feasibility of the solution.  

Presentation issues occur too.  
There are several examples throughout the paper. In the abstract, the case of a wrong-booked hotel room, in the introduction, the renting of a car, in the first part of the background, there are two other different examples. When introducing the "failing which" connective, the hotel example reappears. Then, in the Research Statement section, the running example is based on a hotel renting room. The authors should make the presentation consistent and focus on a single running example to increase understandability.  
  
At the end of the first subsection of the background (2.1), a natural deduction occurs, as far as I understand. It is put there without an explanation. Also, it is not mentioned further to explain an important concept in order to better understand the paper. I assume the authors put it there to give an example of a natural deduction made with deontic logic. However, the usefulness of the example in that position is questionable, in my view, especially if not used to explain a notion, concept, or passage. That natural deduction does not improve the understanding of deontic logic, the general idea of the paper, or why the authors decided to use such logic to represent penalty rules.  

*In Section 3.1, the rules are expressed formally. Some definitions are missing: BalconyWithSeaView, KingSizeDoubleBed, CheckIn, etc. The name is self-explanatory, but they must be expressed formally, too. Then, when expressing FreeSpa, I see a problem. The expression says, "There exists a spa that belongs to Service". In this case, "Service" can be any spa, but in the text, the "hotel's Spa" is mentioned.*  

All in all, the idea behind this paper is of interest and could spark interesting discussions and follow-ups. However, the entire architecture must be improved, and the usage of blockchain must be reconsidered. All the weaknesses should be addressed, too, such as the expressions of missing rules.  

  
  
----------------------- REVIEW 2 ---------------------  
SUBMISSION: 23  
TITLE: Blockchain-Aided Enactment of Choreographed Penalties  
AUTHORS: Lam Son Lê and D.V. Toan Phi  
  
----------- Overall evaluation -----------  
The paper proposes to enforce declarative penalty rules from service agreements on the blockchain by first translating the penalty rules to BPMN choreography diagrams and then enforcing them with a hybrid on-and-off-chain approach. Penalty rules are formally specified in the form of deontic logic. A mapping to choreography diagrams is provided, and a blockchain-based implementation is discussed.  
  
In favor:  
  
+ The paper is easy to read  
+ The concepts are provided in a proper level of technical detail.  
+ The topic fits well with the conference  
  
Against:  
- The paper falls short of motivating why the declaratively specified penalty rule should be translated into a choreography diagram. Why can't we execute them on a rule engine (off-chain or on-chain but secured by the blockchain?). One reason would be to reuse existing approaches for their enforcement, such as chor-chain. However, this is not mentioned in the discussion of the future implementation.
  
- The paper refers to blockchains in general but has a very unusual assumption about blockchains: Each choreography task leads to the creation of a new block. Please check how transactions and blocks actually relate or justify why you want your custom blockchain system to behave this way.
  
- As the authors write, penalty rules typically require human intervention. One reason is that the participants first need to agree on the fact of a service violation. The paper proposes to enforce the rules automatically on-chain. However, how the consensus on a violation can be automated in the proposed system remains unclear.  
  
Detailed comments:  

p2: … is made transparent thanks to the immutability of the blockchain. Transparency has nothing to do with immutability.  

p4 : As a matter of style, please do not write a whole paragraph in a footnote.  
Citation for [4]. What is the idea of citing [4] with “… just three steps”. The paper is on flexible execution on the blockchain by executing the actual rules off-chain. However, there are many other approaches with a few steps for model-based execution of processes on the blockchain.  
You need a better motivation for your approach.  

p7: “…BPMN 2.0 has recently adopted …” I would not say an extension from more than 10 years ago can be referred to as recently.  
  
  
  
----------------------- REVIEW 3 ---------------------  
SUBMISSION: 23  
TITLE: Blockchain-Aided Enactment of Choreographed Penalties  
AUTHORS: Lam Son Lê and D.V. Toan Phi  

----------- Overall evaluation -----------  
The topic of this paper is the enforcement of penalties in a contractual service agreement. The authors seek to automate the expected compensation actions that are supposed to be realized when a contract is not fulfilled. A proposal is made to handle such actions via a blockchain based architecture. The approach relies on formal expression of penalty rules and their transformation into BPMN choCeographies. A blockchain is used to store most essential data used and generated by the choreographies. The enactment of the choreographies is realized via Smart Contracts implemented on top of the Blockchain.  
  
Globally, the paper is well written and rather easy to understand and to follow. The provided example is very helpful for understanding the approach. The main issue is related to validity and feasibility of the approach. No implementation or Proof of Concept is mentioned; the approach remains fully conceptual.  
  
  
  
----------------------- REVIEW 4 ---------------------  
SUBMISSION: 23  
TITLE: Blockchain-Aided Enactment of Choreographed Penalties  
AUTHORS: Lam Son Lê and D.V. Toan Phi  
  
----------- Overall evaluation -----------  
The paper presents a theoretical model that, given a penalty rule expressed using deontic operators, suggests these rules can be mapped to BPMN Choreography tasks, with their executions tracked via blockchain for auditability and transparency. The model is illustrated using a hotel room allocation scenario.  
  
The paper fits well within the conference scope.  
  
Sections 1 to 3 are clear and provide sufficient background and motivation to understand the problems the authors aim to solve. However, while the research questions are clear, they lack generality and are overly narrow, focusing too much on the paper's specific contributions rather than flowing naturally from the motivation and background sections. This suggests they were written with the solution already in mind, limiting the paper's scope.  
  
Section 4 is the core of the paper, describing the solution and providing answers to the research questions. However, the answers are not entirely convincing:  
  
    RQ1: "What logical representation and model-based techniques shall we follow?" Response: "Deontic logic is chosen for its simplicity and relevance to business contract modeling." However, no alternatives are considered, leaving it unclear why Deontic logic was chosen over other methods like Normative Systems or Promise Theory.  
  
    RQ2: "How can we refine a logically represented penalty rule into a language-agnostic conceptual model to enable penalty fulfillment?" The authors suggest a classification of deontic clauses and the corresponding modeling structures for process choreography. This response is illustrative but lacks demonstration.  
  
    RQ3: How can we transform their model-based procedural contracts into smart contracts to programmatically trigger compensation in favor of their customers?  
        Response: This question is not directly answered and is left for future work. Including this as a research question without addressing it in the paper may not be advisable.  
  
The blockchain aspect is the least convincing part:  
  
    The paper mentions that certain logs must be stored off the chain but does not explain why.  
    The processing of data seems block-centric rather than transaction-centric. The explanation of how a smart contract creates a block is unclear: "A smart contract is programmed to create a firing block to confirm that a penalty rule has just been kicked off." The blockchain semantics need clarification.  
    The authors claim their process includes "human-in-the-loop" but do not provide details on managing stakeholder access rights, access to secret/private data, or how the audit should be performed.  
  
No implementation is provided, which limits the ability to learn practical lessons from this work. An implementation would have helped in understanding the relationship between the theoretical model and practical application.