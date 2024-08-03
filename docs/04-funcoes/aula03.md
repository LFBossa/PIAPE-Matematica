# Operações com funções e domínios

Uma coisa muito legal que acontece em matemática é o seguinte: 
- Suponha que temos um conjunto $B$ qualquer que tem alguma operação definida $\star$ (uma soma, multiplicação, qualquer coisa);
- Sendo  $f$ e $g$ duas funções de um conjunto qualquer $A$ em $B$, podemos definir essa mesma operação $\star$ para $f$ e $g$: basta aplicar essa operação nas fórmulas de $f$ e $g$.

## Exemplos

Nos exemplos abaixo, considere 
$$f(x) = 3x + 2$$
$$g(x) = x^2 + 1$$

Então a soma $f + g$ pode ser calculada como 

$$(f + g)(x) = f(x) + g(x) =  3x+2 + x^2 +1 = x^2 + 3x + 3 $$

Usando um abuso de notação, podemos escrever $$f + f = 2f$$

O produto $f\cdot g$ pode ser calculado como

$$(f\cdot g)(x) = f(x)\cdot g(x) = (3x+2)(x^2 + 1) = 3x^3 + 2x^2 + 3x + 2$$

Novamente, abusando da notação, podemos escrever 
$$ f\cdot f = f^2$$

Podemos também calcular a divisão das funções $f/g$:

$$\frac{f}{g}(x) = \frac{f(x)}{g(x)} = \frac{3x + 2}{x^2+1} $$


Lembre-se que nos reais, também podemos tirar raízes quadradas, entaõ podemos definir $\sqrt{f}$

$$\sqrt{f}(x) = \sqrt{3x+2}$$

Nas expressões acima, temos que tomar cuidado com algumas coisas: será que $f/g$ está bem definda? Será que $\sqrt{f}$ está bem definida?

## Domínios

Sempre que definimos uma função através de uma expressão, temos que tomar cuidado com o domínio no qual aquela expressão tem sentido. Vamos usar as regras fundamentais dos números reais:

1. Não podemos dividir por zero
2. Não podemos tirar uma raíz quadrada de um número negativo.
3. Não podemos tirar logaritmo de um número não-positivo. 

Aplique essas três regras, e use interseções de conjuntos quando aplicar mais do que uma regra ao mesmo tempo. 

## Exemplos

Qual o domínio das funções definidas pelas expressões abaixo:

1. $f(x) = 2x +1$
2. $g(x) = \frac{2x + 3}{x^2 - 4}$
3. $h(x) = 3x + \sqrt{4x + 2}$
4. $\ell(x) = \frac{\pi}{\sqrt{2x}} + \frac{1}{x - 5}$






---

<div class="grid cards" markdown>
 - [Slides :material-presentation-play:](./aula03-slides.md)
 - [Exercícios :writing_hand:](./questoes03.pdf)
</div>
