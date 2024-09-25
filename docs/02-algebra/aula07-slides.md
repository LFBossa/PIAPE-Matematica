---
template: reveal.html
search:
  exclude: true
---
# Completando quadrados

---

Um trinômio quadrado perfeito tem origem em uma expressão 

$$(a+b)^2 = a^2 + 2ab + b^2$$

--

Assim, a expressão 

$$x^2 +6x + 9$$ 

pode ser fatorada como $(x+3)^2$.

--

Se a expressão fosse ligeiramente diferente, digamos

$$x^2 + 6x + 4$$

a mesma fatoração não seria possível. Entretando, temos um artifício matemático para contornar tais situações.

---

## Intuição geométrica

Ignorando o coeficiente sem $x$, temos sempre uma expressão da forma 

$$x^2 + ax$$

--

Que pode ser interpretada como a soma de áreas de um quadrado de lado $x$ e de um retângulo de lados $a$ e $x$. 

--

![Interpretação com áreas](./02-algebra/img/aula07-img01.svg)

--

![Cortando na metade](./02-algebra/img/aula07-img02.svg)

--

![Ajustando a metade](./02-algebra/img/aula07-img03.svg)

--

![Quem falta](./02-algebra/img/aula07-img04.svg)

---

## Resolvendo equação de segundo grau

Como poderíamos resolver a equação 

$$x^2 + 4x - 12 = 0$$

geometricamente?

--

Primeiro, passamos o 12 pro outro lado. 

$$x^2 + 4x =  12 $$

Interpretamos o lado esquerdo como uma soma de áreas: um quadrado mais um retângulo. Acrescentamos o pedaço que falta e obtemos 

--

$$
\\begin{align*}
x^2 + 4x + 4 &= 16 \\\\
(x+2)^2 &= 4^2 \\\\
|x+2| &= 4
\\end{align*}
$$

Assim, $x+2 = 4$ ou $x+2 = -4$, de modo que $x=2$ ou $x=-6$.

---

[Voltar ao conteúdo](./02-algebra/aula07)

