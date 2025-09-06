Service được mint dựa trên Dapp Owner, và seller -> Mỗi seller có 1 policy ID riêng cho những token đấy -> có thể đếm được có bao nhiêu service cho mỗi người bán


mình có thể kiểm tra datum trước khi rating là gì luôn ... 
Redeemer 
* Rate(rating) -> Kiểm tra Transaction cuối cùng là transaction kết thúc (how?)
* và thêm rating vào đâu ? 



Validator Mint
Param:
- lấy Service Token Policy ID của service đó
- lấy kết quả (true-false)
-> đảm bảo chỉ ra 2 policy ID đặc biệt cho riêng service đó, không phân biệt ai rate
Checking:
- Tên ?
- oneshot

Làm sao để kiểm tra không ai khác ngoài mình(seller) có thể mint được cái này ?
kiểm tra seller có sign thôi là được, bằng cách tìm datum ở trong token Service.
Làm sao để biết được mint chung với transaction ? input từ script address 

Mint chung với transaction 

Dear Dr. ,
I don't know if you could attend my Thesis Oral defense on 9/12, if you can't attend it offline, you could attend it online through the link I sent later.

Best ..