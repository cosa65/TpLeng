"""Parser LR(1) de calculadora."""
import ply.yacc as yacc
from .lexer import tokens
from .parsed_objects import *

#precedence = [ 
#        ('left', 'PLUS'),
#        ('left', 'MINUS'),
#        ('left', 'TIMES')
#        ]

def p_M_if_then_else(p):
    'M : IF M THEN M ELSE M'
    # Check if both parts have the same type
    if type(p[4]) == type(p[6]):
        p[0] = p[4] if p[2] else p[6]
    else:
        p[0] = "Error de tipos"

def p_M_bool(p):
    'M : BOOL'
    p[0] = p[1]

def p_M_nat(p):
    'M : NAT'
    p[0] = p[1]

def p_iszero(p):
    '''M : ISZERO '(' M ')' '''
    p[0] = p[3] == 0

def p_pred(p):
    '''M : PRED '(' M ')' '''
    p[0] = int(p[3]) - 1

def p_succ(p):
    '''M : SUCC '(' M ')' '''
    p[0] = int(p[3]) + 1

def p_ZERO(p):
    'M : ZERO'
    p[0] = 0

def p_term_var(p):
    'M : VAR'
    p[0] = p[1]

def p_bool(p):
    'T : TBOOL'
    p[0] = p[1]

def p_nat(p):
    'T : TNAT'
    p[0] = p[1]

def p_function(p):
    'T : T ARROW T'
    p[0] = (p[1], p[3])

def p_abstraction(p):
    '''M : LAMBDA VAR ':' T '.' M'''
    p[0] = Abstraction(p[2], p[4], p[6])

#def p_app(p):
#    'M : M M'
#    p[0] = p[1]( p[2] )

def p_error(p):
    print("Vayan a fumar droga")

    parser.restart()


# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(str):
    return parser.parse(str)
