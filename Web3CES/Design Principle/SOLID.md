> The solid principles tell us how to arrange out functions and data structures into classes, and how those classes should be interconnected. 

>The use of word "class" does not imply that these principles are applicable only to object-oriented software. they are a coupled grouping of functions and data. Every software system has such groupings, whether they are called classes or not. **SOLID** principles apply to those groupings.

# GOAL
The creation of mid-level software structures that:
* Tolerate change
* Are easy to understand, and
* Are the bases of components that can be used in many software systems
> [!Mid-level ]
> refers to the fact that these principles are applied by programmers working at the [[module]] level. They are applied just above the level of the code and help to define the kinds of software structures used within modules and components.

Just as it is possible to create a substantial mess with well-made bricks, so it is also possible to crate a system-wide mess with well-designed mid-level components. For this reason, once we have covered the SOLID principles, we will move on to their counterparts in the component world, and then to the principles of high-level architecture.

# Type
## [[SRP]]: The Single Responsibility Principle
An Active corollary to Conway's law: The best structures for a software system is heavily influenced by the social structure of the organization that uses it so that each software [[module]] has one, and only one, reason to change
## [[OCP]]: The Open-Closed Principle
Bertrand Meyer made this principle famous in the 1980s. The gist is that for software systems to be easy to change, they must be designed to allow the behavior of those systems to be changed by adding new code, rather than changing existing code.
## [[LSP]]: The Liskov Substitution Principle
Barbara Liskov's famous definition of subtypes, from 1988. In short, the principle says that to build software systems from interchangeable parts, those part musts adhere to a contract that allows those parts to be substituted one for another.
## [[ISP]]: The Interface Segregation Principle
This principle advises software designers to avoid depending on things that they don't use.
## [[DIP]]: The Dependency Inversion Principle
The code that implements high-level policy should not depend on the code that implements low-level details. Rather, details should depend on policies.

#CES 