# Conjuntos Numéricos

## Números naturais

São os números utilizados para contagem. Representamos pelo símbolo $\mathbb{N}$. 

Existe muito debate se o número $0$ é natural ou não, por conta de toda a história envolvendo a criação desse número. Dependendo do autor, ele inclui ou não o zero em $\mathbb{N}$.
Eu sou do time $0\in\mathbb{N}$. Assim
$$
\mathbb{N} = \{0,1,2,3,4,5,\ldots\}
$$

### Operações

Nos naturais, estão bem definidas as operações de adição $+$ e multiplicação $\cdot$. O que significa estar bem definida? Significa que ao somar ou multiplicar dois números naturais, sempre obtemos um número natural. 

Essas operações satisfazem as seguintes propriedades: para quaisquer $a,b,c\in\mathbb{N}$

**[A1]** a adição é associativa

$$ (a+b) + c = a + (b+c) $$

**[A2]** a adição é comutativa

$$ a+b = b+a $$

**[A3]** existe o elemento neutro da adição

$$ a + 0 = a $$

**[M1]** a multiplicação é associativa

$$ (a\cdot b)\cdot c = a\cdot (b\cdot c) $$

**[M2]** a multiplicação é comutativa

$$ a\cdot b = b\cdot a $$

**[M3]** existe o elemento neutro da multiplicação

$$ a\cdot 1 = a $$


**[D]** propriedade distributiva da multiplicação com relação a adição

$$ a\cdot (b+c) = a\cdot b + a\cdot c $$


Note que a operação de subtração $-$ não está bem definida em $\mathbb{N}$: não podemos subtrair 10 de 5 e obtermos um número natural. 

Para que a subtração possa ser definida, temos que inventar um novo conjunto numérico.

## Números inteiros

Os números inteiros são construídos pegando os números naturais e acrescentando os números negativos. Representamos pelo símbolo $\mathbb{Z}$.
$$
\mathbb{Z} = \{ \ldots, -3,-2,-1,0,1,2,3,\ldots\}
$$

Note que $\mathbb{N}\subseteq\mathbb{Z}$.
### Operações

Nos números inteiros, as operações de adição, subtração e multiplicação estão bem definidas. 

Além de todas as propriedades [A1] até [A3], [M1] até [M3] e [D], a adição possui mais uma propriedade em $\mathbb{Z}$

**[A4]** existência do oposto para a adição: para todo $a$ existe um $-a$ que satisfaz

$$ a + (-a) = 0 $$

### Divisibilidade

Dizemos que um inteiro $a$ _divide_ $b$ se existe algum inteiro $c$ que quando multiplicado por $a$ nos dá $b$, ou seja,
$$
b = a\cdot c
$$
Nesse caso, utilizamos a notação $a\mid b$. Quando $a$ divide $b$, dizemos que 
- $a$ é um _divisor_ de $b$
- $b$ é _divisível_ por $a$
- $b$ é _múltiplo_ de $a$


**Exemplos**
- $5 \mid 10$, pois $10 = 5\cdot 2$.
- $(-3) \mid 27$, pois $27 = (-3)\cdot (-9)$
- $2\mid 0$ pois $0 = 2\cdot 0$

Quando $a$ divide $b$, o número $c$ é único e podemos definir 

$$  b\div a = c $$

Mas note que a divisão exata nem sempre é possível em $\mathbb{Z}$: não podemos dividir $15$ por $4$ por exemplo. 

### Inteiros e a reta

Numa reta horizontal, fixamos o $0$ como origem. Dada uma unidade de medida $u$, fazemos marcações à direita de $u$ em $u$ unidades para representar os números positivos, e à esquerda para representar os negativos.

![A reta dos inteiros](./img/aula03-img01.svg)

## Números racionais

Os números racionais foram criados para fazer a operação de divisão ser possível para quaisquer inteiros. Nos racionais, faz sentido dividir $15$ por $4$. Denotamos esse conjunto por $\mathbb{Q}$

Para definir $\mathbb{Q}$, vamos definir uma _fração_: é um par de números inteiros $a$, $b$, com $b\neq 0$ e denotada por $$\frac{a}{b}$$
com $a$ sendo o _numerador_ e $b$ sendo o _denominador_. 

