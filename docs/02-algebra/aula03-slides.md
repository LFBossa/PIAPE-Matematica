---
template: reveal.html
search:
  exclude: true
---
# Fatoração de expressões

---


Lembrando que _fator_ é um dos elementos que compõe uma _multiplicação_:
$$ 3\cdot 4 = 12 $$
3 e 4 são chamados _fatores_ e 12 é o _produto_.


---


Portanto, _fatorar_ uma expressão, consiste em trasformar ela em um produto de _fatores_.

---

## Glossário

**Fatorar**: transformar uma expressão em fatores

**Expandir**: calcular o produto dos fatores.


---


## Produtos notáveis

São expressões que aparecem corriqueiramente na matemática, por isso, _notáveis_. 


---


### Quadrado da soma 

$$(a+b)^2 = a^2 + 2ab + b^2$$

--

**Exemplos**

$$
\begin{align*} (x+2)^2 &= \\\\
\left(y + \frac{2}{3}\right)^2 &= \\\\
\left(3z + \sqrt{5}\right)^2 &=  \\\\
\end{align*}
$$

--


**Exemplos**

$$
\begin{align*} (x+2)^2 &= x^2 + 4x + 4 \\\\
\left(y + \frac{2}{3}\right)^2 &= y^2 + \frac{4}{3}y + \frac{4}{9} \\\\
\left(3z + \sqrt{5}\right)^2 &=  9z^2 + 6\sqrt{5}z + 5\\\\
\end{align*}
$$

---


### Quadrado da diferença

$$(a-b)^2 = a^2 - 2ab + b^2$$

--

**Exemplos**

$$
\begin{align*} (x-3)^2 &=  \\\\
\left(\alpha - \frac{1}{2}\right)^2 &= \\\\
\left(2\gamma - \sqrt{3}\right)^2 &= \\\\
\end{align*}
$$

--

$$
\begin{align*} (x-3)^2 &= x^2 -6x + 9  \\\\
\left(\alpha - \frac{1}{2}\right)^2 &= \alpha^2 - \alpha + \frac{1}{4}\\\\
\left(2\gamma - \sqrt{3}\right)^2 &= 4\gamma^2 -4\sqrt{3}\gamma +3\\\\
\end{align*}
$$

---


### Produto da soma e diferença

$$(a+b)(a-b) = a^2 - b^2$$

--

**Exemplos**

$$
\begin{align*} (x - 7)(x+7) &= \\\\
(3s-2)(3s+2) &= \\\\
\left(\frac{p^2}{3} + \sqrt{2}t\right)\left(\frac{p^2}{3} - \sqrt{2}t\right) &= \\\\
\end{align*}
$$

--

$$
\begin{align*} (x - 7)(x+7) &= x^2 - 49\\\\
(3s-2)(3s+2) &= 9s^2 - 4\\\\
\left(\frac{p^2}{3} + \sqrt{2}t\right)\left(\frac{p^2}{3} - \sqrt{2}t\right) &= \frac{p^4}{9} - 2t^2 \\\\
\end{align*}
$$



---


### Cubo da soma

$$(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$

--

**Exemplos**

$$
\begin{align*} (2x+1)^3 &= \\\\
\left(\frac{b}{2} + c^2\right)^3&= \\\\
\end{align*}
$$

--


$$
\begin{align*} (2x+1)^3 &= 8x^3 + 12x^2 + 6x + 1 \\\\
\left(\frac{b}{2} + c^2\right)^3&= \frac{b^3}{8} + \frac{3}{4}b^2c^2 + \frac{3}{2}bc^4 + c^6 \\\\
\end{align*}
$$

---


### Cubo da diferença

$$(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$

--

**Exemplos**
$$
\begin{align*} (2y-3)^3 &= \\\\
\left(\frac{d}{3} - 2l^2\right)^3&= \\\\
\end{align*}
$$

--

$$
\begin{align*} (2y-3)^3 &= 8y^{3}-36y^{2}+54y-27\\\\
\left(\frac{d}{3} - 2l^2\right)^3&= \frac{d^{3}}{27}-\frac{2}{3}d^{2}l^{2}+4dl^{4}-8l^{6} \\\\
\end{align*}
$$

---

### Diferença de cubos

$$a^3 - b^3 = (a-b)(a^2+ab +b^2)$$

--

**Exemplos**
$$
\begin{align*}x^3 - 1 &= \\\\
8\beta^3 - 27 &=  \\\\
\end{align*}
$$

--

$$
\begin{align*}x^3 - 1 &= (x-1)(x^2 +x + 1)\\\\
8\beta^3 - 27 &= (2\beta - 3)(4\beta^2 + 6\beta + 9)\\\\
\end{align*}
$$


---

## Outras nomenclaturas

- $(a\pm b)^2$ é o _quadrado da soma ou diferença_
- $a^2 \pm 2ab + b^2$ é o _trinômio quadrado perfeito_
- $(a+b)(a-b)$ é o _produto conjugado_
- $a^2 - b^2$ é a _diferença de quadrados_

---

## Resumo

$$
\\begin{align*}
(a+b)^2 &= a^2 + 2ab + b^2\\\\
(a-b)^2 &= a^2 - 2ab + b^2\\\\
(a+b)^3 &= a^3 + 3a^2b + 3ab^2 + b^3\\\\
(a-b)^3 &= a^3 - 3a^2b + 3ab^2 - b^3 \\\\
a^2 - b^2 &= (a-b)(a+b)\\\\
a^3 - b^3 &= (a-b)(a^2+ab +b^2)
\\end{align*}
$$

---

## Generalização

Binômio de Newton

$$(a+b)^n = \sum_{k=0}^n \begin{pmatrix} n \\\\ k \end{pmatrix} a^{n-k}b^k$$

---

[Voltar ao conteúdo](./02-algebra/aula03)