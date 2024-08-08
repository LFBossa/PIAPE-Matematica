---
template: reveal.html
search:
  exclude: true
---
# Lógica aplicada à Matemática

<slide/>

## Conceitos iniciais

**Proposições**
: São afirmações as quais podemos atribuir um valor verdadeiro ou falso, chamado de _valor-verdade_.

<subslide/>
_Exemplos_
 
- A lua é um planeta
- O céu é azul
- Matemática é a melhor disciplina

_Contraexemplos_

- Você vai no cinema amanhã?
- Que horas passa o próximo ônibus? 

<slide/>

**Conectivos**
: São operadores lógicos que usamos para aglutinar proposições.


_Exemplos_

- e
- ou
- não
- se ... então ...
- se e somente se

<subslide/>
 
_Exemplos_

- A lua é cinza e a lua é cheia de crateras
- O número 2 é primo ou o número 17 é par
- Se um número é primo então esse número é ímpar

<slide/>
 
**Proposições atômicas**
: São proposições que não podem ser divididas em proposições menores.

<slide/>

# Cálculos das proposições

Para simplificar, utilizamos letras para representar proposições atômicas, geralmente $p$, $q$, $r$ e $s$

<subslide/>

## Operações com proposições

Quando aglutinamos proposições usando conectivos, podemos calcular o valor-verdade da nova proposição formada usando os valores das proposições atômicas. 

<slide/>

### Negação: Operador `não`

A negação, também chamada de operador `não`, é denotada pelo símbolo $\sim$ ou $\neg$ 

_Exemplo_

- $p$ = "o número 2 é ímpar"
- $\sim p$ =  "o número 2 não é ímpar"

<subslide/>

#### Tabela-verdade da negação

|$p$|$\sim p$|
| --- | :---: | 
|  V  |  F  |
|  F  |  V  | 

> A negação inverte o valor-verdade da proposição.

<slide/>

### Conjunção: Operador `e`

A conjunção, também chamada de operador `e`, é denotada pelo símbolo $\wedge$ 

_Exemplo_

- $p$ = "A lua é cinza"
- $q$ = "A lua é cheia de crateras" 
- $p\wedge q$ = "A lua é cinza e a lua é cheia de crateras". 

<subslide/>

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

 
<slide/>

### Disjunção: Operador `ou`

A disjunção, também chamada de operador `ou`, é denotada pelo símbolo $\vee$

_Exemplo_

- $p$ = "o número 2 é primo" 
- $q$ = "número 17 é par"
- $p\vee q$ = "o número 2 é primo ou o número 17 é par"

<subslide/>

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

<slide/>

### Condicional: `se então`

O operador condicional, é denotado por $\rightarrow$ e em linguagem coloquial é construído com a frase "se [...] então [...]". 

<subslide/>

_Exemplo_

- $p$ = "ela dança" 
- $q$ = "eu danço"
- $p\rightarrow q $ = "se ela dança então eu danço"

<subslide/>

Na construção $p\rightarrow q$, $p$ é chamada _condição necessária_  e $q$ é chamada _condição suficiente_.

<subslide/>

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

<slide/>

### Bicondicional: `se e somente se`

O operador bicondicional, denotado por $\leftrightarrow$ e em linguagem coloquial é construído com a frase "[...] se o somente se [...]"

_Exemplo_

- $p$ = "eu vou ao parque" 
- $q$ = "está fazendo sol"
- $p\leftrightarrow q$ = "eu vou ao parque se e somente se está fazendo sol"

<subslide/>

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

<slide/>

# Contradição e Tautologia

<slide/>
> Uma **contradição** é uma proposição composta que possui o valor-verdade sempre falso, independente do valor-verdade das proposições atômicas que o constituem.  


_Exemplo_

 $$p \wedge \sim p$$

<slide/>

> Uma **tautologia** é uma proposição composta que possui o valor-verdade sempre verdadeiro, independente do valor-verdade das proposições atômicas que o constituem.

_Exemplo_
$$ p \vee \sim p$$

<slide/>

# Validade de argumentos

<subslide/>

Um _argumento_ é composto de uma lista de proposiçoes $p_1, p_2, \ldots, p_n$ que serão chamadas de _premissas_, e uma proposiçao _q_ chamada de _conclusão_. 

<subslide/>

> Dizemos que o argumento é _válido_ se, toda vez que as premissas forem todas verdadeiras, a conclusão também é verdadeira. 

<subslide/>

Quando o argumento é válido, denotamos por 
$$ p_1, p_2, \ldots, p_n \models q$$

<subslide/>

_Exemplo 1_

 - $p_1 $ = "se choveu hoje então a rua está molhada"
- $p_2 $ = "a rua não está molhada"
- $q $ = "não choveu hoje"

O argumento acima é válido.

<subslide/>

_Exemplo 2_

- $p_1$ = "se choveu hoje então a rua está molhada"
- $p_3$ = "não choveu hoje"
- $q_2$ = "a rua não está molhada"

O argumento acima é inválido.

<slide/>

# Lógica de predicados

<subslide/>

Nem toda lógica pode ser descrita usando proposições. As vezes, queremos fazer afirmações sobre elementos de conjuntos. Um _predicado_ denota uma relação entre objetos de um determinado contexto de discurso. Esse contexto de discurso é um conjunto no qual os objetos existem. 

<subslide/>

_Exemplos_

- Sócrates é mortal
- O número 2 é primo
- Um pássaro voa

<subslide/>

Nesse caso, simbolizamos os predicados com letras maiúsculas, e deixamos uma _variável livre_, abaixo denotada por $x$

- M(x) = x é mortal
- P(x) = x é primo
- V(x) = x voa

<subslide/>

As frases anteriores se traduzem como

- M(Sócrates)
- P(2)
- V(pássaro)

<slide/>

## Quantificadores

<slide/> 

Quando estamos falando de predicados, geralmente queremos fazer afirmações do tipo 
- Existe um elemento com tal propriedade
- Todo elemento satisfaz essa propriedade

Para isso, usamos os _quantificadores_

<subslide/>

### Existe

A seguinte construção
$$\exists x, P(x)$$
é lida como 
> existe um x tal que P(x)

<subslide/>

Como P(x) significa "x é primo", a construção se traduz como 

> Existe um x que é primo

<subslide/>

### Para todo

A construção
$$\forall x, M(x)$$
é lida como 
> para todo x, M(x)

<subslide/>

Como M(x) significa "x é mortal", a construção se traduz como
> Todo x é mortal 