import ply.yacc as yacc
from .lexer import tokens

def p_M_if_then_else(p):
	'M : IF M THEN M ELSE M'
	p[0] = p[4] if p[2] else p[6]

def p_M_bool(p):
	'M : BOOL'
	p[0] = p[1]

def p_M_nat(p):
	'M : NAT'
	p[0] = p[1]

def p_iszero(p):
	'M : ISZERO OPEN_BRACKETS M CLOSE_BRACKETS'
	p[0] = p[3] == 0

def p_pred(p):
	'M : PRED OPEN_BRACKETS M CLOSE_BRACKETS'
	p[0] = p[3] - 1

def p_succ(p):
	'M : SUCC OPEN_BRACKETS M CLOSE_BRACKETS'
	p[0] = p[3] + 1

def p_zero(p):
	'M : ZERO'
	p[0] = 0

def p_term_var(p):
	'M : TERM_VAR'
	p[0] = p[1]

def p_abstraccion(p):
	'M : LAMBDA TERM_VAR COLON T DOT M'
	p[0] = 

def p_app(p):

def p_error(p):
    print("Hubo un error en el parseo.")
    parser.restart()