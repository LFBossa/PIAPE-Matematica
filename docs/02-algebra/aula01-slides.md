---
template: reveal.html
search:
  exclude: true
---
# A lei das potências

---

## Potências

Uma potência é uma multiplicação feita repetidas vezes.

$$2^3 = 2\cdot 2 \cdot 2 = 8$$

$$(-3)^4 = (-3)\cdot (-3)\cdot (-3)\cdot  (-3) = 9\cdot 9  = 81$$

--

O número que está sendo multiplicado é chamado de _base_ e o número de vezes que ele está sendo multiplicado é chamado _expoente_.

---

## Propriedade fundamental das potências

$$a^n\cdot a^m = a^{n+m}$$

> Ao multiplicarmos potências de mesma base, somam-se os expoentes. 

--

**Exemplos**

- $2^3\cdot 2^4 = 2^7$
- $(-3)^2\cdot (-3)^4 = (-3)^6$
- $\sqrt{7}\cdot \sqrt{7}^3 = \sqrt{7}^4$

É essa propriedade que permite expandir os expoentes para outros conjuntos numéricos.

---

## Expoente zero

Note que fazendo $n=0$, temos a seguinte situação:

$$a^0\cdot a^m = a^{0+m} = a^m$$

--

Pela propriedade **[M3]** (existência do elemento neutro da multiplicação), o elemento neutro da multiplicação é _único_. Note que o $a^0$ está fazendo papel de elemento neutro, portanto, segue que 
$$a^0 = 1$$
não importa qual seja o valor de $a$. 

---

## Expoente negativo

Como podemos definir $a^{-n}$? Podemos utilizar a propriedade das potências para calcular
$$a^{-n}\cdot a^{n} = a^{-n+n} = a^0 = 1$$

Logo, isolando $a^{-n}$ obtemos a fórmula
$$a^{-n} = \frac{1}{a^n}$$

---

## Potência de potência

Podemos elevar uma potência a uma potência. Exemplo

$$\left(a^n\right)^3 = a^n\cdot a^n\cdot a^n = a^{n+n+n} = a^{3n}$$

Assim, de modo geral, vale

$$\left(a^n\right)^m = a^{m\cdot n}$$

---

## Expoente fracionário

O que significaria $a^{\frac{1}{2}}$? 

Note que, pela propriedade fundamental, teríamos

$$a^{\frac{1}{2}}\cdot a^{\frac{1}{2}}  = a^{\frac{1}{2} + \frac{1}{2} } = a^{1} = a$$

--

Por outro lado, podemos reescrever o lado esquerdo como $(a^{1/2})^2$. Logo

$$\left(a^{\frac{1}{2}}\right)^2 = a$$

Tomando a raiz quadrada de ambos os lados, obtemos

$$a^{\frac{1}{2}} = \sqrt{a}$$

--

De maneira análoga, 

$$ a^{\frac{1}{n}} = \sqrt[n]{a}$$

--

E usando a propriedade de potência de potência, temos o caso geral 

$$a^{\frac{m}{n}} = \sqrt[n]{a^m}$$


---

## Outras propriedades

Todas as propriedades acima foram deduzidas para uma potência de uma base só. 

Podemos utilizar a propriedade comutativa da multiplicação para obter a seguinte propriedade envolvendo potências de multiplicações.

--

### Potência de um produto

$$(a\cdot b)^n = a^n\cdot b^n$$

---

[Voltar ao conteúdo](./02-algebra/aula01)
