# Description
* The processing of the data in a system is organized so that each processing component (filter) is discrete and carries out one type of data transformation. The data flows (as in a pipe) from one component to another for processing
# Example
* Processing invoices
* ![[Pasted image 20230824102006.png]]
# When used
* Commonly used in data processing application (both batch and transaction based) where inputs are processed in separate stages to generate related outputs
# Advantages
* Easy to understand and supports transformation reuse. Workflow style matches the structure of many business processes. Evolution by adding transformations is straightforward. Can be implemented as either a sequential or concurrent system.
# Disadvantages
* The format for data transfer has to be agreed upon between communication transformations. Each transformation must parse its input and un-parse its output to the agreed form. This increases system overhead and may mean that it is impossible to reuse functional transformation that use incompatible data structure.
#SOFTWARE_ENGINEERING 

$\frac{x^{3}+x-1}{x^{2}+1}+\frac{y^{3}+y-1}{y^{2}+1}+\frac{z^{3}+z-1}{z^{2}+1}$
$\frac{(x - 1)(x + 1)(x + 1)}{x^2 + 1} + \frac{(y - 1)(y + 1)(y + 1)}{y^2 + 1} + \frac{(z - 1)(z + 1)(z + 1)}{z^2 + 1}$
$\frac{(x - 1)(x + 1)(x + 1) + (y - 1)(y + 1)(y + 1) + (z - 1)(z + 1)(z + 1)}{x^2 + 1 + y^2 + 1 + z^2 + 1}$
$\frac{(a - 1)(a + 1)(a + 1)}{(a^2 + b^2 + c^2) + 3} + \frac{(b - 1)(b + 1)(b + 1)}{(a^2 + b^2 + c^2) + 3} + \frac{(c - 1)(c + 1)(c + 1)}{(a^2 + b^2 + c^2) + 3}$
$\frac{(x^{3}+x-1)(y^{2}+1)+(y^{3}+y-1)(z^{2}+1)+(z^{3}+z-1)(x^{2}+1)}{(x^{2}+1)(y^{2}+1)(z^{2}+1)} = \frac{(x-1)(y^{2}+1)(x+1)+(y-1)(z^{2}+1)(y+1)+(z-1)(x^{2}+1)(z+1)}{(x+1)(y+1)(z+1)}$

$g_x + \lambda = 0 g_y + \lambda = 0 g_z + \lambda = 0 x + y + z = 1$
