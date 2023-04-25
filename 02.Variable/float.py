"""
Tipo de Float

Em Python, "float" é um tipo de dados numérico que representa números de ponto flutuante, ou seja, números que podem ter uma parte fracionária. É uma abreviação de "floating point number".

O tipo de dados "float" é utilizado para representar números *reais* e pode ser utilizado para realizar operações matemáticas com números com parte fracionária. Em Python, os números float são escritos com um ponto *decimal* (por exemplo, 3.14). É importante notar que os números float não podem representar todos os números reais com precisão, devido à forma como eles são armazenados em um computador, portanto, alguns erros de arredondamento podem ocorrer durante cálculos.

#Errado NO PONTO DO FLOAT, MAS GERA UMA TUPLA:
valor = 1, 44
print(valor)
print(type(valor))
=tuple

#Certo NO PONTO DE VISTA FLOAT: 
valor = 1.44
print(valor)
print(type(valor))
=float

O que é Tuple e float?

Tuple e float são dois tipos de dados diferentes em Python.

Um "tuple" é uma sequência ordenada e imutável de valores, separados por vírgula e envolvidos por parênteses. Os valores dentro de um tuple podem ser de qualquer tipo de dados, incluindo outros tuples. Tuples são úteis para armazenar dados relacionados que precisam ser tratados como uma única unidade. Eles são criados usando parênteses, como por exemplo: (1, 2, 3).

Já um "float" é um tipo de dado numérico que representa um número de ponto flutuante, ou seja, um número com parte decimal. O tipo float é usado para realizar cálculos matemáticos com números reais. Floats são criados usando um ponto decimal, como por exemplo: 3.14159.

Em resumo, enquanto tuples são estruturas de dados para armazenar valores relacionados, floats são usados para representar números de ponto flutuante e realizar cálculos matemáticos com esses números.

O que é dupla atribuição?

Em Python, a dupla atribuição (também conhecida como "atribuição múltipla") é uma técnica que permite atribuir múltiplos valores a múltiplas variáveis em uma única linha de código.

Na dupla atribuição, os valores a serem atribuídos são colocados entre parênteses e separados por vírgulas, e as variáveis a receber esses valores também são separadas por vírgulas. A ordem dos valores e variáveis deve corresponder, ou seja, o primeiro valor é atribuído à primeira variável, o segundo valor à segunda variável, e assim por diante.

Por exemplo: #É POSSIVEL FAZER DUPLA ATRIBUIÇÃO
valor1, valor2 = 1 ,44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

Como converter um float para int?

Em Python, você pode converter um valor de ponto flutuante (float) para um valor inteiro (int) usando a função "int()". A conversão de float para int descarta a parte decimal do valor e retorna a parte inteira.

Por exemplo, suponha que você tenha um valor float 3.14 e queira convertê-lo para um valor inteiro:

Exemplo 01:

num_float = 3.14
num_int = int(num_float)
print(num_int)

Nesse exemplo, a função "int()" é usada para converter o valor 3.14 em um número inteiro, e o resultado é armazenado na variável "num_int". O valor impresso será 3, que é a parte inteira do número original.


obs: Ao converter float para inteiros, nós perdemos precisão.
Exemplo 02:

res = int(valor)
print(res)
print(type(res))


O que significa j em Python e numeros complexos?


Em Python, a letra "j" é usada para representar a unidade imaginária na notação complexa. Quando você adiciona "j" a um número, ele se torna um número complexo. Por exemplo, se você escrever "5j" em Python, ele será interpretado como o número complexo 5i, onde "i" é a unidade imaginária.

variavel = 5j
class 'complex'>

Um número complexo é um tipo de número que inclui tanto uma parte real quanto uma parte imaginária. Ele é expresso na forma a + bi, onde "a" representa a parte real e "b" representa a parte imaginária multiplicada pela unidade imaginária "i". A unidade imaginária é definida como a raiz quadrada de -1, ou seja, i² = -1.

"""