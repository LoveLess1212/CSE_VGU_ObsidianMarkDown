- Independent of physical clock
    - Physical clocks may not be accurate
    - Different from machine to machine
- An event time
    - If A->B then C(A) < C(B)
    - If A and B are concurrent, then C(A) <, =, or > C(B)
- Solution
    - Each processor maintains a logical clock $LC_{i}$
    - Whenever an event occursz locally at i, $LC_{i}$ = $LC_{i}$ + 1
    - When i sends message to j, note $LC_{i}$ 
    - When j receives message from i
        - If $LC_{j}$ < $LC_{i}$  then $LC_{j}$ = $LC_{i}$ +1
        - Else do nothing
![[Logical clock - img.png]]

#DISTRIBUTED_SYSTEM 