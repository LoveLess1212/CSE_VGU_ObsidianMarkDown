# Basic priority inheritance [[protocol]]
- **Aim:** to **adjust the scheduling priorities** of jobs during resource access, to reduce the duration of timing anomalies
- **Constraints:** 
    - Works with any pre-emptive, [[Priority-driven]] [[scheduling algorithm]] 
    - Does not require any prior knowledge of the jobs' resource requirements
    - **Does not prevent deadlock**, but if some other mechanism used to prevent deadlock, ensures that no job can block definitely due to uncontrolled priority inversion
- We discuss the basic priority-inheritance [[protocol]] which **assumes there is only 1 unit of resource**
- **Assumptions** (for all of the following protocols):
    - Each resource has only 1 unit
    - The priority assigned to a job according to a standard scheduling algorithm is its **assigned priority**
    - At any time *t*, each ready job $J_{k}$ is scheduled and executes as its **current priority**, $\pi_{k}(t)$, which may differ from its assigned priority and may vary with time
- The current priority $\pi_{l}(t)$ of a job $J_{l}$ **may be raised** to the higher priority $\pi_{h}(t)$ of another job $J_{h}$
- In such a situation, the lower-priority job $J_{l}$ is said to **inherit the priority** of the higher-priority job $J_{h'}$ and $J_{l}$ executes at its inherited priority $\pi_{h}(t)$ 

## Rule of Basic priority inheritance [[protocol]]
### 1. Scheduling Rule:
- Ready jobs are scheduled on the processor preemptively in a priority-driven manner according to their current priorities
- At its release time *t*, the current priority $\pi(t)$ of every job J is equal to its assigned priority
- The job remains at this priority except under the condition stated in rule 3
### 2. Allocation Rule:
When a job J requests a resource R at time *t*,
- if R is **free**, R is **allocated** to J until J releases the resource, and
- if R is **not free**, the request is denied and J is **blocked**.
### 3. Priority-Inheritance Rule:
- When the requesting job J becomes blocked, the job $J_{l}$ which blocks J **inherits** the **current priority** $\pi(t)$ of J
- The job $J_{l}$ executes at its inherited priority $\pi(t)$ until it releases R; at that time, the priority of $J_{l}$ return its priority $\pi_{l}(t)$ at the time t when its acquires the resource R

## Properties of the Priority-inheritance [[Protocol]]
- Simple to implement, does not require prior knowledge of resource requirements
- Jobs exhibit different types of blocking
    - Direct blocking due to resource locks
    - Priority-inheritance blocking
    - Transitive blocking
- Deadlock  is not prevented
    - Although it can be prevented by using additional protocols in parallel
- Can reduce blocking time compared to non-preemptable [[Critical Sections]], but does not guarantee to minimize blocking

#REAL-TIME_SYSTEM 