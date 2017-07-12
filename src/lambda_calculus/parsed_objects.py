class Expression(object):
    def __init__(self, function, function_name, sub_expression, domain, image):
        self._function = function
        self._function_name = function_name
        self._sub_expression = sub_expression
        self._domain = domain
        self._image = image

    def __str__(self):
        return self._function_name + '(' + str(self._sub_expression) + ')'

class Variable(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return str(self._name)

class Constante(Expression):
    def __init__(self, value):
        identity = lambda x : x
        super(Constante, self).__init__(identity, "cte", int(value), None, int)
        self._value = int(value)

    def __str__(self):
        return str(self._value)

class Booleano(Expression):
    def __init__(self, boolean):
        identity = lambda x : x
        super(Booleano, self).__init__(identity, "cte", boolean, None, bool)
        self._value = boolean

    def __str__(self):
        return str(self._value)

class Application(Expression):
    def __init__(self, first, second):
        self._first = first
        self._second = second

    def __str__(self):
        return str(self._first) + str(self._second)

class Abstraction(Expression):
    def __init__ (self, variable, variable_type, body):
        super(Abstraction, self).__init__(body._function, body._function_name, body, variable_type, body._image)
        self._body = body
        self._variable = variable

    def __str__(self):
        return '(\\' + str(self._variable) + ':' + str(self._domain) + '.' + str(self._body) + ')'
