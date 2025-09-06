** * consist of both in on chain and off chain
	 * on chain: only consist of rules that to validate if the [[Cardano Transaction|transaction]] is comply with the rules of the [[blockchain]]
	 * off chain: generate the [[Cardano Transaction|transaction]] + [[datum]] that conform with the rules


> [!assumption]
> BPMN luôn là dạng có deontic rule (how to check this ?)(for now, impossible as it in metadata)
> No option to not sign the transaction

---
# Function:

* ai sẽ là người chọn next [[task]] (người làm task trước)
# SC creation (Onchain)
* người dùng inititate 1 -> deposit vào trong SC
* Chạy Task dùng function task
* Finalize
* đánh giá (how) 
* (optional) end bất cứ lúc nào nếu muốn
# Checking ([[Validator]])
* [[Init]]
	* Kiểm tra fee được gửi vào túi của owner :))
* [[Task]] action
	* [[Task]] của Provider thì cần cả 2 người ký :V, 
	* [[Task]] của user thì chỉ cần provider ký, giảm thiểu [[collateral]] fee cho user
 add [[task]] sau vào trong [[datum]]
* Finalize,
	* 2 chữ ký
	* kiểm tra [[datum]] cũ, nếu next [[task]] = **[end task](endtaskSC)** 
	* kiểm tra tiền được gửi cho provider
	* kiểm tra 1 cái gì đó dùng để confirm user đã hoàn thành cái bpmn này được gửi cho user - thật ra là tx hash thôi là đủ :V
	* [[kiểm tra có 1 output to Provider là 1 UTXO chứa token đánh giá]]


> kiểm tra xem khi consume khi token gửi cho bên 