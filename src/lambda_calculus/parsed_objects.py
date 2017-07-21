replace_type_list = {"<type 'int'>": "Nat", 
                     "<type 'bool'>": "Bool"
                     }

def replace_types(string):
    string = str(string)
    for tipe in replace_type_list.keys():
        if tipe in string:
            string = string.replace(tipe, replace_type_list[tipe])

    return string

class Expression(object):
    def __init__(self, domain, image, context):
        self._domain = domain
        self._image = image
        self._context = context

    def arity(self):
        if self._domain is None:
            return replace_types(self._image)
        else:
            return replace_types(self._domain) + "->" + replace_types(self._image)

    def __str__(self):
        return self._function_name + '(' + str(self._sub_expression) + ')'

class Conditional(Expression):
    def __init__(self, condition, expression_if_true, expression_if_false):
        super(Conditional, self).__init__(None, expression_if_true._image, {})
        self._condition_expression = condition
        self._expression_if_true = expression_if_true
        self._expression_if_false = expression_if_false

    def __str__(self):
        return "if " + str(self._condition_expression) + " then " + \
                str(self._expression_if_true) + " else " + str(self._expression_if_false)

class ConstantExpression(Expression):
    def __init__(self, value):
        super(ConstantExpression, self).__init__(None, int, {})
        self._value = int(value)

    def __str__(self):
        begin = str()
        end = str()
        for _ in range(self._value):
            begin += "succ(" 
            end += ")"
        return begin + "0" + end 

class BooleanExpression(Expression):
    def __init__(self, boolean):
        super(BooleanExpression, self).__init__(None, bool, {})
        self._value = boolean

    def __str__(self):
        return str(self._value)

class FunctionType(object):
    def __init__(self, domain, image):
        self._domain = domain
        self._image = image

    def __str__(self):
        return "(" + str(self._domain) + "->" + str(self._image) + ")"

class ArithmeticExpression(Expression):
    def __init__(self, sub_expression, arithmetic_function, arithmetic_function_name):
        super(ArithmeticExpression, self).__init__(int, int, sub_expression._context)
        self._sub_expression = sub_expression
        self._function = arithmetic_function
        self._function_name = arithmetic_function_name

    def __str__(self):
        return self._function_name + "(" + str(self._sub_expression) + ")" 

class Variable(Expression):
    def __init__(self, name):
        super(Variable, self).__init__(None, None, {name: None})
        self._name = name

    def __str__(self):
        return self._name

class Application(Expression):
    def __init__(self, lambda_expression, parameter_expression):
        super(Application, self).__init__(lambda_expression._domain, lambda_expression._image, {})
        self._lambda_expression = lambda_expression
        self._parameter_expression = parameter_expression

    def __str__(self):
        return str(self._lambda_expression) + " " + str(self._parameter_expression)

class Abstraction(Expression):
    def __init__ (self, variable, variable_type, body):
        context = body._context
        if variable in context:
            if context[variable] is None:
                context[variable] = variable_type
            else:
                # Esto lo hago para que tire error luego
                context[variable + "2"] = None
        else:
            context[variable] = variable_type

        if isinstance(body, Variable):
            super(Abstraction, self).__init__(variable_type, variable_type, context)
        elif isinstance(body, Abstraction):
            super(Abstraction, self).__init__(variable_type, FunctionType(body._domain, body._image), context)
        else:
            super(Abstraction, self).__init__(variable_type, body._image, context)
        self._body = body
        self._variable = variable

    def __str__(self):
        return '\\' + str(self._variable) + ':' + replace_types(self._domain) + '.' + str(self._body)
