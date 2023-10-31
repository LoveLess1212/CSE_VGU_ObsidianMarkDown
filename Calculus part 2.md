> Phần này dài quạ :'), chắc t chỉ giải thích lại bằng tiếng việt cho m dễ hiểu thoi ha, có gì về làm bt thì cứ nhắn t 

> [!tldr]
> Phần này nói về đạo hàm và các ứng dụng của nó trong việc giải quyết các vấn đề vật lý (vận tốc, độ thay đổi vận tốc ...), cũng như các vấn đề toán học đang tồn tại mà không thể giải quyết được bằng các phương pháp khác, cụ thể như: 
> 	Tìm đường tiệp cận của 1 hàm số tại 1 điểm
> 	Tìm số xấp xỉ của 1 hàm số phức tạp quanh 1 điểm a (Linear approximation, quad approx, Taylor Series - Maclaurin series) 
> Qua đó, vô tình tìm ra được cách để
> 	Tính liên tục của 1 hàm số có đạo hàm
> 	Tìm cực trị 
# 1. Định Nghĩa Đạo Hàm

![[Pasted image 20231022014906.png]]

>[!theorem 1]
> If f is differentiable at a, then f is continuous at a.
> **Nếu 1 hàm số có đạo hàm tại 1 điểm thì nó liên tục tại điểm đó**
## Giải thích
* f'(a) đại diện cho độ thay đổi của hàm số f tại giá trị a aka. góc của đường tiệp cận tạo với Ox
* Để hiểu được tại sao có công thức này, m có thể nhìn vào hình dưới
* ![[Pasted image 20231022015020.png]]
* Để tìm được góc của đường tiệm cận tại P thì mình cần tìm được góc của đường tiệm cận tại P, (vì P là điểm duy nhất mình có, mà tìm được công thức 1 đường thẳng thì mình cần 2 điểm lận :V)
* nên lúc này mình sẽ lấy 1 điểm Q nằm trên f(x), sao cho Q càng gần P càng tốt (vì càng gần thì cái góc mình tính ra càng đúng) 
* nên trong ví dụ trên, cái tần số góc hay độ dốc k trong công thức $y=k(x-x_{0})+ y_0$ 
	* sẽ là $\frac{x^{2}-1}{x-1}$ 
		* kiểu $\frac{y-y_0}{x-x_0}$ á
* mà như đã nói, càng gần điểm đó thì cái độ dốc càng đúng, vậy nên nó sẽ là ![[Pasted image 20231022020141.png]]
* sau đó người ta đặt h cho dễ tính thôi, chứ bản chất của nó vẫn là như vầy.
## Dạng 1: Tìm đường tiệm cận 
* dùng cthc  $y=k(x-x_{0})+ y_0$ aka.  $y=(f^{|}x)(x-x_{0})+ y_0$ 
## Dạng 2:  Tính :V
> Cái này thì coi lại công thức hồi cấp 3 har :')

* ở Đại học thì nó sẽ khác (chi tiết thêm 1 xíu)
	* Đạo hàm bậc 1 nó sẽ là $\frac{dy}{dx}$ hoặc$\frac{df(x)}{dx}$ hay còn gọi là đạo hàm của y-f(x) theo x,
	* Bậc 2: ![[Pasted image 20231022021055.png]] tương đương $f^{||} x$
	* Bậc 3 : ![[Pasted image 20231022021143.png]]
	* Bậc n: ![[Pasted image 20231022021156.png]]
* mấy cthuc đặc biệt: ![[Pasted image 20231022021553.png]]
# 2. Ứng Dụng
> concept đứng sau đống này là mình sẽ dựa vào cái mà t giải thích ở phần giải thích ở phần 1 á, mình tính giá trị xấp xỉ của 1 số x gần số a, càng gần càng đúng :V. 
> 	Tại sao lại phải gần 1 số *a* :))))))) mà không phải số đó mẹ luôn :)))
> 		vì có thể mình biết được căn 4 =2 nhưng đ biết căn 5 bằng bao nhiêu, thì mình sẽ tính xx giá trị căn 5 theo giá trị của căn 4
## Linear Approx:
![[Pasted image 20231022021700.png]]
* để giải thích cái này thì đọc lại phần giải thích ở P1 nha :V, chỉ là nhân lại với mẫu để lấy phần bị dịch ra thôi
## Quadratic Approx
* cũng là Linear Approx nhưng mà đạo hàm thêm 1 lần nữa :V
* ![[Pasted image 20231022022009.png]]
## Power series
* Đ liên quan m gì tới đống này :))))), chỉ là thêm vài công thức hỗ trợ tụi Taylor với Maclaurin series thôi
## Taylor
* là linear approx với đạo hàm n lần nữa:V -> độ chính xác sẽ hơn nhiều Linear approx (nếu ai có đủ sức lực tính toán :)))))) )
![[Pasted image 20231022022250.png]]
### Maclaurin series
* Là taylor series với a=0 
* ![[Pasted image 20231022022404.png]]
* đọc lại định nghĩa: là xấp xỉ của 1 hàm số f xung quanh số 0 :V
	* tại sao lại là số 0:
		* vì nó cách đều mọi số 
		* vì nó dễ tính toán 
			* (chứ giả sử khi tính xấp xỉ f(x) tạix =1000 đi chẳng hạn thì Taylor series của f(x) với a = 999, hoặc a =1000 vẫn đúng hơn Maclaurin :V)
			* Nhưng đ có ai đủ sức để tính đống đó :)))))) sooo, we have Maclaurin
## Phần còn lại (cực trị - Newton iteration)
* Điểm cực trị thì coi lại C3
* Newton ite t thấy nó dễ á, nhớ coi lại thôi là được :')'