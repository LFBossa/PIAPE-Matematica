# Intervalos

Intervalos representam um subconjunto de números que estão em sequência

## Notação de intervalo

Dados dois números $a$ e $b$ pertencentes a um conjunto numérico $\mathbb{B}$ qualquer, com $a$ < $b$. Aqui, $\mathbb{B}$ pode estar representando $\mathbb{N}, \mathbb{Z}, \mathbb{Q}$ ou $\mathbb{R}$.

A notação de intervalo com extremos $a$ e $b$ representa o conjunto de todos os números que são maiores do que $a$ e menores do que $b$, podendo ou não incluir os extremos. 

**Intervalo aberto** 
$$]a,b[  =  \{x\in\mathbb{B} \mid a < x < b\}$$
Nesse caso, os extremos **não pertencem** ao intervalo.

**Intervalo fechado** 
$$[a,b]  =  \{x\in\mathbb{B} \mid a \le x \le b\}$$
Nesse caso, os extremos **pertencem** ao intervalo.

Podemos também misturar a notação e criar os intervalos "mistos"

**Intervalo fechado à esquerda** 
$$[a,b[  =  \{x\in\mathbb{B} \mid a \le x < b\}$$

**Intervalo fechado à direita** 
$$]a,b]  =  \{x\in\mathbb{B} \mid a < x \le b\}$$

## Representação gráfica

Podemos representar um intervalo na reta numérica destacando seus extremos e seu interior. Marcamos os extremos como bolinhas, e se o extremo pertencer ao intervalo, pintamos o interior dessa bolinha. Se o extremo não pertencer, deixamos vazio. 

**Intervalo aberto**

![Intervalo aberto](./img/aula04-img01.svg)


**Intervalo fechado**

![Intervalo aberto](./img/aula04-img02.svg)


**Intervalo fechado à esquerda**

![Intervalo aberto](./img/aula04-img03.svg)


**Intervalo fechado à direita**

![Intervalo aberto](./img/aula04-img04.svg)

## Exemplos

**Exemplos**

1. O intervalo $[3,7]$ em $\mathbb{N}$ é o conjunto 
$$ [3,7] = \{x\in \mathbb{N} \mid 3\le x \le 7\} = \{3,4,5,6,7\} $$

2. O intervalo $]-3,3[$ em $\mathbb{Z}$ é o conjunto 
$$ ]-3,3[ = \{x\in \mathbb{Z} \mid -3 < x < 3\} = \{-2,-1,0,1,2\} $$

3. O intervalo $]0,1]$ em $\mathbb{Q}$ contém todos os racionais maiores que zero e menores ou iguais a 1. Assim, $0$ não está no intervalo, mas $1$ está. 

4. O intervalo $[0,1[$ em $\mathbb{R}$ contém o zero mas não contém o um.

## Intervalos ilimitados

São intervalos limitados em apenas um dos extremos. O extremo ilimitado é representado pelo símbolo do infinito $\infty$ e é sempre _aberto_ nesse extremo. 

$$[a,\infty[ = \{x\in\mathbb{B}\mid x \ge a \}$$
$$]-\infty,a] = \{x\in\mathbb{B}\mid x \le a \}$$
