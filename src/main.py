"""Archivo principal de Lambda Calculus parser."""
from lambda_calculus import parse

while True:
    try:
        exp_str = raw_input('calc> ')
    except EOFError:
        break
    # Falta la parte donde se reduce la expresion
    print(parse(exp_str))
