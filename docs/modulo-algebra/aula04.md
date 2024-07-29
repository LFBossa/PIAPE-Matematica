# Raízes numéricas

Definição de raíz n-ésima

> A raíz n-ésima de um número $a$ é um número $b$ que satisfaz a propriedade de que, quando elevado a n-ésima potência, resulta no número $a$.

$$\sqrt[n]{a} = b \quad \Leftrightarrow \quad b^n = a$$

Lembrando que: raiz quadrada é _sempre_ positiva. 

- Correto: $\sqrt{25} = 5$
- Incorreto: $\sqrt{25} = \pm5$

Mas por que quando resolvemos equações, aparecem duas raízes?

Por causa do _módulo_. 

$$\sqrt{x^2} = |x|$$

Assim, por exemplo

$$x^2 = 25$$
$$\sqrt{x^2} = \sqrt{25}$$
$$|x| = 5$$
$$x = 5 \text{ ou } x = -5$$

## Propriedades da raiz

$$\sqrt[n]{a\cdot b} = \sqrt[n]{a}\cdot \sqrt[n]{b}$$
$$\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$$
$$\left(\sqrt[n]{a}\right)^m = \sqrt[n]{a^m}$$
$$\sqrt[p]{\sqrt[n]{a}} = \sqrt[pn]{a}$$


## Multiplicação de raízes de índices diferentes

Apenas usando as propriedades acima, não é possível simplificar um produto do tipo 
$$\sqrt[3]{4}\sqrt{5}$$


Lembrando o conteúdo visto na [Aula 02](./aula02.md), raízes são potências fracionárias

$$\sqrt{x} = x^{\frac{1}{2}}$$

Em geral, 

$$\sqrt[n]{x} = x^{\frac{1}{n}}$$

Assim, podemos encontrar um radical comum entre ambas:

$$\sqrt[3]{4} = 4^{1/3} = 4^{2/6}$$

$$\sqrt{5} = 5^{1/2} = 5^{3/6}$$

Assim:

$$\sqrt[3]{4}\sqrt{5} =  4^{1/3}\cdot 5^{1/2} = 4^{2/6}\cdot 5^{3/6} = \sqrt[6]{4^2}\cdot \sqrt[6]{5^3} = \sqrt[6]{4^2\cdot 5^3} $$


## Racionalização

Consiste em eliminar uma raiz do denominador de uma fração. Para tal, podemos usar algumas técnicas.

### Multiplicar por 1

Se o denominador é uma raiz simples, multiplicamos a fração por 1, porém na forma _raiz/raiz_.

$$\frac{3}{\sqrt{5}} = \frac{3}{\sqrt{5}}\cdot 1 = \frac{3}{\sqrt{5}}\cdot \frac{\sqrt{5}}{\sqrt{5}} = \frac{3\sqrt{5}}{5}$$

### Multiplicar pelo conjugado 

Se o denominador for da forma _número + raiz_, multiplicamos pelo seu **conjugado** _número - raiz_. Assim, utilizamos o produto notável 
$$(a-b)(a+b) = a^2 - b^2$$

$$\frac{4}{1 + \sqrt{2}} = \frac{4}{1 + \sqrt{2}}\cdot \frac{1 - \sqrt{2}}{1 - \sqrt{2}}$$

## Resolvendo equações com raiz

Note que temos que usar o módulo

$$(x+1)^2 = 9$$
$$\sqrt{(x+1)^2} = \sqrt{9}$$
$$|x+1| = 3$$
Assim, $x+1 = 3$ ou $x+1 = -3$.0 Resolvendo cada equação, temos $x= 2$ ou $x = -4$.