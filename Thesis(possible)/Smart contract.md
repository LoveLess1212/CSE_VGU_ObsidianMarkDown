* Tại sao mình lại chọn BPMN, vì mình có thể enact từng bước của nó được
* có thể chuyển thành 1 app chuyên hỗ trợ [[point-to-point|P2P]] transfering 
* Không quan tâm nó tạo ra [[Cardano Transaction|transaction]] kiểu gì, cái mình cần kiểm tra là cái [[Cardano Transaction|transaction]] này hợp lệ hay không, kiểu như là 1 cái tester đảm bảo cho cái logic của mình luôn luôn chạy đúng
# Question 
1. Có nên lưu BPMN vào [[blockchain]] không, nếu có, mình nên lưu nó ntn
2. What happen when 
# Flow
* Khi customer A đăng ký sử dụng 1 dịch vụ của bên B
	1. Bên A tạo ra 1 [[Cardano Transaction|transaction]] chuyển tiền cho bên B, và nó sẽ được lock cho đến khi cái service hoàn thành (BPMN đi đến bước kết thúc)
	2. Mình có thể handle BPMN qua nhiều cách, cũng có thể qua event channel.
		1. nếu qua event channel thì sẽ bị cân nhắc về tính dư thừa của BPMN.
		2. nếu không qua event channel thì sẽ mất nhiều thời gian để xử lý BPMN mà không chắc chắn có thể 
	3. 
	4. Khi hoàn thành, thì bên A sẽ *bằng 1 cách nào đó* release cho bên B 1 cái key để redeem, hoặc là sẽ *tự động* khi bước cuối của BPMN hoàn thành
## BPMN Handling
* Multiple escrow contract until reached the final state 
* State channel

# Definition
# What I Have Known already
* Smart contract có input và output 
* [[Validator]] sẽ được đính vào smart contract để xác nhận rằng cái contract này, có được thực hiện hay không