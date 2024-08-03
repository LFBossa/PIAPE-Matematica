---
template: reveal.html
search:
  exclude: true
---
# Frações Parciais

Uma função racional 
$$\frac{P(x)}{Q(x)}$$
pode ser reescrita como soma de frações mais simples
$$\frac{A_1}{x-a_1} + \frac{A_2}{x-a_2} + \ldots + \frac{A_nx+B_n}{x^2 + a_nx + b_n}$$

Quem dita o formato da decomposição é o denominador $Q(x)$.  Nos casos abaixo, estaremos trabalhando na hipóteses de $Q(x)$ ter grau 2. 

## Caso 1: fatores lineares distintos

Se $Q(x)$ pode ser fatorado em $(x-a)(x-b)$ então podemos escrever

$$\frac{P(x)}{Q(x)} = \frac{A}{x-a} + \frac{B}{x-b}$$

Para descobrir os coeficientes do lado direito, fazemos o MMC dos denominadores e somamos as frações.

### Exemplo 1

$$\frac{2x+4}{x^2-5x+6} = \frac{A}{x-2} + \frac{B}{x-3}$$

Reescrevendo o lado direito
$$\frac{2x+4}{x^2-5x+6} = \frac{A(x-3)}{(x-2)(x-3)} + \frac{B(x-2)}{(x-2)(x-3)}$$

Igualando os numeradores

$$2x+4 = A(x-3) + B(x-2)$$

Escolhendo uns valores "espertos" de $x$, obtemos os valores de $A$ e $B$. Fazendo $x=2$ temos

$$2\cdot 2 + 4 = A(2-3) + B(2-2) \Rightarrow 8 = -A$$

Fazendo $x=3$ temos

$$2\cdot 3 + 4 = A(3-3) + B(3-2) \Rightarrow 10 = B$$

Assim, 
$$\frac{2x+4}{x^2-5x+6} = \frac{-8}{x-2} + \frac{10}{x-3}$$

## Caso 2: fatores lineares repetidos

Caso $Q(x) = (x-a)^2$.

$$\frac{P(x)}{Q(x)} = \frac{A}{x-a} + \frac{B}{(x-a)^2}$$

## Caso 3: quando o polinômio não tem raiz

Caso $Q(x)$ não tenha raízes reais, não tem muito o que fatorar

$$\frac{P(x)}{Q(x)} = \frac{Ax + B}{x^2 + pq + q}$$


## Graus maiores que 2

No caso de $Q(x)$ ter grau maior do que 2, aplicamos as regras acima para cada fator que aparecer no denominador. 

Vamos supor que $Q(x)$ seja fatorado em $(x-2)(x-1)^2(x^2+1)$

Para o fator $x-2$ aplicamos o Caso 1, para o fator $(x-1)^2$ aplicamos o Caso 2 e para $x^1+1$ aplicamos o Caso 3, obtendo

$$\frac{P(x)}{(x-2)(x-1)^2(x^2+1)} = \frac{A}{x-2} + \frac{B}{x-1} + \frac{C}{(x-1)^2} + \frac{Dx+E}{x^2+1}$$




[Referência](https://lemas.furg.br/images/parte1.pdf)

---

<div class="grid cards" markdown>
 - [Slides :material-presentation-play:](./aula08-slides.md)
 - [Exercícios :writing_hand:](./questoes08.pdf)
</div>
