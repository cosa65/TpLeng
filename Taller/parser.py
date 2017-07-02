"""Parser LR(1) de calculadora."""
import ply.yacc as yacc
from .lexer import tokens

precedence = [ 
        ('left', 'PLUS'),
        ('left', 'MINUS'),
        ('left', 'TIMES')
        ]

def p_expression_plus(p):
    'expression : expression PLUS NUMBER'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : term MINUS NUMBER'
    p[0] = p[1] - p[3]

def p_expression_times(p):
    'expression : term TIMES NUMBER'
    p[0] = p[1] * p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_number(p):
    'term : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Hubo un error en el parseo.")

    parser.restart()


# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(str):
    return parser.parse(str)
