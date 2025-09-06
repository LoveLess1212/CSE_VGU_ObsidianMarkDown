---
tags:
  - BLOCKCHAIN
  - Thesis
---
## [[Provider Verification Token]] 
* The Token was only minted for testing for the app, but not for commercial use, so that they could be less secure in [[FFPP/Term]] of ....


For now I have to focus on the [[validator]] part to actually work on the part that the thesis states

Mint(doable) -> Marketplace(doable) -> Check BPMN -> Result --- done

# Check BPMN part
## Read the BPMN
* Chạy từ trên xuống dưới, kiểm tra xem cái mình đang xem là bước nào
## [[Cardano Transaction|Transaction]], [[smart contract]]
Logic cơ bản

A người mua - B người bán 

Với mỗi lần gặp 1 element trong BPMN thì mỗi người sẽ ký 2 lần

A mua 1 service của B - cả 2 ký -> tiếp tục
* normal rules 
	* nếu 1 bước nào đó mà A không ký -> refund cho B
	* 1 bước nào đó mà B không ký -> quay về bước compensation gần nhất - nếu không có bước compensation gần nhất, -> refund ngay lập tức -> uncompensated

* Nếu gặp 1 block bình thường
	* cả 2 ký -> tiếp tục
* nếu gặp exclusive gateway
	* cả 2 confirm đi bước này đúng không -> tiếp tục


làm 1 vài token sample demo frontend
làm 1 vài [[Cardano Transaction|transaction]] demo escrow

---

tại sao newDatum không phải là [[datum]] ?

input [[datum]] không sửa được, do nó là [[datum]] của 
[[Cardano Transaction|transaction]] là ai gửi cái gì cho ai cái gì cho ai
script được gắn vào [[Cardano Transaction|transaction]] ([[Validator]] ) là thứ kiểm tra [[Cardano Transaction|transaction]] xem 
output aka. là 1 dạng tài sản nhưng với script đi theo
[[datum]] được tạo ra khi tạo ra output mới
[[redeemer]] được sử dụng khi spend cái output đấy

giờ nó chỉ là escrow thôi, không [[redeemer]] :V

giờ ở trong flow chính, 
Trong [[Cardano Transaction|transaction]] mình sẽ specify new route(just new hash id) vào [[redeemer]] cũng như provide new [[task]] vào trong [[datum]] mới

- Redeemers 
[[Task]]([[task]] mới):
* [[datum]] mới có được cập nhật theo đúng với những gì state trong [[redeemer]] hay không ?
* có 2 người ký hay không ?
Cancel: 
* có ai trong 2 người đó ký hay không ?
* người dùng có được trả lại tiền hay không? 
Finalize([[task]] mới):
* cả 2 người ký

mục tiêu của mình là mỗi bước đều được lưu lại -> không cheat được
nếu thế những bước được lưu lại là những gì ?
* hash của bpmn
* 2 [[parties|participants]]
* những bước đã đi - bởi vì nó có cả trước, hiện tại, và sau, nên khả năng cheat nó sẽ ... vãi l :))) khả năng cao nó sẽ đ bh xảy ra :V
có cả bắt đầu và kết thúc hay không ?
tạo ra 1 [[Cardano Transaction|transaction]] bắt đầu, cả 2 đều ký .-. done gọi là [[init]] 
tạo ra 1 [[Cardano Transaction|transaction]] kết thúc, cả 2 đều ký, nhưng mà có [[datum]]


Người mua sẽ luôn luôn mất 1 lượng tiền cố định - không đáng kể vào chain, bởi đấy

List asset (seller) - done
Start (buyer) - 
Each Step (n) (seller) - 
Finalize (seller) - 

done

Frontend user step

1. Seller could see the list of services that are on sales on this platform -> services view
2. Could click to any of them, to start  -> BPMN services view
3. like the draft
4. when done, show button to route back to services

Make a sample BPMN first -

---
 should modified to ensure 2 parties could both see the process on the bpmn * also the check Txbody on the buyer view
 
Start
1. mem: 215315
2. steps: 77386668
Task 1
1. mem: 277618
2. steps: 93271641
Task 2
1. mem: 285634
2. steps: 96874957
End
1. mem: 268106
2. steps: 90 482 454

Dear Dr. Son,

Thank you for your request. I'd be happy to help with the session. However, I have a few questions to ensure I can provide the best support:

1. Are there any specific requirements the students need to meet, such as an end product for midterm assessment?

2. Would it be possible to schedule a meeting this week to discuss the session in detail? Since Aiken is a specialized language requiring significant background knowledge not to write, but to understand the purpose of it, I want to ensure that I understand the scope and requirements correctly.

I look forward to your response.


Check all the todo
redraw  --
check inconsistency
add code for BPMN parser
Cite the background
fix citing part for BPMN
cite the conclusion
Acknowledgement


Mesh Token image sample Token Background
Fix phase on 4.2 ?

Academic Rigor

Recapture image.

Linking
evaluation on the approach chapter

C -> G/B -> Am -> Fm* -> G* -> C -> G/B -> Am->Dm ->Fm->G -> C -> G/B* ->Am* -> Dm->Fm->G



Am -> Dm -> G -> E7 -> Am -> 

# All user can(when not connected):
* See all listed service 
# After connected to the wallet 
* Mint the service token to be the service provider(if not be a service provider)
* Buy(Start any listed service)
* See the process and 
## Service provider can:
* Create, List a service
# When on a Active Service
All can: 
* See the process
* Cancel 
* Sign the transaction
## Service Provider Can
* Task - Finish Initiator 

Dear students,

Please follow these steps to register your topic:

1. First, review the available topics in our class spreadsheet [insert link].
2. To register your topic, send an email to [17431@student.vgu.edu.vn](mailto:17431@student.vgu.edu.vn) with:
    - Subject line: "Intro to CS - Group 2 - Topic Register"
    - Email body: Include your group name and your chosen topic

Please ensure you check the spreadsheet before sending your registration to avoid duplicate topic selections.

Best regards, [Your name]

Start and end symbol of the workflow: shall we create a transaction block ? if yes, what in-block data to capture?

Yes and 

Choreography task-ID generated in BPMN XML

What’s about rule-ID? - It is represented by the hashed of the whole rule BPMN-XML 

Provider – Consumer – list of partners (optionally)

## Rule ID
I think this one is already represented by the full bpmn-xml hashed of the rule. If we want to store this, we could store in a off-chain database.
## Outcome of the task: true / false -
No need because
This is already represented by the proposal of the provider for the next task, and the next task will represent for the outcome of the last task. For example:
* Previous transaction task: Provider alternative room
* The provider could provide that room -> 
* The provider will create a transaction with current task is contract fulfilled. ( this transaction will need to be signed (acknowledged) by buyer to confirm that) 
This approach is because on the BPMN we already model all the outcome of the rule(if satisfy go this task, and if not go to another).

## Start and end symbol
* yes, the start event is represented by the action listing 
* the end event is now represented by action fund release for both party

figure 4: re draw -> off-chain db -> confirm data hash on chain

data model 

tại sao dùng cardano ?