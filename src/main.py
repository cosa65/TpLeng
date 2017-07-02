"""Archivo principal de Lambda Calculus parser."""
from lambda_calculus import parse

while True:
    try:
        exp_str = raw_input('calc> ')
    except EOFError:
        break
    print(parse(exp_str))
