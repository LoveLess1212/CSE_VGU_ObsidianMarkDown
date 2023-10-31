---
tags:
  - CES
---
>**This architecture style is a natural fit for product-based applications (packaged and made available for download and installation as a single, monolithic deployment…**
* The microkernel architecture style is a relatively simple monolithic architecture consisting of two architecture components: a core system and plug-in components. Application logic is divided between independent components and the basic core system, providing extensibility, adaptability and isolation of application features and custom processing logic. 
### **The core system**
* The core system is defined as the minimal functionality required to run the system. It is responsible for providing the basic mechanisms for dynamically loading and unloading plug-in components, for managing the life cycle of the plug-in components, and for providing the services that the plug-in components can use.