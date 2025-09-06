# Huynh Gia Huy
## Old Comment
Layer Architecture 
Downward arrows connecting the components are totally missing
What are represented in your database layer are in fact entities / tables of a relational DBMS. We expect to see separate database systems in this layer.

Event-driven Architecture
Try to come up with a better name for Fine Management System to make it more general. It might handle functions other than fines.

Microservices Architecture
You should elaborate on the data schema of your microservices, i.e., what (multiple) entities to be represented? Simply giving a name to the data schema is not enough
## Comparison
### Layered 
* Old: ![[Pasted image 20240614143710.png|500]]
* new: ![[Pasted image 20240614143919.png]]
* Database layer is still entities or tables of a relational DBMS not database systems. And you might misunderstand the downward arrow, it could just be an arrow from the layer to the below layer.
### Event-driven 
* Old ![[Pasted image 20240614145851.png]]
* New ![[Pasted image 20240614145814.png]]
* you just changed the name of Fine Management system -> Request fulfillment system, which is even more confusing while there is already "Request-fulfillment".
* And your Inventory is even updated before you know that the return is applied or not ? Which is very unnormal, imagine you have 100 returning request denied, and 100 books missing from your inventory
### Microservice
* Old: ![[Pasted image 20240614150019.png]]
* new: ![[Pasted image 20240614150036.png]]
* the database is still unelaborated, please have a look at my old feedback.

database and Blocks on the on-chain
frontend-backend on the off-chain
# 