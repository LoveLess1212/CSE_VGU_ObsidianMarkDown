---
tags:
  - BLOCKCHAIN
  - Thesis
---

1. Hey Team - Is there a way I can kee the [[Wallet]] connected even after the user refreshes the page? It's a bit annoying if the user has to keep connecting it.
    
    After user gives the permission, you can connect whenever you want. One solution is to store the name of the [[wallet]] in local storage, make an initial check for this cache, and attempt connection if the value was present.
    
2. 
After user gives the permission, you can connect whenever you want. One solution is to store the name of the [[wallet]] in local storage, make an initial check for this cache, and attempt connection if the value was present.
### SevenBC _—_ 28/08/2023 11:45

Hmm, How do I connect on page load?

1. keyanm _—_ 28/08/2023 12:24
If you store the name of the [[wallet]] user had connected to, you can grab it on load (`localStorage.getItem()`), and "connect" (i.e. instantiate a `BrowserWallet`) using that name:
![Hình ảnh](https://media.discordapp.net/attachments/907224762437210132/1145589624870281246/image.png?ex=66fc303a&is=66fadeba&hm=371cd65c371d9eb8380a82f691a0f9c5599a5054f6a21ed69c4589496f5b5fd3&=&format=webp&quality=lossless&width=593&height=77)
    
Hmm, How do I connect on page load?

hazryder _—_ 28/08/2023 14:30

Use the appropriate hook in whatever framework you’re working in. If you’re building in React/Next, you can utilise a useEffect hook to trigger on page load
    
6. 
    ![Hình ảnh](https://media.discordapp.net/attachments/907224762437210132/1145622212032856094/image.png?ex=66fc4e93&is=66fafd13&hm=e2f18e5936f38e21a4f38a3f26bd19017fa9f00d03fca88aac9d6340e678c5e9&=&format=webp&quality=lossless&width=687&height=206)
    
7. Don't forget the required includes: `import { useWallet } from '@meshsdk/react'` `const { connected, connect } = useWallet()`
    
8. 
    
    And just to clarify incase you're unfamiliar with how `useEffect` is working in this context, if you provide an empty Dependency List as the second param (the empty [] array), the hook is called just-once on page load
    
    1
    
9. 
    
    ### SevenBC _—_ 28/08/2023 21:30
    
    Bro, i love you guys @hazryder ... seriously
    
10. 
    
    amazing work
    
11. SevenBC _—_ 28/08/2023 22:40
    
    hmm, however, BrowserWallet.enable & connect(walletName) aren't working for me
    
12. 
    
    I have localStorage working