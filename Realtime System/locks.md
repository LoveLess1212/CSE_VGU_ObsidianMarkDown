- Assume a **lock-based concurrency control** mechanism
    - A job wanting to use $n_{k}$ units of resource $R_{k}$, it executes a lock, denoted $L(R_{k}, n_{k})$ to request the resource
        - $L(R_{k})$ if $n_{k}$ = 1
    - When the job is finished with the resources, it unlocks them, denoted $U(R_{k}, n_{k})$ 
        - $U(R_{k})$ if $n_{k}$ = 1
    - If a lock request **fails**, the requesting **job is blocked and loses the processor**; when the requested resource becomes **available**, it is **unblocked**
- A job holding a lock cannot be preempted by a higher priority job needing that lock
- Resources are released in the **last-in-first-out** order

#REAL-TIME_SYSTEM 