---
template: reveal.html
search:
  exclude: true
---
# Lógica aplicada à Matemática

---

![Tabuleiro](/01-conjuntos/img/aula00-tabuleiro.jpg)

--

![Damas](/01-conjuntos/img/aula00-damas.jpg)

--

![Xadrez](/01-conjuntos/img/aula00-xadrez.jpg)

---

Matemática é como um jogo: você estabelece um conjunto de regras e joga conforme elas. 

Mudando-se as regras, você tem um novo jogo - ou uma nova Matemática.

--

## Geometria Euclidiana

> **Axioma das Paralelas**: dados um ponto e uma reta que não passa nesse ponto, `existe uma única` reta paralela à reta dada que passa pelo ponto dado.


--

## Geometrias Não-Euclidianas

Se modificarmos o _Axioma das Paralelas_, damos origens a outros tipos de geometrias.

--

## Geometria Esférica

> **Axioma das Paralelas**: dados um ponto e uma reta que não passa nesse ponto, `não existe` reta paralela à reta dada que passa pelo ponto dado.

--


## Geometria Hiperbólica

> **Axioma das Paralelas**: dados um ponto e uma reta que não passa nesse ponto, `existem infinitas` retas paralelas à reta dada que passa pelo ponto dado.

--

![Geometrias](/01-conjuntos/img/aula00-geometrias.jpeg)


---

## Conceitos iniciais

**Proposições**
: São afirmações as quais podemos atribuir um valor verdadeiro ou falso, chamado de _valor-verdade_.


--

_Exemplos_
 
- A lua é um planeta
- O céu é azul
- Matemática é a melhor disciplina

_Contraexemplos_

- Você vai no cinema amanhã?
- Que horas passa o próximo ônibus? 


---


**Conectivos**
: São operadores lógicos que usamos para aglutinar proposições.


_Exemplos_

- e
- ou
- não
- se ... então ...
- se e somente se


--

 
_Exemplos_

- A lua é cinza e a lua é cheia de crateras
- O número 2 é primo ou o número 17 é par
- Se um número é primo então esse número é ímpar


---

 
**Proposições atômicas**
: São proposições que não podem ser divididas em proposições menores.


---


# Cálculos das proposições

Para simplificar, utilizamos letras para representar proposições atômicas, geralmente $p$, $q$, $r$ e $s$


--


## Operações com proposições

Quando aglutinamos proposições usando conectivos, podemos calcular o valor-verdade da nova proposição formada usando os valores das proposições atômicas. 


---


### Negação: Operador `não`

A negação, também chamada de operador `não`, é denotada pelo símbolo $\sim$ ou $\neg$ 

_Exemplo_

- $p$ = "o número 2 é ímpar"
- $\sim p$ =  "o número 2 não é ímpar"


--


#### Tabela-verdade da negação

|$p$|$\sim p$|
| --- | :---: | 
|  V  |  F  |
|  F  |  V  | 

> A negação inverte o valor-verdade da proposição.


---


### Conjunção: Operador `e`

A conjunção, também chamada de operador `e`, é denotada pelo símbolo $\wedge$ 

_Exemplo_

- $p$ = "A lua é cinza"
- $q$ = "A lua é cheia de crateras" 
- $p\wedge q$ = "A lua é cinza e a lua é cheia de crateras". 


--


#### Tabela-verdade da conjunção

|$p$|$q$|$p\wedge q$ |
| --- | --- | :----------: |
|  V  |  V  |  <spam class="fragment highlight-green">V</spam> |
|  V  |  F  |  F |
|  F  |  V  |  F |
|  F  |  F  |  F |


<blockquote class="fragment fade-up"  >
$p\wedge q$ será verdadeira quando $p$ e $q$ forem verdadeiras. Caso contrário, a conjunção será falsa.
</blockquote>

 

---


### Disjunção: Operador `ou`

A disjunção, também chamada de operador `ou`, é denotada pelo símbolo $\vee$

_Exemplo_

- $p$ = "o número 2 é primo" 
- $q$ = "número 17 é par"
- $p\vee q$ = "o número 2 é primo ou o número 17 é par"


--


#### Tabela-verdade da disjunção

|$p$|$q$|$p\vee q$
| --- | --- | :----------: |
|  V  |  V  |  V |
|  V  |  F  |  V |
|  F  |  V  |  V |
|  F  |  F  |  <spam class="fragment highlight-red">F</spam> |

