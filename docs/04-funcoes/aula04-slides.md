---
template: reveal.html
search:
  exclude: true
---
# Composição de funções

---

Se tivermos um par de funções

$$f:A\to B \qquad g:B\to C$$


podemos criar uma nova função, que vai de $A$ diretamente para $C$, utilizando as regras que definem $f$ e $g$: aplicamos primeiro $f$ e depois aplicamos $g$, formando a função

---

$$\begin{aligned}
g\circ f: A&\to C\\\\
x&\mapsto g(f(x))
\end{aligned}$$


> Precisamos garantir que $$\text{Im }f\subseteq \text{Dom }g$$

---

## Exemplos

$$f(x) = \sqrt{x} + 2$$ $$g(x) = 3x -1$$

A ideia principal é que o $x$ representa apenas um espaço a ser preenchido na expressão.

--

$$\begin{align*}
f(\square) = \sqrt{\square} + 2\\\\
g(\star) = 3\star -1
\end{align*}$$


--

Calculamos $g\circ f$ fazendo em duas etapas:
- Na fórmula de $g$, substituímos todos os $x$ por $f(x)$
$$(g\circ f )(x) = 3f(x) - 1$$

--

- Na fórmula obtida, substituímos $f(x)$ pela sua fórmula e efetuamos os cálculos para simplificar as expressões
$$
\begin{aligned}
(g\circ f )(x) &= 3(\sqrt{x} + 2) - 1 \\\\ &= 3\sqrt{x} + 6 - 1  = 3\sqrt{x} + 5
\end{aligned}$$

--

Se quisermos calcular $f\circ g$, procedemos de maneira análoga:
- Na fórmula de $f$, substituímos todos os $x$ por $g(x)$
$$(f\circ g)(x) = \sqrt{g(x)} + 2$$

--

- Na fórmula obtida, substituímos $g(x)$ por sua fórmula e efetuamos as simplificações, se possível
$$(f\circ g)(x) = \sqrt{3x-1} + 2$$

---

## 'Decomposição' de funções

Uma habilidade importante para se desenvolver é a habilidade de ver uma expressão como composição de funções. No Cálculo, isso é fundamental para aplicar a regra da cadeia. 

--

Regras de bolso para "decompor" funções

- Agrupar tudo o que está dentro de uma raiz, logaritmo, exponencial, funções trigonométricas ou parênteses: essa é a função "de dentro"
- O que sobra é a função "de fora"


--

Aplicando a regra anterior na expressão 
$$\sqrt{2x + 1} + 3$$

temos que a função "de dentro" é $f(x) = 2x+1$

--

A expressão vira 
$$\sqrt{f(x)} + 3$$

Logo, a função "de fora" é $g(x) = \sqrt{x} + 3$.



---

[Voltar ao conteudo](./04-funcoes/aula04)
