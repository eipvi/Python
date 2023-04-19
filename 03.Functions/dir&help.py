"""
Funções DIR E HELP no Python
UTILITÁRIOS Python para auxiliar na programação.

dir--> Apresenta todos os atributos/propriedades e funções/métodos disoiníveis para determinado tipo de dados ou variável.

help--> Apresenta a documentação/como utilizar os atributos/propriedades e funções/métodos disponiveis para determinado tipo de dado ou variável

dir e help--> geralmente são usadas no modo interativo, somente para obter informações rápidas.



-DIR
Apresenta todos os atributos e funções/métodos disponiveis para determinado tipo de dado ou variável.

O dir() retorna todas as propriedades e métodos do objeto especificado. Vamos tentar entender através de exemplos:

dir(int)
 ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', 
'__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', 
'__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', 
'__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', 
'__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__',
'__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__',
'__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__',
'__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
'__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
'__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate',
'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

Exemplos:
Pode por exemplo, usar o dir para obter informações dos métodos do int ou input:

dir(input)
 ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', 
'__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__text_signature__']



-HELP
Ele nos fornece uma breve explicação de como implementa o método e informa qual a utilidade dele.

Exemplos:
Nos exemplos do dir obtemos informações dos métodos da biblioteca math. Com a função help agora podemos saber o que cada uma faz:

import math as ma

>>> dir(ma)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 
 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 
 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod',
 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 
 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

>>> help(ma.sqrt)
Help on built-in function sqrt in module math:
sqrt(x, /)
 Return the square root of x.

 Obtemos que na biblioteca math a função sqrt retorna a raiz do número passado por parâmetro.

Podemos também, verificar o que faz o método .lower() do tipo de dados string:

help("Hello World".lower)
Help on built-in function lower:

lower() method of builtins.str instance
 Return a copy of the string converted to lowercase.

 Com isso, a função help() nos auxilia quando necessitamos de informações sobre determinada função ou método disponível.

 
 Resumo:

 q = Voltar
 "".upper() = Deixa tudo maiúsculo
 help("x".title) = Tirar dúvida de como fazer
 'palavra'.title() = 'Palavra' letra do primeiro nome em maiusculo 
 'PALAVRA'.lower().title() = Transforma a palavra em letra minuscula em seguida transforma e em minuscula mas com a primeira letra em maiscula, ex: Palavra.
 help(4.real) = ERRO, TENTE: num = 4 enter help(num.real)
 print(dir('objetivo')) = Usado para imprimir o que deseja


 Strings: As strings são usadas para armazenar informações de texto em uma variedade de aplicativos, como processadores de texto, editores de código, programas de banco de dados e aplicativos da Web. Elas também podem ser manipuladas e processadas por meio de funções específicas, como concatenação, substituição, extração e comparação de strings. Em muitas linguagens de programação, as strings são definidas entre aspas duplas ("") ou simples ('').
"""