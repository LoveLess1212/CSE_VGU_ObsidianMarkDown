## Fundamentals 
- Additional resources, along with processors, required for jobs to be executed
    - So far, we ignores resources for scheduling processors
- Resources may represent:
    - **Hardware devices** such as sensors and actuators
    - **Disk** or **memory** capacity, buffer space
    - **Software resource:** mutexes, [[locks]], queues, etc.
- This chapter discusses:
    - How resource contention affects the execution behavior and schedulability of jobs
    - How various resource access-control protocols work to reduce the undesirable effect of resource contention
    - How well these protocols succeed in achieving this goal
## Definitions and notations
- Assume a system with $\rho$ types of resource named $R_{1}$, $R_{2}$, ..., $R_{\rho}$ 
    - Each resource $R_{i}$ comprises $v_{i}$ indistinguishable units
        - Resources with a (practically) **infinite number** of units have no effect on scheduling; and so are **ignored**
    - Each unit of resource is used in a **non-preemptable** and **mutually exclusive manner**; resources are serially reusable
        - E.g., when a unit of resource $R_{i}$ is granted to a job, this unit is no longer available to other jobs until the job frees the unit
    - If a resource *can be used by more than one job at a time*, we model that resource **as having many units**, each used mutually exclusively

## [[locks]]
## [[Critical Sections]] 
- The segment of a job that **begins at a lock** and **ends at a matching unlock** is a **[[Critical Sections]]** 
    - Use the expression $[R, n;e]$ to represent a [[Critical Sections]]  regarding $n$ units of $R$, with the critical section requiring e units of execution time
    - [[Critical Sections]] may nest if a job needs multiple simultaneous resources
    ![[Pasted image 20230617171428.png]]
## Conflict and blocking
- Two jobs **conflict** with one another if some of the **resources** they require are of **the same type**
    - They contend for a resource if one job requests a resource that the other job has already been granted
- When the scheduler **does not grant** $n_{k}$ units of resource $R_{k}$ to the job requesting them, the lock request $L(R_{k}, n_{k})$ of the job **fails** (or is denied)
    - The job is blocked and loses the processor
    - The job is unblocked when the scheduler grants it $n_{k}$ units of resource $R_{k}$
## [[Resource access control protocols]]
- A [[Resource access control protocols]], or simply an access-control protocol, is **a set of rules** that govern:
    - when and under what conditions each **request for resource is granted** and
    - how jobs requiring resources are **scheduled**.
- More detail the **undesirable effects** of resource contention
    - [[Priority inversion]]
    - [[Deadlock]]
    - [[Time anomalies]]
## Additional terminologies
- A higher-priority job $J_{h}$ is said to be **directly blocked** by a lower-priority job $J_{l}$ when $J_{l}$ holds some resource which $J_{h}$ requests and is not allocated
- **Wait-for-graph**
    - A cyclic path indicates a deadlock
    - A path from higher job to lower priority  job is a directed block
    ![[Pasted image 20230617175623.png]]
## Notations
- A [[Periodic tasks]] $T_{i}$ has a [[Critical Sections]] $[R, x;y]$ if every job in $T_{i}$ requires at most $x$ unit of $R$ for $y$ units of time
- Denote: $T_{i}$ = $(\phi_{i}, \rho_{i}, e_{i}, D_{i};[R, x;y])$
    - $T_{1}$ = (50, 30;$[R_{3};10[R_{2};5]]$)
    - $T_{2}$ = (100,20;$[R_{2};7[R_{3};2]][R_{3};3]$)
    ![[Pasted image 20230617182309.png]]
    - Parameters are not relevant: $T_{i}$ =  $(\phi_{i}, \rho_{i}, e_{i}, D_{i}, c_{i})$
        - $c_{i}$: maximum [[Critical Sections]] 

# [[Resource access control protocols]] 
- [[Non-preemptable Critical Sections - NPCS]]
- [[Priority inheritance protocol]]
- [[Basic priority ceiling protocol]]
- Stack-based priority ceiling protocol


#REAL-TIME_SYSTEM 