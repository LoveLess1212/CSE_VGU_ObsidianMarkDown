---
tags:
  - BLOCKCHAIN
  - CES
  - Thesis
---
```json
{
  "name": "Provider Verification Token",
  "description": "This token identifies and verifies users as service providers in the DApp.",
  "attributes": [
    {
      "trait_type": "Timestamp",
      "value": "unix_timestamp"
    },
    {
      "trait_type": "Staked Amount",
      "value": "number"
    },
    {
      "trait_type": "Verification Date",
      "display_type": "date",
      "value": "unix_timestamp"
    }
  ]
}
```

who can mint it?, what can they do to be able to mint it ?
- Everyone could have only one of it
- 
chèn address của người mint vào trong NFT ?? hoặc là tạo 1 riêng 1 app [[wallet]] để ký vào [[Smart contract]] khi mint cái NFT này -> đảm bảo là người dùng chỉ có thể mint được cái NFT dạng này ở trên APP của mình 

lúc tạo - list  service NFT thì [[smart contract]] sẽ kiểm tra xem cái NFT đấy có được cái(public address) của ví của mình ký hay không ?

lúc mua, đảm bảo người mua có NFT Provider(chắc là check offchain :V ) và cái NFT service mà mình mua sẽ có chữ ký của APP(off chain) 