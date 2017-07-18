types = {
          int: "Nat",
          bool: "Bool",
          None: ""
        }

class Expression(object):
    def __init__(self, domain, image):
        self._domain = domain
        self._image = image

    def arity(self):
        if self._domain is None:
            return types[self._image]
        else:
            return types[self._domain] + "->" + types[self._image]

    def __str__(self):
        return self._function_name + '(' + str(self._sub_expression) + ')'

class Conditional(Expression):
#class Conditional(object):
    def __init__(self, condition, expression_if_true, expression_if_false):
        super(Conditional, self).__init__(None, expression_if_true._image)
        self._condition_expression = condition
        self._expression_if_true = expression_if_true
        self._expression_if_false = expression_if_false

    def __str__(self):
        return "if " + condition + " then " + \
                str(expression_if_true) + " else " + str(expression_if_false)

class ConstantExpression(Expression):
#class ConstantExpression(object):
    def __init__(self, value):
        super(ConstantExpression, self).__init__(None, int)
        self._value = int(value)

    def __str__(self):
        begin = str()
        end = str()
        for _ in range(self._value):
            begin += "succ(" 
            end += ")"
        return begin + "0" + end 

class BooleanExpression(Expression):
#class BooleanExpression(object):
    def __init__(self, boolean):
        super(BooleanExpression, self).__init__(None, bool)
        self._value = boolean

    def __str__(self):
        return str(self._value)

class ArithmeticExpression(Expression):
#class ArithmeticExpression(object):
    def __init__(self, sub_expression, arithmetic_function, arithmetic_function_name):
        super(ArithmeticExpression, self).__init__(int, int)
        self._sub_expression = sub_expression
        self._function = arithmetic_function
        self._function_name = arithmetic_function_name

    def __str__(self):
        return self._function_name + "(" + str(self._sub_expression) + ")" 

class Variable(Expression):
    def __init__(self, name):
        super(Variable, self).__init__(None, None)
        self._name = str(name)

    def __str__(self):
        return self._name

class Application(Expression):
    def __init__(self, first, second):
        self._first = first
        self._second = second

    def __str__(self):
        return str(self._first) + str(self._second)

class Abstraction(Expression):
    def __init__ (self, variable, variable_type, body):
        if isinstance(body, Variable):
            super(Abstraction, self).__init__(variable_type, variable_type)
        else:
            super(Abstraction, self).__init__(variable_type, body._image)
        self._body = body
        self._variable = variable

    def __str__(self):
        return '(\\' + str(self._variable) + ':' + types[self._domain] + '.' + str(self._body) + ')'
