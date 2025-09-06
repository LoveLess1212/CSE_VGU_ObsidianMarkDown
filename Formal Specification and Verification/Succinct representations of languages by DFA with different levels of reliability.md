---
tags:
  - CURRENT_TOPIC
---

## Symbol 
* $L$: is the language that are considered to be processed by the DFA M
* $M$: is the DFA (processor for the language)
	* $M = (Q,\sum\limits,\delta, q_0,F)$
	* Q: finite set of states
	* $\sum\limits$: finite set of input symbol
	* $\delta$: (delta) transition function
	* $q_0$: initial state
	* F: set of final states
* $l$: size(length) of the input 
* $X_{l}(M,L)$:
	* **$X$** is the name of the function
	* $X_l$ is the function that process all the word of the language L that have size $l$
	* $M$ is the processor
	* $L$ is the language that go through the function of the processor

> sometime you will also see this notation: 
> $\sum^l$: set of all word over $\sum$ that have the length $l$
> 
### Definition 1 (Reliable function)

$Rel_{l}(M,L) = \frac{|correct_{l}(M,L)|}{|\sum|^{l}}= 1 - \frac{|incorrect_{l}{M,L}|}{|\sum|^{l}}$
### Definition 2 (Convergent-reliability with reliable function)

#### Convergent-reliability
>the reliability of "the software system that is under consideration" **increases** over the length of the input


$\lim_{l->\infty}{Rel_{l}(M,L)} =1$
$\leftrightarrow \lim_{l->\infty}Rel_{l}(M,L) = \lim_{l->\infty}\frac{|correct_{l}(M,L)|}{|\sum|^{l}}= 1 - \lim_{l->\infty}\frac{|incorrect_{l}{M,L}|}{|\sum|^{l}} = 1$  

#### Slender-reliability
>the situation that only a constant number of inputs is incorrectly processed in the system at any point in time
>aka. kể cả nó có sai, thì không cần biết cái input nó dài bao nhiêu, chỉ có đúng tối đa n số bị xử lý sai trong 1 thời điểm

for every $l>1$ and N is a constant, we have ${|incorrect_{l}(M,L)|} \leq N$   


number of word of each length could be bounded by a function

### Definition 3 (FD-Reliability)
>aka. finite prefix deviation
>requires the software system to work fully reliably from some given point in time on.

Let M be a DFA and $L \subseteq \Sigma^*$ a language. We say that M is a finite prefix Deviation (FD) description of L if there exist a $l_0>0$ that for all $l \geq l_0$ we have $|incorrect_{l}(M,L)|=0$
### Definition 4 (lifeness-reliability)
>regardless of the state that the system is in, there always exists and input sequence such that the system will work correctly.

Let M be a DFA and $L \subseteq \Sigma^*$ a language. We say that M is a liveness-reliable description of L if, for all $x \in \Sigma^{*}$, there is a $y \in \Sigma^*$ such that $xy \in correct(M,L)$ 

### Def 5 (Strong lifeness-reliability )
>requires the system to always work correctly "once in a while", regardless of given input
>không cần biết input là gì, khi M xử lý L nó sẽ luôn luôn chạy (tới một mức độ nào đó, vào 1 lúc nào đó)

Let M be a DFA and $L \subseteq \Sigma^*$ a language. We say that M is a strong liveness-reliable description of L if there is a $c>0$ such that for all $x \in \Sigma^*$ and for all $y \in \Sigma^*$ with $|y|>c$ there is a partition $y= y_{1}y_{2}$ such that $xy_{1}\in correct(M,L)$ 
aka. $concat(x,y_1)$ luôn đúng
---
* the concept
* should convey the idea --
* Q1:
	* you need to see if you can fit inside the presentation
	* the paper is actually in theoretical CS journal  
	* if you can convey if you do not go into the detali it ok,
	* but be careful the time

Lemma2: any DFA M FD-reliably describing $H_n$ has at least n states  
Lemma 1: There is a DFA M with three states that slender-reliably describe language H, with length n and $rel(M,H_{n)}= 1-\frac{1}{3^n}$

---
We are all know that, software reliability: the ability of a software system or component to perform its required functions under stated conditions for a specified period of time.

As the consequences of a failure of a specific software component can range anywhere from unpleasant to disastrous, it is an area of tremendous practical interest for computer systems in public or private use

Follow the previous paper's approach, any DFA can be used as a representation for any languages, and reliability turns into a resource that can be quantified, much like ambiguity or non-determinism.

By allowing different "levels" of reliability in our DFA models, as defined qualitatively in the paper, we may be able to significantly reduce the number of states needed compared to a perfectly reliable model. Something as simple as a "finite prefix deviation reliable" or "slender reliable" DFA could achieve major reductions.

Before this work, several research have been done to 
*  Proposed the Quantitative measure for reliability of a system.
	* It show that: more reliable descriptions required more states in general
* Introduce Slender reliability - convergence reliability
* studied DFA approximations that accept languages up to a certain length.
But the problem is that  they had not fully formalized qualitative reliability or proven theorems relating the concepts. We are all know that *Without formal proofs of relationships and tradeoffs, the prior definitions/notions would remain just intuitive concepts!*

So the goal of the paper is to 
- Establishes formal relationships between notions and proves unbounded gaps in complexity between different reliability levels.
- Explain reliability as a computational resource that can be exchanged for conciseness
this paper is done in the spirit of classical descriptional complexity analysis.

To understand more about the concept of the paper, we could consider a narrative:
"
Suppose we are software engineers working on a critical system that controls air traffic at a major airport. Reliability is of the utmost importance.

When designing the core control algorithms that direct planes for takeoff and landing, we model the system using deterministic finite automata (DFAs). This allows us to formalize the behavior and check for errors mathematically. Our goal is to create DFAs that represent the required language (set of valid behaviors) *with as high a level of reliability as possible with a limited resource.*
"

We are already model - that we need to create a DFA that accept $K_{n}= (a+b)^{+}+ c^n$
with n <= 100
now, through previous paper, we know that **Need at least 100 + 3 stages to achieve “exact reliability”**

To solve this problem, we could apply some tradeoffs - definition in the paper to make the DFA achieve *acceptable reliability* with significant reduce in number of stages 

**

Where:

- Q: a finite set of states
    
- : a finite set of input symbols
    
- : (delta) transition function
    
- q0: initial state
    
- F: set of final states
    

Sssss

Correctness - incorrectness 

## Convergent reliability

## Slender reliability

## FD-reliability

## Lifeness-reliability

## Strong lifeness-reliability

**