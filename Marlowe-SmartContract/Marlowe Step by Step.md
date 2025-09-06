---
tags:
  - BLOCKCHAIN
---
[[Marlowe]] has six ways of building contracts. Five of these -- `Pay`,`let`,`If`,`When` and `Asssert` -- Build a complex contract from simpler contracts, and the sixth, `Close` is a simple contract. At each step of execution, as well as returning a new state and continuation contract, it is possible that effects -- payments -- and warnings can be generated too.

In explaining these contracts we will also explain [[Marlowe]] values, observations and actions, which are used to supply external information and inputs to a running contract to control how it will elvove.

# Pay
A payment contract `Pay a p t cont` will make a payment of value `V` of token `t` from the account `a` to a payee `p`, which will be one of the contract participants or another account in the contract. Warnings will be generated if the value `v` is negative, of if there is not enough in the account to make the payment in full (even if there are positive balances of other tokens in the account). In the latter case, a partial payment, a partial payment (of all the money available) is made. The continuation contract is the one given in the contract: `cont`.
# Close
A contract `Close` provides for the contract to be closed (or terminated). The only action that it performs is to provide refunds to the owners of accounts that contain a positive balance. This is performed one account per step, but all accounts will be refunded in a single transaction.

Before discussing other forms of contracts, we need to describe values, observations and actions.
# Values, Observations and actions
**Values** include some quantities that change with time, including "the current slot number", "the current balance of some token in an account", and any choices that have already been made; we call these volatile values. Values can also be combined using addition, subtraction, negation, multiplication, and division, and can be conditional on an observation. Even though they are supported by [[Marlowe]], the use of multiplication and division may render the process of static analysis intracttable.

**Observations** are boolean values derived by comparing values, and can be combined using the standard Boolean operators. It is also possible to observe whether any choice has been made (for a particular identified choice).

Observations will have a value at every step of execution. On the other hand, actions happen at particular points during execution. As noted earlier, actions can be:
* Depositing money
* making a choice between various alternatives, including an oracle value, or
* notifying an external value of some kind.
# Oracles
Oracles are begin developed for the Cardano [[blockchain]] in general, and will be available for use within [[Marlowe]] on Cardano. In the meantime, we have introduced and oracle prototype, which is implemented in the [[Marlowe]] Playuground.

We model Oracles as choices that are made by a participant with a specific Oracle role: "kraken"

If a role in a contract is `kraken`, and that role makes a choice such as `dir-adausd` the, in the playground simulation, this choice will be prefilled, based on data from Crytowat.ch, with the current value of the direct ADA/USD conversion rate. You can find all supported currency pairs here:

[https://api.cryptowat.ch/markets/kraken](https://api.cryptowat.ch/markets/kraken)

It is also possible to obtain the inverstate rates of currency pairs listed by adding the prefix `inv-` instead. For example,  `inv-adausd` would return the value of the USD/ADA conversion rate.

Note, that we support only whole numbers as choice inputs. How then do we use current ADA/USA price, which might be $0.098924? We simple multiply the price by 10^8, so the price would appear as 9892400. You can use `DivValue` with the resulting value after doing your calculations

# If 
The conditional `If obs cont1 cont2` will continue as `cont1` or `cont2`, depending on the Boolean value of the observation `obs` when this construct is executed.
# When 
This is the most complex contructor for contracts, with the form `When cases timeout cont`