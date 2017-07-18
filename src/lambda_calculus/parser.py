#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parser LR(1) de calculadora."""
import ply.yacc as yacc
from .lexer import tokens
from .parsed_objects import *

precedence = [
                ("left", "uARROW"),
                ("left", "uLAMBDA"),
                ("left", "uIF"),
                ("left", "uAPP")
        ]

def p_M_if_then_else(p):
    'M : IF M THEN M ELSE M %prec uIF'
    condition = p[2]
    expression_if_true = p[4]
    expression_if_false = p[6]
    p[0] = Conditional(condition, expression_if_true, expression_if_false)

def p_M_bool(p):
    'M : BOOL'
    p[0] = BooleanExpression(p[1])

def p_M_nat(p):
    'M : NAT'
    p[0] = ConstantExpression(p[1])

def p_iszero(p):
    '''M : ISZERO '(' M ')' '''
    check_zero = lambda x: x == 0
    expression = p[3]
    p[0] = BooleanExpression(check_zero, 'iszero', expression, int, bool)

def p_pred(p):
    '''M : PRED '(' M ')' '''
    pred = lambda x: x - 1
    expression = p[3]
    p[0] = ArithmeticExpression(expression, pred, 'pred')

def p_succ(p):
    '''M : SUCC '(' M ')' '''
    succ = lambda x: x + 1
    expression = p[3]
    p[0] = ArithmeticExpression(expression, succ, 'succ')

def p_ZERO(p):
    'M : ZERO'
    p[0] = ConstantExpression(0)

def p_term_var(p):
    'M : VAR'
    p[0] = Variable(p[1])

def p_bool(p):
    'T : TBOOL'
    p[0] = bool

def p_nat(p):
    'T : TNAT'
    p[0] = int

def p_function(p):
    'T : T ARROW T %prec uARROW'
    p[0] = (p[1], p[3])

def p_abstraction(p):
    '''M : LAMBDA VAR ':' T '.' M %prec uLAMBDA '''
    # Chequear que las variables de M esten ligadas
    expression = p[6]
    variable_type = p[4]
    variable = p[2]
    p[0] = Abstraction(variable, variable_type, expression)
    #if expression._domain == variable_type:
    #else:
    #    print "Type error"

def p_application(p):
    'M :  M M %prec uAPP'
    expression1 = p[2]
    expression2 = p[4]
    p[0] = Application(expression1, expression2)
    #if isinstance(expression1, Abstraction):
    #    if expression1._domain == expression2._image and isinstance(expression2, Constante):
    #        # Guardo el resultado de aplicar el valor de expression2
    #        # A la función de expression1
    #        p[0] = expression1._function(expression2._value)
    #    else:
    #        print "Type error"
    #else:
    #    p[0] = Application(expression1, expression2)

#def p_expression(p):
#    '''M : '(' M ')' '''
#    expression = p[2]
#    p[0] = Expression(expression)

def p_error(p):
    print("Vayan a fumar droga")

    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)

def apply_parser(str):
    return parser.parse(str)