Duas frações são iguais se a multiplicação cruzada dos numeradores pelos denominadores for igual

$$ \frac{a}{b} = \frac{c}{d}\quad \Leftrightarrow \quad a\cdot d = b\cdot c $$

Definimos a adição de duas frações da seguinte forma

$$ \frac{a}{b} + \frac{c}{d} = \frac{a\cdot d + b\cdot c }{b\cdot d} $$

Definimos a multiplicação de duas frações da seguinte forma

$$ \frac{a}{b} \cdot  \frac{c}{d} = \frac{a\cdot c }{b\cdot d} $$

As operações acima definidas satisfazem todas as propriedades [A1] até [A4], [M1] até [M3] e [D]. Além disso, temos mais uma propriedade 

**[M4]** existência do inverso para a multiplicação: para toda fração $\frac{a}{b}$ existe uma fração $\frac{b}{a}$ que satisfaz

$$ \frac{a}{b}\cdot \frac{b}{a} = 1 $$

Por causa da propriedade [M4], podemos definir a divisão em $\mathbb{Q}$ como

$$ \frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \cdot  \frac{d}{c}  $$

Note que para qualquer inteiro $a\in\mathbb{Z}$ a fração $\frac{a}{1}$ se comporta exatamente como $a$. Com isso, podemos dizer que $\mathbb{Z}\subseteq\mathbb{Q}$.

### Representação decimal

Quando fazemos a "divisão na chave", obtemos a representação decimal da fração.

**Exemplo**

Dividindo $15$ por $4$, obtemos $3,\!75$. Assim, a representação decimal da fração $$\frac{15}{4} = 3,\!75$$ 

Dividindo $25$ por $3$ obtemos $8,\!333..$. Note que o $3$ se repete indefinidamente depois da vírgula, e nesse caso temos uma _dízima periódica_. 

$$ \frac{25}{3} = 8,\!3333\ldots $$

Toda fração tem uma representação decimal que é exata ou uma dízima periódica.

### Racionais e a reta

Os racionais preenchem mais a reta do que os inteiros, completando algumas lacunas entre os inteiros.

![Reta com os racionais](./img/aula03-img02.svg)

## Números reais

Embora os racionais preencham as lacunas da reta, eles não preenchem ela completamente. 

O Teorema de Pitágoras garante que um quadrado de lado $1$ possui diagonal medindo $\sqrt{2}$. Um homem demonstrou que esse número não pode ser racional e diz a lenda que ele perdeu a vida por causa disto.

Os reais são criados "completando as lacunas" dos racionais na reta, e são representados por $\mathbb{R}$. Deste modo, temos $\mathbb{Q} \subseteq \mathbb{R}$.


## Números complexos 

Pelas propriedades da multiplicação, sabemos que todo número elevado ao quadrado é positivo. Assim, não existe número real que elevado ao quadrado é negativo, e logo não faz sentido falar em raiz quadrada e um número negativo. 

Os complexos foram criados para dar sentido a expressões como $\sqrt{-121}$. Nesse caso, juntamos a unidade imaginária $i = \sqrt{-1}$ ao conjunto dos reais, e podemos fazer a conta

$$ \sqrt{-121} = \sqrt{-1\cdot 121} = \sqrt{-1}\cdot\sqrt{121} = i\cdot 11 $$

## Diagrama dos conjuntos numéricos

O diagrama abaixo representa a relação de inclusão entre os conjuntos numéricos.

![Diagrama dos conjuntos numéricos](./img/aula03-img03.svg)

## Notações especiais

- Quando adicionamos um $*$ na notação do conjunto, estamos tirando o zero dele.
- Quando adicionamos um $+$ na notação do conjunto, estamos considerando apenas os números maiores ou iguais a zero. 
- Quando adicionamos um $-$ na notação do conjunto, estamos considerando apenas os números menores ou iguais a zero.

Assim, 
- $\mathbb{N}^*$ é o conjunto dos naturais sem o zero. 
- $\mathbb{Z}_+ = \{0,1,2,3,4,\ldots\}$ é o conjunto dos inteiros não negativos, que é igual a $\mathbb{N}$.
- $\mathbb{Q}_-^*$ é o conjunto dos racionais negativos.
