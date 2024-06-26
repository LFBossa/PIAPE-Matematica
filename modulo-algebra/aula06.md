# O algoritmo de Briot-Ruffini

É um algoritmo feito para dividir um polinômio $p(x)$ qualquer por um monômio na forma $x-a$. 

Montamos uma tabela com 3 linhas.

- Na primeira linha escrevemos os coeficientes de $p(x)$, do coeficiente de maior grau para o de menor grau
- Na segunda linha, escrevemos $a$
- A terceira linha será usada para os cálculos

Se $p(x) = a_4x^4 + a_3x^3 + a_2x^2 + a_1x + a_0$, a tabela fica assim

|     | $a_4$ | $a_3$ | $a_2$ | $a_1$ | $a_0$ |
| --- | ----- | ----- | ----- | ----- | ----- |
| $a$ |       |       |       |       |       |
|     |       |       |       |       |       |


1. O passo inicial é descer o termo $a_4$ para a terceira linha. 

A partir de então, você repete os passos 2 e 3 até acabarem as colunas

2. Pegue o número que está na terceira linha gerado no passo anterior. Multiplique esse número por $a$ e escreva o resultado dessa multiplicação na segunda linha, uma coluna à frente.
3. Some o número obtido no passo anterior com o número da primeira linha que está acima dele. Escreva o resultado na terceira linha dessa mesma coluna.


## Exemplo numérico 

Seja $p(x) = 3x^4 -2x^3 + 2x^2 - x + 4$ e considere o monômio $x - 2$. Usando o algoritmo acima, inciamos a tabela como

|   | 3 | -2 | 2 | -1 | 4 |
| - | --- | --- | --- | --- | --- |
| 2 |     |     |     |     |     |
|   |     |     |     |     |     |

Passo 1.

|   | 3 | -2 | 2 | -1 | 4 |
| - | --- | --- | --- | --- | --- |
| 2 |     |     |     |     |     |
|   |  3  |     |     |     |     |

Passo 2.

|   | 3 | -2 | 2 | -1 | 4 |
| - | --- | --- | --- | --- | --- |
| 2 |     |   6  |     |     |     |
|   |  3  |     |     |     |     |

Passo 3.

|   | 3 | -2 | 2 | -1 | 4 |
| - | --- | --- | --- | --- | --- |
| 2 |     |   6  |     |     |     |
|   |  3  |  4   |     |     |     |

Passo 2.

|   | 3 | -2 | 2 | -1 | 4 |
| - | --- | --- | --- | --- | --- |
| 2 |     |   6  |  8  |     |     |
|   |  3  |  4   |     |     |     |

Passo 3.

|   | 3 | -2 | 2 | -1 | 4 |
| - | --- | --- | --- | --- | --- |
| 2 |     |   6  |  8  |     |     |
|   |  3  |  4   |  10  |     |     |


Passo 2.

|   | 3 | -2 | 2 | -1 | 4 |
| - | --- | --- | --- | --- | --- |
| 2 |     |   6  |  8  |  20   |     |
|   |  3  |  4   |  10  |     |     |

Passo 3.

|   | 3 | -2 | 2 | -1 | 4 |
| - | --- | --- | --- | --- | --- |
| 2 |     |   6  |  8  |  20   |     |
|   |  3  |  4   |  10  |  19   |     |

Passo 2.

|   | 3 | -2 | 2 | -1 | 4 |
| - | --- | --- | --- | --- | --- |
| 2 |     |   6  |  8  |  20   |   38  |
|   |  3  |  4   |  10  |  19   |     |


Passo 3.

|   | 3 | -2 | 2 | -1 | 4 |
| - | --- | --- | --- | --- | --- |
| 2 |     |   6  |  8  |  20   |   38  |
|   |  3  |  4   |  10  |  19   |   42  |

Assim, o resultado da divisão de $p(x) = 3x^4 -2x^3 + 2x^2 - x + 4$ por $x-2$ é $3x^3 + 4x^2 + 10x + 19$ com resto $42$.

## Observações

- Fique atento e complete os coeficientes zero.
- Fique atendo ao sinal do número $a$