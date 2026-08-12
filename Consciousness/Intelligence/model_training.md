**Training Data**  
**Input**                                                  |   **Output**   
START I worked very hard. I am tired now. END              | START I must go to sleep. END   <br />
START I worked very hard today.  END                       | START I must sleep now. END     <br />
START I worked hard today. END                             | START Therefore, I am going to sleep. END <br />

**Data Prepration** <br />

**Data Cleaning** <br />

**Removal of Punctutaion**  <br />
**ADD [start] and [end] TOKENS**  <br />

**Input**                                                  |   **Output** <br />
START I worked very hard I am tired now END                | START I must go to sleep END  <br />
START I worked very hard today END                         | START I must sleep now END    <br />
START I worked hard today END                              | START Therefore, I am going to sleep END <br />

**TOKENIZATION**  

*TOKENIZATION METHOD*  

**WORD TOKENIZATION**

START I worked very hard I am tired now END [10 WORDS \ TOKENS]

1     0 .............................. 0.2
1     0 ------------------------------ 3.0
0     0                         ...... 0.01
0     0.2                          ... 0.23
0     0.1                           .. 0.001
.
.
.
...[N X M]

N = 10
M = 500

S V D =  U(NXP) SIG(PxP) V (PXM)  ::>   U SIG V   
P = 3

10 x 3  + 3 x 3 + 3 X 500

INSTEAD TRY:  
A        AT           AAT
[N X M] [M X N]   =   N X N    = P (N X K <<N ) D PT (K X N)

**ORDER** and **CONTEXT** <br />

**FIND COSINE SIMILARITY** <br />
[P1 P2 P3 P4 P5 P5 .....]  

**CONTEXT**: RELEVANCE WEIGHT W1 for P1 = COS(P1,P2) + COS(P1, P3) + COS(P1, P4), COS(P1, P5) ..... / SUM(....) <br />
[W1P1 W2P2 .....] = [WT1 PT1 ...] <br />
SAY K = 1 <br />

INPUTS: <br />

P (N x 2) D (N X 1) ::: T(L x 2) DT(L X 1)

**OBJECTIVE** <br />

MIN (SQRT(P-T) + SQRT(DT-T)) <br />

MAAPPING: HIGHER W :: BIGGER EIGEN VAL  <br />

**INPUT** ==> DEEP NEURAL NETWORK WITH RESIDUAL CONNECTION ==> OUTPUT          <br />
3N (N ~ 20-30) ==>  DL (0.75)   DL   DL (0.25)   DL  DL (0.75)    ==> OUTPUT LAYER (LINEAR) => L X 2 + L x 1 = 3 L (L ~ 10) <br />

**MAP OUTPUT TO TEXT**  <br />

P(L x 2) D(L x 1)P(2 x L) = TARGET (L X L) <br />

OUTPUT -> PREDICTION: START [SENTENCE/IDEA]



