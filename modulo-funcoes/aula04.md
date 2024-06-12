# Composição de funções


Se tivermos um par de funções

$$f:A\to B \qquad g:B\to C$$

podemos criar uma nova função, que vai de $A$ diretamente para $C$, utilizando as regras que definem $f$ e $g$: aplicamos primeiro $f$ e depois aplicamos $g$, formando a função

$$\begin{aligned}
g\circ f: A&\to C\\
x&\mapsto g(f(x))
\end{aligned}$$


> Para ser mais preciso, precisamos garantir que $\text{Im }f\subseteq \text{Dom }g$. Mas não nos preocuparemos com detalhes agora. 

## Exemplos

Se $f(x) = \sqrt{x} + 2$ e $g(x) = 3x -1$, calculamos $g\circ f$ fazendo em duas etapas:
- Na fórmula de $g$, substituímos todos os $x$ por $f(x)$
$$(g\circ f )(x) = 3f(x) - 1$$

- Na fórmula obtida, substituímos $f(x)$ pela sua fórmula e efetuamos os cálculos para simplificar as expressões
$$(g\circ f )(x) = 3(\sqrt{x} + 2) - 1 = 3\sqrt{x} + 6 - 1  = 3\sqrt{x} + 5$$

Se quisermos calcular $f\circ g$, procedemos de maneira análoga:
- Na fórmula de $f$, substituímos todos os $x$ por $g(x)$
$$(f\circ g)(x) = \sqrt{g(x)} + 2$$
- Na fórmula obtida, substituímos $g(x)$ por sua fórmula e efetuamos as simplificações, se possível
$$(f\circ g)(x) = \sqrt{3x-1} + 2$$

## 'Decomposição' de funções

Uma habilidade importante para se desenvolver é a habilidade de ver uma expressão como composição de funções. No Cálculo, isso é fundamental para aplicar a regra da cadeia. 

Por exemplo, 
$$\sqrt{2x + 1} + 3$$
pode ser decomposto como a composição de $f(x)=2x+1$ com $g(x)=\sqrt{x} + 3$
