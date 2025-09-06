## **User Rating Token (Non-Fungible Token - NFT)**
- Purpose: Allow users to rate providers after each service.
- Minting: Minted by the user after completing a service.
- Attributes:
	- Provider ID
	- Service ID
	- Rating score
	- Timestamp
## **User Loyalty Token (Fungible Token)(Native)**
>	As a fungible token representing user loyalty, it can be implemented as a [[[[native token]]]].

>	Native tokens are well-suited for fungible tokens that have a fixed supply and are easily transferable.

- Purpose: Represent user loyalty and influence the weight of their ratings and votes.
- Minting: Minted and awarded to users based on their activity and usage of the DApp.
- As a fungible token representing user loyalty, it can be implemented as a [[native token]].
- Native tokens are well-suited for fungible tokens that have a fixed supply and are easily transferable.
- Attributes:
	- User ID
	- Loyalty score
## **Service Token (Non-Fungible Token - NFT)**
- Purpose: Represent each service uploaded by providers.
- Minting: Minted by providers when uploading a new service.
- Attributes:
	- Provider ID
	- Service ID
	- Service metadata (text description, BPMN)
	- Timestamp
## **Provider Verification Token (Non-Fungible Token - NFT)**
- Purpose: Identify and verify users as service providers.
- Minting: Minted and assigned to users who meet the criteria to become providers.
- Attributes:
	- User ID
	- Verification status
	- Timestamp
### What to check when mint this token
* for now, we just need to check that every user could only be able to have one [[Provider Verification Token]] 
## **Service Activation Token (Fungible Token)(Native)**
>	- The service activation token, used to track the activation and progress of a service, can also be implemented as a [[native token]].
>	- Native tokens can be minted and burned efficiently, making them suitable for representing service activation states.

- Purpose: Track the activation and progress of a service by a user.
- Minting: Minted when a user activates a service.
- Burning: Burned when the service is completed or terminated.

- Attributes:
	- User ID
	- Service ID
	- Activation status
	- Progress (linked to BPMN)
	- Timestamp
## **Service Result Token (Non-Fungible Token - NFT)**
- Purpose: Represent the result of a completed service.
- Minting: Minted upon service completion.
- Attributes:
	- User ID
	- Service ID
	- Result metadata
	- Timestamp

By using a combination of fungible and non-fungible tokens, you can effectively represent and track various aspects of your DApp, such as user ratings, loyalty, service uploads, provider verification, service activation, and results.

notes:
- User Rating Token: Keep as NFT, implement as [[smart contract]]
- User Loyalty Token: Keep as [[native token]]
- Service Token: Keep as NFT, implement as [[smart contract]]
- Provider Verification Token: Keep as NFT, implement as [[smart contract]]
- Service Activation Token: Change to [[smart contract]] (from native token)
- Service Result Token: Keep as NFT, implement as [[smart contract]]




