# Cân cà phê page
> canCaPhe
* Without any previous record
	* create new record button in the middle
* Already some record 
	* 2 * x box, the first box is create new record, 
	* existed box including date - title - ID
> canCaPhe/:IDofWRecord
* Create a WRecord
* auto save after each WRecordDetail 
* top
	* changing name ( default create name: cân - {date})
	* change view (view mode & edit mode)
	*  change informations: Độ, tạp, mốc
* main content ( edit mode)
	* record
	* 5 input (number-integer only, press enter to go to the bottom input, if it is the last input field, save current record & create new input)
	* last readonly inputfield: sum of 5 input
* main content ( view mode)
	* show 5 record next to
	* bottom button to 
		* add informations: Độ, tạp, mốc & the calculation to reduce from the total weigh
		* save & go back
* Database 
	* WRecordDetail: 
		* ID ( auto)
		* W1 -> W5 (for each input)
		* total ( sum W1 -> W5)
		* WRecordID
	* WRecord
		* ID
		* Name
		* Date
		* Humidity 
		* Impurity
		* Mold
		* Total


minh hoa datum, va redeemer 
Fee

Check xem chay duoc o dau la off chain hay on chain 

dạ, cái việc check mà 1 transaction hợp lệ hay không thì sẽ diễn ra ở cả 2 phía

Ví dụ, mình tạo 1 transaction ở off chain với thông tin: cần 2 người tham gia, A và B ký, với tài sản X(tài sản này sẽ chứa datum), 

---
Off chain: check trước khi được gửi vào blockchain để kiểm tra xem cái transaction này có phải là 1 transaction hợp lệ như nó đề ra hay không (chưa liên quan đến nội dung của smart contract)

- số lượng chữ ký
- người ký khớp với yêu cầu
- người này có tài sản đó hay không
- đủ tiền trả phí hay không
- cấu trúc transaction ( thuần về mặt nghữ nghĩa)
- ...
Nếu không đạt 1 trong những yêu cầu -> transaction fail, không thể gửi lên on chain
---
On Chain: kiểm tra transaction này thoả mãn những điều kiện của redeemer trong Smart contract hay không? 



- Null (no customer)
- Null (no partner)
- Hashing Chor.Tasks
- Null (no prev.)
- First Task
- Next Task
- Hashing BPMN XMI


Đánh số eUTxO

Bảng map từ 