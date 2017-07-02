#! coding: utf-8
"""Calculator lexer example."""
import ply.lex as lex

"""
Lista de tokens

El analizador léxico de PLY (al llamar al método lex.lex()) va a buscar
para cada uno de estos tokens una variable "t_TOKEN" en el módulo actual.

Sí, es súper nigromántico pero es lo que hay.

t_TOKEN puede ser:

- Una expresión regular
- Una función cuyo docstring sea una expresión regular (bizarro).

En el segundo caso, podemos hacer algunas cosas "extras", como se
muestra aquí abajo.

"""

"""
V : true | false | \\x:T.M | n
M : x | true | false | if M1 then M2 else M3 | \\x:T.M | M1 M2 | 0 | succ(M) | pred(M) | iszero(M)
T : Bool | Nat | T1 -> T2
"""

def t_BOOL(t):
    r'true|false'
    t.value = True if (t.value == "true") else False
    return t

def t_NAT(t):
    r'(?!-)\d+'
    t.value = int(t.value)

t_IF = r'if '
t_THEN = r' then '
t_ELSE = r' else '
t_ISZERO = r'iszero'
t_PRED = r'pred '
t_SUCC = r'succ '
#t_OPEN_BRACKETS = r'('
#t_CLOSE_BRACKETS = r')'

t_ABSTRACTION = r'\\.:.*\..*'

#t_APPLICATION = r''

tokens = (
	'BOOL',
	'NAT',
	'IF',
	'THEN',
	'ELSE',
	'ISZERO',
	'OPEN_BRACKETS',
	'CLOSE_BRACKETS',
	'PRED',
	'SUCC',
	'ZERO',
	'VAR',
	'COLON',
	'DOT',
	'ABSTRACTION'
	)

# Build the lexer
lexer = lex.lex()

def apply_lexer(string):
    """Aplica el lexer al string dado."""
    lexer.input(string)

    return list(lexer)