<blockquote class="fragment fade-up">
$p\vee q$ só será falso quando ambas $p$ e $q$ forem falsas. Caso contrário, a disjução é verdadeira.
</blockquote> 


---


### Condicional: `se então`

O operador condicional, é denotado por $\rightarrow$ e em linguagem coloquial é construído com a frase "se [...] então [...]". 


--


_Exemplo_

- $p$ = "ela dança" 
- $q$ = "eu danço"
- $p\rightarrow q $ = "se ela dança então eu danço"


--


Na construção $p\rightarrow q$, $p$ é chamada _condição necessária_  e $q$ é chamada _condição suficiente_.


--


#### Tabela-verdade da condicional

|$p$|$q$|$p\rightarrow q$
| --- | --- | :----------: |
|  V  |  V  |  V |
|  V  |  F  |  <spam class="fragment highlight-red">F</spam> |
|  F  |  V  |  V |
|  F  |  F  |  V |

<div class="r-stack">
<blockquote class="fragment fade-in-then-out	   "  >
A condicional $p\rightarrow q$ só será falsa caso $p$ seja verdadeira e $q$ seja falsa. Caso contrário, a condicional é verdadeira.
</blockquote>
<blockquote class="fragment fade-up">
Gosto de usar a frase "A verdade não pode levar a uma mentira" para memorizar essa regra.
</blockquote>
</div>


---


### Bicondicional: `se e somente se`

O operador bicondicional, denotado por $\leftrightarrow$ e em linguagem coloquial é construído com a frase "[...] se o somente se [...]"

_Exemplo_

- $p$ = "eu vou ao parque" 
- $q$ = "está fazendo sol"
- $p\leftrightarrow q$ = "eu vou ao parque se e somente se está fazendo sol"


--


#### Tabela-verdade da condicional

|$p$|$q$|$p\leftrightarrow q$
| --- | --- | :----------: |
|  V  |  V  |  V |
|  V  |  F  |  F |
|  F  |  V  |  F |
|  F  |  F  |  V |


<blockquote class="fragment fade-up">
A bicondicional $p\leftrightarrow q$ é verdadeira quando os valores de $p$ e $q$ são iguais. Caso contrário, a bicondicional é falsa.
</blockquote>


---


# Contradição e Tautologia


---

> Uma **contradição** é uma proposição composta que possui o valor-verdade sempre falso, independente do valor-verdade das proposições atômicas que o constituem.  


_Exemplo_

 $$p \wedge \sim p$$


---


> Uma **tautologia** é uma proposição composta que possui o valor-verdade sempre verdadeiro, independente do valor-verdade das proposições atômicas que o constituem.

_Exemplo_
$$ p \vee \sim p$$


---


# Validade de argumentos


--


Um _argumento_ é composto de uma lista de proposiçoes $p_1, p_2, \ldots, p_n$ que serão chamadas de _premissas_, e uma proposiçao _q_ chamada de _conclusão_. 


--


> Dizemos que o argumento é _válido_ se, toda vez que as premissas forem todas verdadeiras, a conclusão também é verdadeira. 


--


Quando o argumento é válido, denotamos por 
$$ p_1, p_2, \ldots, p_n \models q$$


--

_Exemplo 1_

 - $p_1 $ = "se choveu hoje então a rua está molhada"
- $p_2 $ = "a rua não está molhada"
- $q $ = "não choveu hoje"

O argumento acima é válido.

--

- $c$: Choveu hoje
- $m$: A rua está molhada

Assim, podemos reescrever o argumento acima como

- $p_1 = c \rightarrow m$
- $p_2 = \sim m$
- $q = \sim c$

--


|  $c \rightarrow m$  |  $\sim m$  |  $\sim c$  |
| ------------------- | ---------- | ---------- |
|          V          |      F     |      F     |
|          F          |      V     |      F     |
|          V          |      F     |      V     |
|        **V**        |    **V**   |    **V**   |


--


_Exemplo 2_

- $p_1$ = "se choveu hoje então a rua está molhada"
- $p_3$ = "não choveu hoje"
- $q_2$ = "a rua não está molhada"

O argumento acima é inválido.


---


[Voltar ao conteúdo](/01-conjuntos/aula00) 