"""Parser LR(1) de calculadora."""
import ply.yacc as yacc
from .lexer import tokens

#precedence = [ 
#        ('left', 'PLUS'),
#        ('left', 'MINUS'),
#        ('left', 'TIMES')
#        ]

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
    'M : VAR'
    p[0] = p[1]

def p_abstraction(p):
    'M : ABSTRACTION VAR COLON M DOT M'
    p[0] = 1

#def p_app(p):
#    'M : ABSTRACTION TERM_VAR COLON T DOT M'
#    p[0] = 1

def p_error(p):
    print("Hubo un error en el parseo.")

    parser.restart()


# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(str):
    return parser.parse(str)
