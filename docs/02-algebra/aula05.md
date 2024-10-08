# Polinômios

Um polinômio numa variável $x$ é uma expressão da forma

$$a_0 + a_1x + a_2x^2 + \ldots a_nx^n$$

com os $a_i$ números chamados **coeficientes**. O **grau** desse polinômio é $n$. 

Podemos operar polinômios.

## Soma e subtração

São operações feitas somando os coeficientes de mesmo grau. 
Sendo $p = 1 + 2x + x^2$ e $q = 4x + x^2 + x^3$ temos
$$p + q =  1 + 2x + x^2 + 4x + x^2 + x^3 = 1 + 6x + 2x^2 + x^3$$

## Multiplicação

É feita usando-se a propriedade distributiva da multiplicação.
Sendp $p = 1 + 3x$ e $q = 2 - 4x$ então 
$$p\cdot q = (1+3x)(2-4x) = 2 - 4x + 6x - 12 x^2 = 2 - 2x - 12x^2$$

## Divisão

Aqui, utilizamos a divisão euclidiana (com resto). 
Sendo $p = x^2 + 3x + 1$ e $q = x + 1$ temos 
$$p\div q =  x + 2 \text{ com resto } -1$$

## Valor numérico

Quando substituímos o valor de $x$ por um número, obtemos um valor numérico.

Se $p(x) = 2x^2 + 3x +1$ então $p(-1) = 0$

## Raízes

Dizemos que $x$ é uma _raíz_ de um polinômio $p$ se $p(x) = 0$. 

## Raízes e fatoração

Sempre que você achar uma raíz de um polinômio, você consegue fatorar ele. 
Se um polinômio $p(x)$ tem raíz $a$, então $p(x)$ pode ser dividido pelo monõmio $x-a$.

## Fórmulas para as raízes

Alguns polinômios possuem fórmulas para encontrar suas raízes através dos seus coeficientes:

- polinômios de primeiro grau: resolve como equação
- polinômios de segundo grau: fórmula de Bhaskara
- polinômios de terceiro grau: fórmula de [Cardano-Tartaglia](https://medium.com/20-21/a-f%C3%B3rmula-de-cardano-tartaglia-para-equa%C3%A7%C3%B5es-do-3%C2%BA-grau-e7273b816609)
- polinômios de quarto grau: fórmula de [Ferrari](https://www.fisica.net/FaceBook/Equacao-do-quarto-grau.pdf)
- polinômios de grau maior que cinco: o matemático Evariste Galois provou que não existe uma fórmula geral para resolver esse tipo de polinômio



## Relações de Girard

Relacionam as raízes de um polinômio com seus coeficientes. 


Sendo
$$p(x) = x^3 + ax^2 + bx + c$$
podemos supor que $p$ tenha raízes $r_1, r_2, r_3$, de modo que 
$$p(x) = (x-r_1)(x-r_2)(x-r_3)$$


Deselvolvendo a segunda fórmula, obtemos as igualdades

$$\begin{align*}
a &= -(r_1 + r_2 + r_3) & \text{-soma das raízes}\\
b &= r_1r_2 + r_2r_3 + r_3r_1 & \text{soma dos produtos 2 a 2} \\
c &= -r_1r_2r_3 & \text{-produto das raízes}
\end{align*}
$$


---

<div class="grid cards" markdown>
 - [Slides :material-presentation-play:](./aula05-slides.md)
 - [Exercícios :writing_hand:](./questoes05.pdf)
</div>
