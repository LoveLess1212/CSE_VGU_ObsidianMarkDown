This guide will walk you through setting up a Cardano wallet on the testnet using the Eternl wallet extension.
# Setup
* https://chromewebstore.google.com/detail/eternl/kmhcihpebfmpgmihbkipmjlmmioameka?hl=en-US&utm_source=ext_sidebar
* Open the wallet from the extension bar
* Change the network to preproduction: ![[Pasted image 20241220115855.png]]
* ![[Pasted image 20241220115944.png]]
# Create a Wallet
* Click Add wallet -> Create Wallet
![[Pasted image 20241220120236.png]]
* Set the Wallet name and password as your pref -> save
 ![[Pasted image 20241220120439.png]]
 * Set the number of account you want (1 is enough for this turto) -> save
  ![[Pasted image 20241220120552.png]]
  * Confirm and continue on the hint stage ( of course after you read those info that they give)
  ![[Pasted image 20241220120703.png]]
  * Carefully write down these 24 words, these word represent for your account, and if anyone have these 24 words, they will have all the control on this wallet. However, we are on the test network so it doesn't matter much 
  ![[Pasted image 20241220120822.png]]
  * Retype those 24 word to confirm that you have "carefully wrote it down" -> continue
# Connect the wallet and get the fund
![[Pasted image 20241220121721.png]]
1. Activate the wallet as the main wallet
2. Go to this window -> Connect DApp account ( for testing further)
3. Go the receive window to get this wallet's address
![[Pasted image 20241220121942.png]]
5. copy that address, go to https://docs.cardano.org/cardano-testnets/tools/faucet
6. Set the correct Environment (preprod testnet) -> set address  -> request fund![[Pasted image 20241220122058.png]]
7. Wait 1-2 minutes for the fund.
8. You could check it from Transaction tab ![[Pasted image 20241220122258.png]]
# Setup collateral
Collateral is a mechanism to make sure that you are not trying to DDoS the system
1. Go to wallet setting![[Pasted image 20241220122404.png]]
2. Go to Collateral -> Set Collateral![[Pasted image 20241220122444.png]]
3. Sign that transaction with your wallet password![[Pasted image 20241220122610.png]]
That is all the setup you need to use Wallet on cardano.
# Exercise 
## Exercise 1: Test Minting (create) a Token
https://plutuspbl.io/live-examples
Follow the tutorial to mint: 
- A custom PPBL token
- 1,000,000 Plutus PBL 2024 Scaffold Tokens
## Exercise 2: Send a fund to a wallet
1. Navigate to the "Send" page in your wallet 
2. Send exactly 2024 tADA to this address: addr_test1qrf0hw6c5t4tpx8ma38r8lxc7nd7eqecgkyvx34ttajveua8ncqydgd7nszsgswadjnlrtj9722gyswmghd3gwctszqs5l2fdf

## Submission 
* submit your address, transaction hash for exercise 1 - 2 in this spreadsheet.
Group 1:
https://docs.google.com/spreadsheets/d/1X_3LRCIELMYt4xRRrE3ugNCPSciNGZj2Ta8s6LU2L0Y/edit?usp=sharing
Group 2:
https://docs.google.com/spreadsheets/d/10V-6m-trsTkiFNXn8Pp5UolX7fddoQo5Ws8WGphwCUY/edit?usp=sharing
## Troubleshooting Tips
- If you don't see your funds after 5 minutes, verify you're on the correct network
- Make sure your collateral is properly set before attempting any smart contract interactions
- Keep your recovery phrase safe - you'll need it if you need to restore your wallet

> [!Note:] 
> This tutorial uses the testnet for practice. When working with real ADA on mainnet, always double-check addresses and amounts before confirming transactions.