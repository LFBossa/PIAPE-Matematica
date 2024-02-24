# Elementos, Conjuntos e pertinência

Em Matemátemática, utilizamos _sistemas axiomáticos_. Nesses sistemas, temos algumas _noções elementares_, que são coisas que não definimos e _axiomas_, que são as regras que escolhemos como válidas dentro desse sistema. 

Na Teoria dos Conjuntos, as noções elementares são:
- conjunto
- elemento
- pertinência

Nossa noção de conjunto em matemática é a mesma da linguagem coloquial: um agrupamento de coisas. Essas coisas que compõe o conjunto são os elementos desse conjunto. Quando um elemento faz parte de um conjunto, dizemos que ele _pertence_ ao conjunto.

**Exemplos**

- O conjunto das vogais: a, e, i, o, u
- O conjunto de alunos do PIAPE
- O conjunto de alunos da UFSC Blumenau
- O conjunto dos números pares: 0, 2, 4, 6, 8,...

## Pertinência

Quando queremos dizer que um elemento pertence a um conjunto, utilizamos o símbolo $\in$. Quando queremos dizer que um elemento não pertence a um conjunto, utilizamos $\notin$.
Assim, $$a\in \text{conjunto das vogais}$$
$$c \notin \text{conjunto das vogais}$$
$$0\in \text{conjunto dos números pares}$$
$$1\notin \text{conjunto dos números pares}$$

## Convenção

Uma convenção é um acordo. A convenção geral é que utilizamos letras minúsculas para denotar os elementos e letras maiúsculas para denotar os conjuntos. 
- $a, b, c$ são elementos
- $A, B, C$ são conjuntos

## Definindo um conjunto

Podemos definir um conjunto de duas maneiras:
- Enumerando seus elementos
- Descrevendo uma propriedade que seus elementos possuem

**Exemplo**

- O conjunto das vogais podemos enumerar como $$V=\{a,e,i,o,u\}$$
Sempre enumeramos os elementos de um conjunto entre chaves $\{\}$. Assim, para dizer que "a" é uma vogal, podemos denotar por $a\in V$.
- O conjunto dos números pares podemos descrever como
$$P = \{ n \text{ é um número par} \}$$

## Conjunto unitário e vazio

Existe um conjunto que não possui nenhum elemento. Esse conjunto é chamado de _conjunto vazio_, e denotado pelo símbolo $\emptyset$.

Um _conjunto unitário_ é um conjunto que possui apenas um elemento. 

**Exemplo**:  o conjunto de tutores de matemática do PIAPE no campus Blumenau possui um único elemento.

## Conjunto universo

Quando estamos trabalhando em um problema, geralmente consideramos um _conjunto universo_, que é o conjunto de todos os elementos que podemos considerar no contexto estudado.

## Subconjuntos

Dizemos que um conjunto $A$ é _subconjunto de $B$ se todo elemento de $A$ também pertence a $B$. Nesse caso, utilizamos a notação $A \subseteq B$.

**Exemplo**
- Seja $A = \{a,b,c\}$ e $B = \{a,b,c,d,e\}$. Note que todo elemento de $A$ também percente a $B$, logo $A \subseteq B$.
- Seja $P = \{ n \text{ é um número par} \}$ e $D = \{ n \text{ é um número múltiplo de 10} \}$. Como todo número múltiplo de 10 também é par, podemos escrever $D \subseteq P$.

**Contra-exemplos**

- Se $A = \{a,e,i,o,u\}$ e $B = \{a,b,c,d,e\}$, note que nem todo elemento de $A$ pertence a $B$. Nesse caso, $A$ **não é** um sonjunto de $B$, e denotamos esse fato escrevendo $$A\not\subseteq B$$
- Seja $P = \{ n \text{ é um número par} \}$ e $C = \{ n \text{ é um número múltiplo de 5} \}$. Nesse caso, $5\in C$, porém $5\not\in P$. Assim, $C$ não pode ser um subconjunto de $P$, e denotamos por $C\not\subseteq P$.


## Diagramas de Venn

Podemos representar conjuntos de maneira visual. Para isso, utilizamos diagramas de Venn. 

Podemos representar o conjunto $A = \{a,b,c,d,e\}$ listando seus elementos e agrupando eles dentro de um círculo, como abaixo

<svg height="200" width="200">
  <circle cx="100" cy="100" stroke="black" r="80" fill="#0000BB" />
  <text x="60" y="80" font-size="20">a</text>
  <text x="120" y="70" font-size="20">b</text>
  <text x="60" y="130" font-size="20">c</text>
  <text x="120" y="140" font-size="20">d</text>
  <text x="90" y="110" font-size="20">e</text>
  <text x="20" y="30" font-size="32">A</text>
</svg>

Se quisermos representar o conjunto $A = \{a,b,c\}$ juntamente com o conjunto $B = \{a,b,c,d,e\}$, podemos representar todos os elementos e depois circular os que pertencem a $A$ e os que pertencem a $B$.

<svg height="200" width="200">
  <circle cx="100" cy="100" stroke="black" r="95" fill="#00BB22" />
  <circle cx="70" cy="110" stroke="black" r="50" fill="#0000BB" />
  <text x="60" y="80" font-size="20">a</text>
  <text x="60" y="110" font-size="20">b</text>
  <text x="60" y="140" font-size="20">c</text>
  <text x="130" y="90" font-size="20">d</text>
  <text x="130" y="130" font-size="20">e</text>
  <text x="50" y="50" font-size="32">A</text>
  <text x="180" y="40" font-size="32">B</text>
</svg>

Agora temos uma maneira visual de entender que $A\subseteq B$.

Se quisermos representar o conjunto $A = \{a,e,i,o,u\}$ juntamente com o conjunto $B = \{a,b,c,d,e\}$, podemos representar todos os elementos e depois circular os que pertencem a $A$ e os que pertencem a $B$.


<svg height="200" width="400">
  <circle cx="100" cy="110" stroke="black" r="50" fill="#00BB22A0" />
  <circle cx="50" cy="110" stroke="black" r="50" fill="#0000BBA0" />
  <text x="30" y="80" font-size="20">u</text>
  <text x="10" y="110" font-size="20">o</text>
  <text x="30" y="140" font-size="20">i</text>
  <text x="70" y="90" font-size="20">a</text>
  <text x="70" y="130" font-size="20">e</text>
  <text x="100" y="80" font-size="20">b</text>
  <text x="120" y="110" font-size="20">c</text>
  <text x="100" y="140" font-size="20">d</text>
  <text x="10" y="50" font-size="32">A</text>
  <text x="110" y="50" font-size="32">B</text>
</svg>