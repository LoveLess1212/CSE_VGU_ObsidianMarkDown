> Model View Controller

# Description
* Separates presentation and interaction from the system data. The system is structured into three logical components that interact with each other. The model component manages the system data and associated operations on that data. The View component defines and manages how the data is presented to the user. The controller component manages user interaction (e.g., key presses, mouse clicks, etc.) and passes these interactions to the view and the Model
# Example
![[Pasted image 20230822144555.png]]
# When used
* When there are multiple ways to view and interact with data. Also used when the future requirements for interaction and presentation of data are unknown.
# Advantages
* Allow the data to change independently of its representation and vice versa. Supports presentation of the same data in different ways with changes made in one representation shown in all of them.
# Disadvantages
* Can involve additional code and code complexity when the data model and interactions are simple.

#SOFTWARE_ENGINEERING 