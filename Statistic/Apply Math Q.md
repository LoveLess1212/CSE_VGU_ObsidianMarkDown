## Q4
>The lifetimes of batteries are independent with an exponential distribution with a mean of 84 days. Consider a random selection of 350 batteries. What is the probability that at least 55 of the batteries have lifetimes between 60 and 100 days?

1. First we calculate the probability for $A$ (1 battery to have a lifetimes between 60 and 100)
	* Lifetimes *exponential distribution* (Lecture 13)
		* $F(x) = 1-e^{-\lambda x }$
	* mean 84 days -> *$E = 84$*
		* $\lambda = \frac{1}{E} = \frac{1}{84}$ 
	* the probability to have a lifetimes between 60 and 100 ( using exponential distribution)
		* $P(A) = P(06 \leq X \leq 100 ) = F(100) - F(60) \approx 0.1874$ 
2. A have only 2 outcome -> *binomial distribution* (lecture 12) -> could be expected by *normal distribution* (lecture 14)
	*  Mean($\mu$) of 350 batteries 
		* $\mu = 350*P(A) = 65.59$ 
	* Variance($\sigma^2$) : $350*P(A)*(1-P(A)) = 53.298$
3. calculate the requested prob
	* $P(X\leq 54.5) = 1-P(X\leq 54.5)$ 
				$= 1- \phi(\frac{54.5 - \mu}{\sigma})$
				$= 1- \phi(-1.52)$ (đối chiếu với bảng z-value)
				$= 1- 0.0643 = ...$
:))) xong rồi á,
ở trên anh dùng 54.5 thay vì 55 thì nó có 1 cái gọi là *continuinity correction* á
có gì em đọc thêm ở đây [link][https://openstax.org/books/statistics/pages/7-3-using-the-central-limit-theorem#:~:text=We%20add%200.5%20if%20we,p%20q%20n%20p%20q%20.] đoạn historical note á

## Q5
>A multiple-choice test consists of 20 questions, each with four possible answers of which only one is correct. A student passes the test if 15 or more correct answers are obtained.

*(d): How many questions are needed in order to be 99% confident that a student who guesses blindly at each question scores no more than 35% on the test?*

* Bài này cũng na ná bài trên :V, nhưng mà a mới kiểm tra thì hình như 2 bài cuối em chưa học :))))))), k làm được cũng hợp lý
* mình cũng tương tự dùng binomial distribution + normal distribution là ra
* coi n là số câu hỏi
* $P(X<n) = \phi(\frac{x-\mu-0.05}{\sigma^2})$
	* x: $0.35*n$ (35% của toàn bộ câu hỏi)
	* $\mu: 0.25 * n$(xác xuất lụi dính 25%)
	* 0.05 là *continuinity correction*
	* $\sigma: 0.25*0.75*n$
* coi trong bảng z value thì 99% ~ 2.33 
* giờ mình giải sao cho $P(X<n) \approx 2.33$ là xong :V
* anh giải ra bằng $~101.7$ nma cái này là discrete var thế nên em lấy 101 hay 102 cũng được, k thì em để đáp án là 101.7 luôn :)))))) tại cái công thức này mình học cũng chỉ ước tính đc thôi chứ không có tính hoàn toàn ra được.