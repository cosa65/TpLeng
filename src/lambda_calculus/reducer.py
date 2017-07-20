from parsed_objects import *

def is_normal_form(expression):
    return isinstance(expression, Variable) or isinstance(expression, ConstantExpression) or isinstance(expression, Abstraction) or isinstance(expression, BooleanExpression)

def recursive_reduce():
    if isinstance(t, Variable) or isinstance(t, Abstraction):
        return t

    elif isinstance(t, Application):
        if isinstance(t._first, Abstraction):
            return recursive_substitution(t._first._body, t._first._variable, t._second)
        else:
# recurse on first element of Application until
# it is fully reduced, then move on to second element
            new_first = recursive_reduce(t._first)
            if new_first != t._first:
                t._first = new_first
                return t
            else:
                t._second = recursive_reduce(t._second)
                return t

def reduce_expression(expression):

    if is_normal_form(expression):
        # no reduction to be done
        return expression

    elif isinstance(expression, ArithmeticExpression):
        reduced_sub_expression = reduce_expression(expression._sub_expression)
        if isinstance(reduced_sub_expression, ConstantExpression):
            return ConstantExpression(expression._function(reduced_sub_expression._value))
        else:
            return "Error type: Expected type Nat"

    elif isinstance(expression, Conditional):
        reduced_conditional = reduce_expression(expression._condition_expression)
        if isinstance(reduced_conditional, BooleanExpression):

            reduced_expression_if_true = reduce_expression(expression._expression_if_true)
            reduced_expression_if_false = reduce_expression(expression._expression_if_false)

            if type(reduced_expression_if_true) == type(reduced_expression_if_false):

                return reduced_expression_if_true if reduced_conditional._value else reduced_expression_if_false

            else:
                return "The resulting expressions of conditionals must have the same type"
        else:
            return "Errot type: Expected type boolean"

    elif isinstance(expression, Application): 
        lambda_expression = expression._lambda_expression
        parameter_expression = expression._parameter_expression
        if isinstance(lambda_expression, Abstraction):
            if lambda_expression._domain == parameter_expression._image:
                #recursive_substituion(lambda_expression._body, parameter_expression._value)
                reduce_expression(lambda_expression._body)
            else:
                return "Type parameter error"
        else:
            return "The aplication must be done to a lambda expression"
        
        #tmp_expression = expression

        #while(True):
        #    expression_str = str(tmp_expression) #objectify expression
        #    reduced_expression = recursive_reduce(tmp_expression)
        #    reduced_expression_str = str(reduced_expression)

        #    if expression_str == reduced_expression_str:
        #        # if fully reduced
        #        return tmp_expression
        #    else:
        #        # continue on if theres more to do
        #        tmp_expression = reduced_expression

"""
def recursive_substitution(old, substituter, new):
    # Variable
    # check if substituter matches var
    if isinstance(old, Variable):
        if old._name == substituter._name:
            return new

    # Application
    # since Application : Term Term, recurse on both 
    # terms to eventually get to Variable case above
    elif isinstance(old, Application):
        old._first = recursive_substitution(old._first, substituter, new)
        old._second = recursive_substitution(old._second, substituter, new)

    # Abstraction
    # if the variable in the abstraction matches the substituter,
    # want to get to Variable case above
    # else, recurse on body for same reason
    elif isinstance(old, Abstraction):
        if old._variable == substituter:
            old._variable = recursive_substitution(old._variable, substituter, new)
            old._body = recursive_substitution(old._body, substituter, new)

return old
"""
#
#
#def beta_reduce(term):
#
## inner function to recursively reduce until a Variable or
## Abstraction is reached, following the steps lined out in
## http://www.cs.yale.edu/homes/hudak/CS201S08/lambda.pdf
#
#def recursive_reduce(t):
