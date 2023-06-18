- Simplest resource access control protocol
    - When a **a jobs acquires** a resource it is **scheduled with highest priority** in a non-preemptable manner
    - **Deadlock can never occur**
- ### Advantages:
    - Simplicity
    - Can be used for both fixed and dynamic priority
- ### Disadvantages:
    - **Every job can be blocked** by every lower-priority job with a [[Critical Sections]], even if there is no resource conflict; very poor timing performance
    - Blocking time of $T_{i}$ due to resource conflict in a $n-$[[Periodic tasks]] system:
        - $b_{i}(rc)$ = $max_{i+1<=k<=n}(c_{k})$
        - Tasks are indexed in order of nonincreasing priority
![[Pasted image 20230617191648.png]]

#REAL-TIME_SYSTEM 