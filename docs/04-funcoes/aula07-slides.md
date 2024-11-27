---
template: reveal.html
search:
  exclude: true
---
# Função inversa

---

Quando uma função 
$$f:A\to B$$
 é bijetiva, isto é, é injetiva e sobrejetiva ao mesmo tempo, é garantido que para cada valor do contradomíno está associado um único valor do domínio.

--

![Função injetora](./04-funcoes/img/aula07-img01.svg)

---

Nesse caso, é possível "inverter a seta" de maneira que tenhamos ainda uma função. Essa função é a chamada **função inversa** 
$$f^{-1}: B \to A$$

--


![Função inversa](./04-funcoes/img/aula07-img02.svg)

---

## Calculando a inversa

Fazemos 
$$y = f(x)$$
trocamos $y$ por $x$ e $x$ por $y$ na expressão acima e resolvemos para $y$
$$x = f(y)$$ 

--

<img src="./04-funcoes/img/aula07-img03.png" height="500"/>


---

**Exemplo 1**

Encontrar a inversa de $f(x) = 3x + 4$

$$\begin{align*}
y &= 3x + 4  \\\\
x &= 3y + 4 & (\text{troca } xy)\\\\
x - 4 &= 3y & (\text{isola } y)\\\\
\frac{x-4}{3} &= y  \\\\
\end{align*}
$$

--

Assim, $$f^{-1}(x) =\frac{x-4}{3}$$

---

**Exemplo 2**

Encontrar a inversa de $f(x) = \frac{x}{2x-3}$

$$\begin{align*}
y &=  \frac{x}{2x-3}  \\\\
x &=  \frac{y}{2y-3} & (\text{troca } xy)\end{align*}
$$

--

$$\begin{align*}
x(2y-3)&= y & (\text{isola } y)\\\\
2xy - 3x &= y  \\\\
2xy - y &=3x \\\\
(2x-1)y &= 3x \\\\
y &= \frac{3x}{2x-1}
\end{align*}$$

--

Assim, $$f^{-1}(x) = \frac{3x}{2x-1}$$


---

## Propriedades da inversa

$$
\begin{align*}
f:A&\to B\\\\
f^{-1}:B&\to A
\end{align*}
$$

Assim, 
$$
\begin{align*}
\text{Dom } f &= \text{Im } f^{-1}\\\\
\text{Im } f &= \text{Dom } f^{-1}
\end{align*}
$$

--

A composição da $f$ com sua inversa dá a função identidade.

$$
\begin{align*}
f\left(f^{-1} (x)\right) &= x  \\\\
f^{-1}\left(f (x)\right) &= x 
\end{align*}
$$

---

[Voltar ao conteúdo](./04-funcoes/aula07)
