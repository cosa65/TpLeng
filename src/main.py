"""Archivo principal de Lambda Calculus parser."""
from lambda_calculus import parse
from lambda_calculus import reduce_expression
import sys

inputs_file = sys.argv[1]

with open(inputs_file, 'r') as inputs:
    for input_line in inputs:
        input_entry, result = input_line.split(',')
        print "Input value: "
        print "----> " + input_entry
        output = reduce_expression(parse(input_entry))
        print "Output value: "
        if isinstance(output, str):
            print output
        else:
            print "----> " + str(output) + ":" + output.arity()
        print "Expected value: "
        print "----> " + result
        #output, arity = reduce_expression(parse(input_entry))
        #print "Output value: "
        #if isinstance(output, str):
        #    print output
        #else:
        #    print "----> " + str(output) + ":" + arity
        #print "Expected value: "
        #print "----> " + result
