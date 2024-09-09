---
template: reveal.html
search:
  exclude: true
---
# Equações

---

Uma equação é uma igualdade entre expressões algébricas. 

Para resolver uma equação, precisamos classificá-la. 

A classificação de uma equação depende da variável de interesse. 

--

Na equação 
$$x^2-4b=0$$
podemos estar interessados em descobrir $x$ em função de $b$ ou $b$ em função de $x$. 

No primeiro caso, teremos uma equação de 2º grau em $x$. No segundo caso, teremos uma equação de 1º grau em $b$.

--

Resolvendo o primeiro caso, teríamos 
$$ x = \pm 2\sqrt{b}$$

--

Resolvendo o segundo caso, teríamos 
$$ b = \frac{x^2}{4}$$

---

## Equações de primeiro grau

Resolvemos elas utilizando a regra máxima: 

> Uma equação funciona como uma balança: tudo o que for feito de um lado da equação, deve ser feito do outro lado também. 

--

Para resolver a equação 

$$ 4x -3 = 13$$ 

inicialmente queremos isolar o termo com $x$. Para isso, precisamos nos livrar do termo $-3$ do lado esquerdo da equação. Para fazer isso, somaremos $+3$ em ambos os lados da equação, obtendo 

--

$$4x -3 +3 = 13 + 3$$
$$4x = 16$$

Agora, para isolar o $x$ completamente, precisamos nos livrar do fator 4. Podemos dividir ambos os lados da equação por $4$ (ou de modo equivalente, multiplicamos ambos os lados por $\frac{1}{4}$). 

---

## Equações de segundo grau

Resolvemos utilizando a fórmula de Bashkara.

--

A equação $$ax^2 + bx + c = 0$$ tem soluções dadas por
$$\begin{align*}
x = \frac{-b\pm \sqrt{\Delta}}{2a} \qquad \Delta = b^2 - 4ac
\end{align*}$$

--

Conforme o sinal de $\Delta$, podemos ter

| Caso | Soluções |
| ---- | --------: |
| $\Delta > 0$ | 2 soluções em $\mathbb{R}$ |
| $\Delta = 0$ | 1 solução em $\mathbb{R}$ |
| $\Delta < 0$ | 2 soluções em $\mathbb{C}$ |

---

### Soma e produto

Outra maneira de solucionar uma equação do segundo grau é através da soma e produto das raízes, dada pelas Relações de Girard.

--

Se equação $$x^2 + px + q = 0$$ tem raízes $x'$ e $x''$, então 

$$\begin{align*}
x' + x''  &= -p & (\text{a soma é }-b)\\\\
x'\cdot x'' &= q & (\text{o produto é }c)
\end{align*}$$

---

[Voltar ao conteudo](./03-equacoes/aula01)