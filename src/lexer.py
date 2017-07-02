import ply.lex as lex

'''
V : true | false | \x:T.M | n
M : x | true | false | if M1 then M2 else M3 | \x:T.M | M1 M2 | 0 | succ(M) | pred(M) | iszero(M)
T : Bool | Nat | T1 -> T2
'''

t_BOOL(t):
	r'true|false'
	t.value = True if (t.value == "true") else False
	return t

t_NAT(t):
	r'(?!-)\d+'
	t.value = int(t.value)

t_IF = r'if '
t_THEN = r' then '
t_ELSE = r' else '
t_ISZERO = r'iszero'
t_OPEN_BRACKETS = r'('
t_CLOSE_BRACKETS = r')'

t_FUNCTION = r'\\.:.*\..*'

#t_APPLICATION = r''

tokens = (
	'BOOL',
	'NAT',
	'IF',
	'THEN',
	'ELSE',
	'ISZERO',
	'OPEN_BRACKETS',
	'CLOSE_BRACKETS'
	'FUNCTION',
	)

def apply_lexer(string):
	lexer.input(string)
	return list(lexer)

lex.lex()