# O corpo ordenado dos reais

Podemos chamar o conjunto dos números reais $\mathbb{R}$ de um _corpo ordenado_. Esse conjunto é um _corpo_ pois, juntamente com as operações de adição  $+$ e multiplicação $\cdot$ satisfaz as seguintes propriedades:


**[A1]** a adição é associativa

$$(a+b) + c = a + (b+c)$$

**[A2]** a adição é comutativa

$$a+b = b+a$$

**[A3]** existe o elemento neutro da adição

$$ a + 0 = a $$

**[A4]** existência do oposto para a adição: para todo $a$ existe um $-a$ que satisfaz

$$ a + (-a) = 0 $$

**[M1]** a multiplicação é associativa

$$ (a\cdot b)\cdot c = a\cdot (b\cdot c) $$


**[M2]** a multiplicação é comutativa

$$a\cdot b = b\cdot a$$

**[M3]** existe o elemento neutro da multiplicação

$$ a\cdot 1 = a $$

**[M4]** existência do inverso para a multiplicação:  para todo $a$ existe um $a^{-1}$ que satisfaz


$$ a\cdot a^{-1} = 1 $$


**[D]** propriedade distributiva da multiplicação com relação a adição

$$ a\cdot (b+c) = a\cdot b + a\cdot c $$
 


Ele é um corpo ordenado, pois juntamente com a relação de ordem $\le$, temos as seguintes propriedades

**[OA]** A adição preserva a ordem: para quaisquer $a,b,c\in\mathbb{R}$ vale que 
$$a\le b \quad \Rightarrow \quad a+c \le b +c$$

**[OM]** A multiplicação preserva a ordem: para quaisquer $a,b\in\mathbb{R}$

$$0\le a,b  \quad \Rightarrow \quad 0 \le a\cdot b$$

## Módulo

O _módulo_ de um número real pode ser interpretado como
- a sua distândia até a origem
- seu valor sem o sinal

Ele é representado por duas barras verticais ao redor do número, $|a|$. 

**Exemplos**

- $|7| = 7$
- $|-3| = 3$
- $|0| = 0$

## Intervalos e módulos

Podemos representar um subconjunto dos reais com uma inequação de módulos. Essas inequações aparecerão frequentemente no estudo de limites.

**Exemplo 1**

Sendo $L$ um real positivo, temos inequações modulares da seguinte maneira

$$|x|\le L$$

Interpretando essa desigualdade, significa dizer que a distância de $x$ até a origem é no máximo $L$. Desse modo, $x$ tem que estar no intervalo $[-L,L]$.
Outra maneira de escrever isso é indicar
$$|x|\le L \Leftrightarrow -L \le x \le L$$

**Exemplo 2**

Sendo $M$ um real positivo, temos inequações modulares da seguinte maneira


$$|x| \ge M$$

Interpretando essa desigualdade, significa dizer que a distância de $x$ até a origem é no mínimo $M$.  Então $x$ tem que estar afastado da origem, podendo estar no intervalo $[M,+\infty[$ ou no intervalo $]-\infty,-M]$. 
Outra maneira de escrever isso é indicar
$$|x| \ge M \Leftrightarrow  x \ge M \text{ ou } x\le -M$$


**Exemplo 3**

Podemos incrementar o Exemplo 1. Considere $L=5$. A inequação abaixo 
$$|x-4| < 5$$

Pode ser reescrita como 
$$ -5 < x-4 < 5$$
Somando 4 em todos os termos, temos
$$ -5 + 4 < x - 4 + 4 < 5 + 4$$
$$ - 1 < x < 9$$
Assim, o intervalo solução é $]-1,9[$.

**Exemplo 4**

Podemos incrementar o Exemplo 2. Considere $M=6$. A inequação abaixo 
$$|x-2| \ge 6$$

Pode ser reescrita como 
$$ x- 2 > 6  \text{ ou } x - 2 < -6$$
Somando 2 em todos os termos, temos

$$ x- 2 + 2 > 6 + 2  \text{ ou } x - 2 + 2 < -6 + 2$$
$$ x > 8  \text{ ou } x < -4$$
Assim, o intervalo solução é $]-\infty,-4[ \ \cup \ ]8,+\infty[$.