#def convert_to_type(t):
types = {
          int: "Nat",
          bool: "Bool",
          None: ""
        }
    #if isinstance(t, FunctionType):
    #    t._domain = types[t._domain]
    #    convert_to_type(t._image)
    #else:
    #    t = types[t]
replace_type_list = {"<type 'int'>": "Nat", 
                     "<type 'bool'>": "Bool"
                     }

class Expression(object):
    def __init__(self, domain, image):
        self._domain = domain
        self._image = image

    def arity(self):
        output = str()
        if self._domain is None:
            for tipe in replace_type_list.keys():
                output = output.replace(tipe, replace_type_list[tipe])
        else:
            output += str(self._domain)
            output += "->"
            output += str(self._image)
            for tipe in replace_type_list.keys():
                output = output.replace(tipe, replace_type_list[tipe])

        return output

        """
        if self._domain is None:
            if isinstance(self._domain, FunctionType):
                return str(self._image)
            else:
                return types[self._image]
        else:
            output = str()
            if isinstance(self._domain, FunctionType):
                output += str(self._domain)
            else:
                output += types[self._domain]

            output += "->"
            if isinstance(self._image, FunctionType):
                output += str(self._image)
            else:
                output += types[self._image]

            return output
        """

    def __str__(self):
        return self._function_name + '(' + str(self._sub_expression) + ')'

class Conditional(Expression):
    def __init__(self, condition, expression_if_true, expression_if_false):
        super(Conditional, self).__init__(None, expression_if_true._image)
        self._condition_expression = condition
        self._expression_if_true = expression_if_true
        self._expression_if_false = expression_if_false

    def __str__(self):
        return "if " + str(self._condition_expression) + " then " + \
                str(self._expression_if_true) + " else " + str(self._expression_if_false)

class ConstantExpression(Expression):
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
    def __init__(self, boolean):
        super(BooleanExpression, self).__init__(None, bool)
        self._value = boolean

    def __str__(self):
        return str(self._value)

class FunctionType(object):
    def __init__(self, domain, image):
        self._domain = domain
        self._image = image

    def __str__(self):
        return str(self._domain) + "->" + str(self._image)

class ArithmeticExpression(Expression):
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
    def __init__(self, lambda_expression, parameter_expression):
        self._lambda_expression = lambda_expression
        self._parameter_expression = parameter_expression

    def __str__(self):
        return str(self._lambda_expression) + str(self._parameter_expression)

class Abstraction(Expression):
    def __init__ (self, variable, variable_type, body):
        if isinstance(body, Variable):
            super(Abstraction, self).__init__(variable_type, variable_type)
        elif isinstance(body, Abstraction):
            super(Abstraction, self).__init__(variable_type, FunctionType(body._domain, body._image))
        else:
            super(Abstraction, self).__init__(variable_type, body._image)
        self._body = body
        self._variable = variable
        if isinstance(body, Abstraction):
            self._context = body._context
            self._context.append((variable, variable_type))
        else:
            self._context = [(variable, variable_type)]

    def __str__(self):
        if isinstance(self._domain, FunctionType):
            return '\\' + str(self._variable) + ':' + str(self._domain) + '.' + str(self._body)
        else:
            return '\\' + str(self._variable) + ':' + types[self._domain] + '.' + str(self._body)
