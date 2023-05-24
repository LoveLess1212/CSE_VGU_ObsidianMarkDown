- Each computer in a distributed system has **its own internal clock**.
- Two processes running on different computers can associate **timestamps** with their events.
- Their local clocks may supply **different time values**.

#DISTRIBUTED_SYSTEM 

**##Berkeley Algorithm**
![[Berkeley Algorithm - img.png]]

a) The time daemon asks all the other machines for their clock value
b) The machines answer
c) The time daemon tells everyone how to adjust their clock

[[Logical clock]]
