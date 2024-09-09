---
template: reveal.html
search:
  exclude: true
---
# Intervalos

---

Intervalos representam um subconjunto de números que estão em sequência.

---

## Notação de intervalo

Dados dois números $a$ e $b$ pertencentes a um conjunto numérico $\mathbb{B}$ qualquer, com $a$ < $b$. Aqui, $\mathbb{B}$ pode estar representando $\mathbb{N}, \mathbb{Z}, \mathbb{Q}$ ou $\mathbb{R}$.

--

A notação de intervalo com extremos $a$ e $b$ representa o conjunto de todos os números que são maiores do que $a$ e menores do que $b$, podendo ou não incluir os extremos. 

--

### Intervalo aberto

$$]a,b[  =  \\{x\in\mathbb{B} \mid a < x < b\\}$$

Nesse caso, os extremos **não pertencem** ao intervalo.

Outra maneira de denotar esse intervalo é usando parênteses $(a,b)$

--

### Intervalo fechado

$$[a,b]  =  \\{x\in\mathbb{B} \mid a \le x \le b\\}$$

Nesse caso, os extremos **pertencem** ao intervalo.

--

Podemos também misturar a notação e criar os intervalos "mistos"

--

### Intervalo fechado à esquerda

$$[a,b[  = [a,b) =  \\{x\in\mathbb{B} \mid a \le x < b\\}$$

--

### Intervalo fechado à direita

$$]a,b] = (a,b] =  \\{x\in\mathbb{B} \mid a < x \le b\\}$$

---

## Representação gráfica

Podemos representar um intervalo na reta numérica destacando seus extremos e seu interior. Marcamos os extremos como bolinhas, e se o extremo pertencer ao intervalo, pintamos o interior dessa bolinha. Se o extremo não pertencer, deixamos vazio. 

--

**Intervalo aberto**

$]a,b[$ ou $(a,b)$

<img title="Intervalo aberto"  width="600" src="./01-conjuntos/img/aula04-img01.svg"/>

--

**Intervalo fechado**

$[a,b]$

<img title="Intervalo fechado" width="600" src="./01-conjuntos/img/aula04-img02.svg"/>

--

**Intervalo fechado à esquerda**

$[a,b[$ ou $[a,b)$

<img title="Intervalo aberto" width="600" src="./01-conjuntos/./img/aula04-img03.svg"/>

--

**Intervalo fechado à direita**

$]a,b]$ ou $(a,b]$

<img title="Intervalo aberto" width="600" src="./01-conjuntos/./img/aula04-img04.svg"/>

---

## Exemplos

--

1. O intervalo $[3,7]$ em $\mathbb{N}$ é o conjunto 

$$ [3,7] = \\{x\in \mathbb{N} \mid 3\le x \le 7\\} = \\{3,4,5,6,7\\} $$

--

2. O intervalo $]-3,3[$ em $\mathbb{Z}$ é o conjunto 

$$ ]-3,3[ = \\{x\in \mathbb{Z} \mid -3 < x < 3\\} = \\{-2,-1,0,1,2\\} $$

--

3. O intervalo $]0,1]$ em $\mathbb{Q}$ contém todos os racionais maiores que zero e menores ou iguais a 1. Assim, $0$ não está no intervalo, mas $1$ está. 

--

4. O intervalo $[0,1[$ em $\mathbb{R}$ contém o zero mas não contém o um.

---

## Intervalos ilimitados

São intervalos limitados em apenas um dos extremos. O extremo ilimitado é representado pelo símbolo do infinito $\infty$ e é sempre _aberto_ nesse extremo. 

--

**Intervalo ilimitado à direita**

$$[a,\infty[ = [a,\infty)= \\{x\in\mathbb{B}\mid x \ge a \\}$$

<img title="Intervalo ilimitado à direita" width="600" src="./01-conjuntos/img/aula04-img0a.svg"/>

--

**Intervalo ilimitado à esquerda**

$$]-\infty,a] = (-\infty,a] = \\{x\in\mathbb{B}\mid x \le a \\}$$

<img title="Intervalo ilimitado à esquerda" width="600" src="./01-conjuntos/img/aula04-img0b.svg"/>

---

## Operações com intervalos

Para operar dois intervalos, é interessante desenhar ambos os intervalos em retas paralelas, respeitando a ordem dos extremos.

--

Para calcular a interseção dos intervalos $[-2,2[$ e $[0,3]$, desenhamos um em cima do outro e marcamos a região que está em ambos os intervalos ao mesmo tempo. 

--

<img title="Interseção de intervalos" width="600" src="./01-conjuntos/./img/aula04-img05.svg"/>

Assim, obtemos

$$ [-2,2[\cap[0,3] = [0,2[$$

--

Se quiséssemos calcular a união, bastaria marcar a região que está em qualquer um dos conjuntos

<img title="União de intervalos" width="600" src="./01-conjuntos/./img/aula04-img06.svg"/>


Assim, obtemos

$$ [-2,2[\cup[0,3] = [-2,3]$$

---

[Voltar ao conteúdo](./01-conjuntos/aula04) 