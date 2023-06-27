- To **bring in information**, a program **opens** a stream on an information source ( a file, memory, socket, etc.), **reads** the information serially and then **closes** the stream
![[Pasted image 20230627201832.png]]
- A program **sends information** to an external destination by **opening** a stream to a destination, **writing** the information out serially, and then **closes** the stream
![[Pasted image 20230627202116.png]]
- We can create a Stream and open that Stream to the keyboard by creating an **InputStream** object
	- InputStream is = System.in;
- InputStream is a **Byte Stream** which can only read **single bytes**. We **convert** our InputStream to a **char reader** by wrapping it up as an **InputStreamReader**
	- InputStreamReader temp = new InputStreamReader (is);
- an InputStreamReader will only **read in data a character** at a time. We need to create a **BufferedReader** from the InputStreamReader to get a whole line of text
	- BufferedReader in = new BufferedReader (temp);

