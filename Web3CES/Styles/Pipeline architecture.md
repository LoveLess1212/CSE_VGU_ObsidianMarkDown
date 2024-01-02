---
tags:
  - CES
---
>**Most developers know this architecture as this underlying principle behind Unix terminal shell languages, such as Bash and Zsh.**
* The pipes and filters coordinate in a specific fashion, with pipes forming one-way communication between filters, usually in a [[point-to-point]] fashion
* Filters are self-contained, independent from other filters, and generally stateless. Filters should perform one task only. Composite tasks should be handled by a sequence of filters rather than a single one. Four types of filters exist within this architecture style:
  * producer: The starting point of the pipeline, aka the source
  * Transformer: The filter that transforms the data
  * Tester: The filter that tests the data
  * Consumer: The end point of the pipeline, aka the sink
 
#CES 