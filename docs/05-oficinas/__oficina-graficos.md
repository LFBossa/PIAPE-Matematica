---
template: reveal.html
search:
  exclude: true
---
## Operações com gráficos

---

Conhecendo o gráfico de uma função, podemos aplicar operações algébricas para transformar esse gráfico.

Podemos deslocar, esticar, achatar, inverter, refletir. Cada operação dessas é feita utilizando alguma transformação algébrica.

---

Para as visualizações desses slides, estaremos usando o gráfico da função

$$f(x) = e^{-x^4 +2x^2 +\frac{x}{2}} + \frac{1}{1+e^{-x}} - \frac{1}{2} $$

Não se assuste com a complicação da expressão, o gráfico é mostrado na seguinte imagem

--

<img src="./05-oficinas/img/graficos-01.png" title="Gráfico de $f$" class="r-stretch" />

--

Escolhi esse gráfico pois ele é:
- assimétrico
- tem uma raiz
- possui máximos e mínimos locais bem distintos

---

## Deslocamento vertical

Para deslocar o gráfico na vertical, adicionamos uma constante a expressão de $f(x)$:

$$g(x) = f(x) + a$$

Dessa forma, o gráfico de $g$ é igual ao gráfico de $f$, apenas deslocado $a$ unidades para cima se $a$ é positivo, ou para baixo se $a$ for negativo.

--

$$g(x) = f(x) + 1$$

<img src="./05-oficinas/img/graficos-02.png" title="Gráfico de $g = f(x) + 1$" class="r-stretch" />


--

$$g(x) = f(x) - 2$$

<img src="./05-oficinas/img/graficos-03.png" title="Gráfico de $g = f(x) - 2$" class="r-stretch" />


---

## Deslocamento horizontal

Para deslocar o gráfico na horizontal, adicionamos uma constante no argumento da expressão $f(x)$:

$$g(x) = f(x + a)$$

Dessa forma, o gráfico de $g$ é igual ao gráfico de $f$, apenas deslocado $a$ unidades para a esquerda se $a$ é positivo, ou para a direita se $a$ for negativo.

--

$$g(x) = f(x + 2)$$

<img src="./05-oficinas/img/graficos-04.png" title="Gráfico de $g = f(x + 2)$" class="r-stretch" />


--

$$g(x) = f(x - \sqrt{5})$$

<img src="./05-oficinas/img/graficos-05.png" title="Gráfico de $g = f(x - \sqrt{5})$" class="r-stretch" />

---

## "Esticamento" vertical

Ao multiplicarmos a função por um número $a$ positivo, realizamos um alongamento ou uma compressão vertical. 

- Se $a > 1$, temos um alongamento vertical
- Se $0 < a < 1$, temos uma compressão vertical

--

$$g(x) = \frac{5}{3}f(x)$$

<img src="./05-oficinas/img/graficos-08.png" title="Gráfico de $g(x) = \frac{5}{3}f(x)$" class="r-stretch" />

--

$$g(x) = \frac{3}{7}f(x)$$

<img src="./05-oficinas/img/graficos-09.png" title="Gráfico de $g(x) = \frac{3}{7}f(x)$" class="r-stretch" />  

---

## "Esticamento" horizontal

Ao multiplicarmos o argumento da função por um número $a$ positivo, realizamos um alongamento ou uma compressão horizontal. 

- Se $a > 1$, temos uma compressão horizontal
- Se $0 < a < 1$, temos um alongamento horizontal

--

$$g(x)  = f(3x)$$

<img src="./05-oficinas/img/graficos-06.png" title="Gráfico de $g(x) = f(3x)$" class="r-stretch" />

--

$$g(x) =  f(\tfrac{1}{4}x)$$

<img src="./05-oficinas/img/graficos-07.png" title="Gráfico de $g(x) = f(\frac{1}{4}x)$" class="r-stretch" />

---

## Reflexões

Ao multiplicarmos a função ou seu argumento por $-1$ causamos uma reflexão.

- Reflexão vertical: multiplicar a função por $-1$
- Reflexão horizontal: multiplicar o argumento da função por $-1$

--

$$g(x) = -f(x)$$

<img src="./05-oficinas/img/graficos-10.png" title="Gráfico de $g(x) = -f(x)$" class="r-stretch" />

--

$$g(x) = f(-x)$$

<img src="./05-oficinas/img/graficos-11.png" title="Gráfico de $g(x) = f(-x)$" class="r-stretch" />



