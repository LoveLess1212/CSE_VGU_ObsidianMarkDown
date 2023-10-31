[[CRC]]
* Transmission errors can be detected via [[CRC]] checksums
	*  If it is important also to correct errors, the data to be transmitted must be c=encoded in a way that error-correction is possible
* Error correction can be realize via Hamming :V
Example:
```
* Data to be transfer: D - 1110
* Generator: G = 1011
* Vì G có 4 ký tự, nên phải thêm vào D 4-1=3 số 0 vào cuối
* -> D'= 1110000

Người gửi
1110000
1011---
=======
-101000
-1011--
=======
--00100
=======
----100
-> Đoạn Data được gửi = Data cũ + data sau khi được tính
= 1110100
Người nhận
1110100
1011---
=======
-101100
-1011--
=======
-----00
= 0 
-> correct
--
```
## Hamming code
### Position Parity Bits
* The bits of a bit seq are numbered starting with 1 from the left
	* Bits which are powers of 2 are parity bits
* The sender calculates the parity bits values
### Parity bit Values

#COMPUTER_NETWORK 

