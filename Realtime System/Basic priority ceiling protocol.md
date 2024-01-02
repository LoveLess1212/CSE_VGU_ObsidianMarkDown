- The priority-ceiling [[protocol]] **extends the priority-inheritance** [[protocol]] to **prevent deadlock** and to further reduce the blocking time
- **Key assumptions:**
    - The **assigned priorities** of all jobs are **fixed** (e.g. RM scheduling, not EDF)
    - The resources required by all jobs are **known a priori**
- Need two additional terms to define the [[protocol]]:
    - The **priority ceiling of any resource** $R_{k}$ is the highest priority of **all the jobs** that require $R_{k}$ and is denoted by $\Pi(R_{k})$ 
    - At any time $t$, the **current priority ceiling**  $\Pi(t)$ of the system is equal to the **highest priority ceiling of the resources** that are **in use** at the time
    - If all resources are free, $\Pi(R_{k})$ is equal to $\Omega$, a nonexistent priority level that is lower than the lowest priority level of all jobs
- If resource access in a system of preemptable, fixed priority jobs on one processor is controlled by the priority-ceiling [[protocol]]:
    - **Deadlock can never occur**
    - A job can be blocked for at most the duration of one critical section
        - There is no transitive blocking under the priority-ceiling [[protocol]]
- Differences between the priority-inheritance and priority-ceiling protocols:
    - **Priority inheritance is greedy**, while priority ceiling is not
        - The priority ceiling [[protocol]] may withhold access to a free resource, causing a job to be blocked by a lower-priority job which does not hold the requested resource-termed avoidance blocking
    - The priority ceiling [[protocol]] forces a fixed order onto resource accesses, thus eliminating deadlock
## Rule of [[Basic priority ceiling protocol]] 
### 1. Scheduling rule:
- At its release time t, the **current priority** $\pi(t)$ of every job J is equal to its assigned priority. The job remains at this priority except under the condition stated in rule 3.
- Every ready job J is scheduled preemptively and in a priority-driven manner as its current priority $\pi(t)$.
### 2. Allocation rule:
Whenever a job J requests a resource R at time t, one of the following two conditions occurs:
- R is held by another job. J's request **fails** and J becomes **blocked**
- R is free
    - If J's priority $\pi(t)$ is **higher than** the current priority ceiling, R is allocated to J
    - If J's priority $\pi(t)$ is not higher than the ceiling $\Pi(t)$ of the system, R is allocated to J only if J is the job holding the resource(s) whose priority ceiling is equal to $\Pi(t)$; otherwise, J's request is denied, and J becomes blocked
    - Unlike priority inheritance: **can deny access to an available resource**
### 3. Priority-inheritance rule:
- When the **requesting** job, J, becomes **blocked**, the job $J_{l}$ which blocks J **inherits** the current priority $\pi(t)$ of J
- $J_{l}$ executes at its inherited priority **until the time when it releases every resource** whose priority ceiling is equal to or higher than $\pi(t)$; at that time, the priority of $J_{l}$ returns to its priority $\pi_{l}(t')$ at the time t' when it was granted the resource(s)
## Enhancing the priority ceiling [[protocol]]
- The basis priority ceiling [[protocol]] gives good performance, but the defining rules are complex
- Also, can result in high context switch overheads due to frequent blocking if many jobs contend for resources
![[Pasted image 20230618015221.png]]
- This has led to two modifications to the [[protocol]]:
        - The stack-based priority ceiling [[protocol]]
        - The ceiling priority [[protocol]]

#REAL-TIME_SYSTEM 