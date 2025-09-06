---
tags:
  - CURRENT_TOPIC
---
>aka. PROcess MEta Language

* intended for modeling a system with a finite number of processes. A run of Promela model does not require any input. The processes may run synchronous or asynchronous and may communicate via channels or (shared) global variables. 
* Processes run interileaved in any arbitrary possible order, the system could be non-deterministic, i,e, two different runs of the system may yield different results. However Promela allows for nondeterminism within a single process.
## Function
> [!main function]
> Nondeterminism -> it is important feature to verify and check concurrent systems

* a statement can only run if it is executable. Some statements may always be executable. However, a logical expression like `a==1` is only executable if it is true. If a process encounters the expression `a==1` and the value of a is 0, it will block until the value of a changes to 1 which may only happen by the workings of another process
* 