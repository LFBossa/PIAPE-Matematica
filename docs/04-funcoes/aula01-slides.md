---
template: reveal.html
search:
  exclude: true
---
# Funções

## definição, domínio, contradomínio e imagem

---

Em notação matemática, usamos a notação $$f:A\to B$$ para representar uma função de nome $f$ que associa elementos do conjunto $A$ a elementos do conjunto $B$.

---

## Nomenclatura

$$f:A\to B$$

- $f$: nome da função
- $A$: **domínio** da função, denotado por $\text{Dom} f$
- $B$: **contradomínio**, denotado por $\text{CD} f$


---


## Formalizando

Uma função é uma relação de um conjunto $A$ num conjunto $B$ tal que cada elemento de $A$ está associado a um _único_ elemento de $B$.

---

**Definindo uma função por uma regra**

$$\begin{align*} f:A&\to B \\\\ x&\mapsto 2x\end{align*}$$

$f$ é a função que associa elementos do conjunto $A$ no conjunto $B$, transformando $x$ em $2x$.

--

Sendo $$A = \left\\{-1,0,\tfrac{1}{2},3\right\\}\\\\[1ex] B = \\{-2,-1,0,1,4,5,6\\}$$ temos a seguinte associação:

--

$$\begin{align*}
f:A&\to B \\\\ 
x&\mapsto 2x \\\\
-1 & \mapsto -2\\\\
0 & \mapsto 0 \\\\
\tfrac{1}{2} & \mapsto 1 \\\\
3 & \mapsto 6 \\\\
\end{align*}$$

---

## Representação por diagrama

No caso do domínio e contradomínio serem pequenos, podemos representar com um diagrama de flechas.

--

![imagem](./04-funcoes/img/aula01-img01.svg)

---

## Mais nomenclatura

$$f\left(\tfrac{1}{2}\right) = 1$$

Essa notação acima indica que o número $\tfrac{1}{2}$ está associado ao $1$. 

- $\tfrac{1}{2}$ é o **argumento** da função
- $1$ é a **imagem** do $\tfrac{1}{2}$ pela função $f$

---

## Imagem

A imagem de uma função é o conjunto de todos os elementos do contradomínio que estão associados a algum elemento do domínio, denotada por $\text{Im} f$.

---

No diagrama de flechas, a imagem é composta de todos os elementos do contradomínio que recebem flechas.

![imagem](./04-funcoes/img/aula01-img02.svg)

---

$$\text{Im} f = \\{-2, 0, 1, 6\\}$$

Sempre vale que $\text{Im} f \subseteq \text{CD} f$


---

## Diagramas que não representam funções

---

![imagem](./04-funcoes/img/aula01-img03.svg)

---

![imagem](./04-funcoes/img/aula01-img04.svg)

---

[Voltar ao conteudo](./04-funcoes/aula01)
