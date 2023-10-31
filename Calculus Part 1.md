# Sequence (aka. dãy số)
* Cho dãy $a_n$, nếu $\lim_{x \to n} a_{n} = L$ thì dãy $a_n$ converge, nếu không thì dãy này nó diverge :)))
* công thức L'Hospita
	* $\lim_{x \to \infty} {\frac{f(x)}{g(x)}} = \lim_{x \to \infty} {\frac{f(x)^|}{g(x)^|}}$ 
* coi lại các công thức về cấp số nhân, cấp số nhân lùi vô hạn ....
* Nếu 1 dãy số tăng hay giảm thì dãy đó gọi là dãy monotonic
* Dãy nó chặn trên nếu mọi số trong dãy đều nhỏ hơn 1 số L
* Dãy chặn dưới nếu mọi số trong dãy đếu lớn hơn 1 số "l"
# Series (Tổng 1 dãy số)
* aka $S_n$ hoặc $\sum_{i=1}^{n} a_i$ 
* Công thức tổng 1 cấp số nhân (aka. Gemetric series )
	* $\frac{u_1*(1-q^n)}{1-q}$ 
	* Nếu công sai $|q| < 1$ thì series converge
	* ngược lại thì series diverge
* Nếu Sequence $a_n$ có $S_n$ converge thì $\lim_{n->\infty} a_{n}= 0$ (nói theo kiểu tiếng việt thì là nếu dãy đó là 1 cấp số nhân lùi vô hạn thì $\lim_{n->\infty} a_{n}= 0$)
* Otherwise, nếu $a_n$ diverge hoặc $\lim_{a_{n}} \ne 0$ thì $S_n$ diverge
# Limit & continuous
>[!Squeeze Theo]
>Cho $f(x)\leq g(x) \leq h(x)$
>nếu $\lim_{x->a} f(x) = \lim_{x->a} h(x) = L$ (L ở đây là 1 số cố đình) 
>Thì $\lim_{x->a} g(x) =L$
>

- Cách để chứng mình 1 hàm số liên tục tại 1 điểm a:
	- $f(x)$ liên tục tại a nếu $\lim_{x->a}f(x)=f(a)$
	- hoặc
	- $\lim_{x->a^{-}}f(x) =\lim_{x->a^{+}}f(x) = f(a)$
- Cách để chứng minh hàm số $f(x)$ liên tục trên 1 khoảng $[a,b]$:
	- Chứng minh mọi số $i$ trong khoảng $[a,b]$ đều thỏa mãn  $\lim_{x->i}f(x)=f(i)$ 

>[!fact]
>Mọi 
>- hàm polinomial(hàm bậc 1 2 3) đều liên tục trên R
>- hàm phân số, hàm căn, hàm mũ, hàm lượng giác đều liên tục trên tập xác định

>[! intermediate theorem]
>nếu $f(x)$ liên tục trên $[a;b]$
>$\exists N \in [f(a),f(b)]$ và $c \in [a,b]$
>Sao cho $f(c) =N$
>
# integral
* Hiểu đơn giản ở đây mình đang tìm cách để tính diện tích tạo ra bởi hàm số f(x) và trục hoành trong khoảng $[a,b]$. Với những hình đơn giản như tam giác, hcn, hình tròn ... thì nó dễ rồi, nên k nói, nhưng mà giả sử f(x) là 1 hình parabol hay polinomial thì mình sẽ làm xao ?
	* mình sẽ chia nhỏ hình đó ra thành vô số hình chũ nhật rồi cộng diện tích của chúng lại với nhau, khoảng chia càng nhỏ thì diện tích tính ra càng đúng
* ![[Pasted image 20231018134337.png]]
* để có được diện tích càng đúng thì mình phải chia ra càng nhiều hình chữ nhật aka. $n -> \infty$
* lúc này công thức tổng quát sẽ là
* $A = \lim_{n->\infty} (f(x_{1})*\Delta x + f(x_{2)}*\Delta x + ... + f(x_{i}*\Delta x))$ 
* $= \lim_{n->\infty} \sum\limits_{i=1}^{n} f(x_{i)}*\Delta x = \int_{a}^{b} f(x) dx$ 
* khi đó $\Delta n = \frac{a-b}{n}$
* $x_{i}= a+ i\Delta x$ 
ví dụ:
>đề:
>tính $\int_{0}^{3} (x^{3}-6x) dx$ theo integral definition

giải:
![[Pasted image 20231018135705.png]]
## Những công thức cần nhớ khi làm dạng này 
![[Pasted image 20231018135543.png]]
* thường dạng bài này đề sẽ hỏi là *Evaluate ... using definition of definite integral*
* nếu đề nói *in term of area* thì mình sẽ vẽ hình ra trên hệ trục tọa độ Oxy thì mình sẽ vẽ - hoặc nhận biết công thức đường thẳng hoặc đường tròn trên hệ trục tọa độ Oxy rồi tính diện tích tạo bởi nó và đường thẳng Ox
$\lim_{x->\infty} 2+x\sin{\frac{1}{2x}} = 2+ \lim_{x->\infty} \frac{\sin{\frac{1}{2x}}}{\frac{1}{x}}$
kỉu cái này = 0/0 á nên mình dùng l hospita cho dễ, khum thì squeeze cũng được
$= \lim_{x->\infty}\frac{\cos\frac{1}{2x} * -\frac{1}{(2x)}^2}{-\frac{1}{(x)}^2}$ =1/4
