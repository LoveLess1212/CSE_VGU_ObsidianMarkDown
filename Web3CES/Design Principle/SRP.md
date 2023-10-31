> A [[module]] should be responsible to one, and only one, actor.

## Symptom 1: Accidental Duplication
> Separate responsibilities into distinct classes to improve cohesion and maintainability. Avoid combining unrelated tasks within a single class. Each class should have a single, well-defined responsibility aligned with the needs of a specific actor or stakeholder. This separation promotes better organization, reduces complexity, and minimizes the risk of unintended side effects when making changes or updates.

>TLDR:
>separate code that supports different actors.
## Symptom 2: Merge
same :V
>separate code that supports different actors.

## Solution:
* Separate the data from the functions. The three classes share access to Data, which is a simple data structure with no methods. Each class holds only the source code necessary for its particular function. The three classes are not allowed to know about each other.
	* This sol raise a problem that now the developers now have three classes that they have to instantiate and track. But this can be solve using *Facade* pattern

#CES 