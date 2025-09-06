---
tags:
  - IT_SECURITY
---
1. How is a maliciously injected script which is permanently stored on the target servers,such as in a [[database]], in a message forum, visitor log, comment field, etc called which the victim retrieves from server when it requests information?
	1. Stored [[XSS]]
2. Define the [[FFPP/Term]] [[Command Injection]]
  - [[Command injection]] is an attack in which the goal is execution of arbitrary commands on the host operating system via a vulnerable application. [[Command injection]] attacks are possible when an application passes unsafe user supplied data (forms, cookies, HTTP headers etc.) to a system shell.
3. If http://192.168.1.50/dvwa/vulnerabilities/[[[[[[xss]]]]]]_r/?name=<script>alert("Alarm!")</script># results in the Java-Script code being executed, it is an example of
  - Reflected [[XSS]]
4. explain CSRF
  - CSRF: cross-site request forgery, is an attack that forces an end user to execute unwanted actions on a web application in which they're currently authenticated.
  > Bởi vì form request có thể copy được do quá trình post - get data, nên nếu biết được link của request đó, mình vẫn hoàn toàn có thể gửi lệnh request đó ở 1 trang khác.
  > Case:
> 	Prep:
  > 	Hacker tạo 1 trang web gì đó thường là blog, có 1 button, nếu người dùng bấm vô nút này, website sẽ gửi 1 lệnh request tới trang web của trang ngân hàng để chuyển tiền tới tài khoản của hacker
> 	trigger:
  > 	Nếu m đã đăng nhập vào 1 trang ngân hàng nào đó, đã làm đủ tất cả mọi bước auth rồi, để tab đó qua 1 bên.
  > 	M qua trang web kia mà hacker tạo ra (cái quan trọng là m không biết trang web đó hacker tạo ra :V), bình luận 1 cái gì đó. -> (bấm nút)
  > 	Lúc này, trang web của hacker sẽ gửi 1 lệnh request tới web ngân hàng (lúc này đã được qua tất cả mọi bước auth, vì m đã đăng nhập)
  > 	Cuối cùng, tiền của m biến mất :))) tới tài khoản của hacker
> 	prevention:
  > 	Nếu m là dev của trang ngân hàng
  > 	m nên dùng 1 thứ gọi là token - cookies gửi chung với request để kiểm tra nguồn request, nếu request đó không tới từ trang web aka. Referer header nhưng thứ này có thể gây ra khá nhiều vấn đề
  > 	Nên bh người ta dùng token, token này được tạo ra mỗi khi cái form này được tạo ra và được lưu vào trong hệ thống, được reset sau n phút và khác nhau với mỗi người. Nên nếu hacker sử dụng token đó để nhét vào cái web của nó, thì sẽ không dùng được, vì cái token nó đã expired rồi.
  > 	
  
  Example: 
5. explain [[XSS]]
	- Cross-Site Scripting ([[XSS]]) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. [[XSS]] attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user.
> Bởi vì mọi thứ trên HTML đều được bắt đầu bằng 1 cặp ngoặc <> và </>
> nên mình có thể nhét 1 cặp tag script vào giữa, nếu form không được validate, thì web của mình sẽ chạy đống script đó, như chưa có gì xảy ra
	
6. explain Dom-based [[XSS]]
	- is an [[XSS]] attack wherein the attack payload is executed as a result of modifying the DOM "environment" in the victim's browser used by the original client side script, so that the client side code runs in an "unexpected manner"
7. explain stored [[XSS]]
	* Stored [[XSS]] generally occurs when user input is stored on the target server, sa in a database, in a message forum, visitor log, comment field, etx. And then a victim is able to retrieve the stored data from the web application without that data begin made safe to render in the browser.
8. explain command injection
	1. Command injection is **a cyber attack that involves executing arbitrary commands on a host operating system (OS)**.
9. explain [[SQL]] injection
	1. [[SQL]] injection usually occurs when you ask a user for input, like their username/user id, and instead of a name/id, the user gives you an [[SQL]] statement that you will **unknowingly** run on your [[database]].