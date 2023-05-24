## Contain functions for
- [[Memory management]]
- process management
- interprocess communication
- hardware management
- [[File Systems]]
## Advantages
- fewer context swtiching as with [[microkernels]] -> better performance
- Grown stability
	- [[microkernels]] are usually not more stable compared with monolithic [[kernels]]
## Drawbacks:
- crashed kernel components can not be restarted separately and may cause the entire system to crash
- Kernel extensions cause a high development effort because for each compilation of the extension, the complete kernel need to be recompiled.
Linux using *Monolithic [[Kernels]]*


Monolithic [[Kernels]]
#OPERATING_SYSTEM