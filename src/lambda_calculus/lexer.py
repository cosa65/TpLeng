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

def t_error(t):
    print "error"

t_IF = r'if\ '
t_THEN = r'then'
t_ELSE = r'else'
t_ISZERO = r'iszero'
t_PRED = r'pred'
t_SUCC = r'succ'
t_ZERO = r'0'
t_NAT = r'[1-9]+'
t_TBOOL = r'Bool'
t_TNAT = r'Nat'
t_LAMBDA = r'\\'
t_ARROW = r'->'
t_ignore = ' \t'
# Asi hago que no me entre en conflicto el leer alguna variable con 
# las palabras claves
t_VAR = r'(?!succ|pred|iszero|if|then|else)[a-z]'

#t_APPLICATION = r''

literals = ['(', ')', ':', '.']

tokens = (
	'TBOOL',
	'TNAT',
	'BOOL',
	'NAT',
	'IF',
	'THEN',
	'ELSE',
	'ISZERO',
	'PRED',
	'SUCC',
	'VAR',
	'ARROW',
	'ZERO',
        'LAMBDA'
	)

# Build the lexer
lexer = lex.lex()

def apply_lexer(string):
    """Aplica el lexer al string dado."""
    lexer.input(string)

    return list(lexer)
