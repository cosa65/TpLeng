class Variable (object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return str(self._name)

    def __eq__(self, other):
        return isinstance(other, Variable) and other._name == self._name

    def normalform(self):
        return True

class Application (object):
    def __init__(self, first, second):
        self._first = first
        self._second = second

    def __str__(self):
        return str (self._first) + str (self._second)

    def __eq__(self, other):
        return isinstance (other, Application) and \
        (other._first == self._first) and  (other._second == self._second)

    def normalform(self):
        if isinstance(self._first,Abstraction) :
            return False
        elif isinstance(self._first,Application) :
            return self._first.normalform()
        else:
            return True

class Abstraction (object):
    def __init__ (self, variable, variable_type, body):
        self._variable = variable
        self._variable_type = variable_type
        self._body = body

        #if self._variable == self._body:
        #    self._identity = True
        #else:
        #    self._identity = False

        #if isinstance(self._body, Abstraction):
        #    if self._body._identity is True:
        #        pass

    def __str__(self):
        return '(\\' + str(self._variable) + ':' + str(self._variable_type) + '.' + str(self._body) + ')'

    def __eq__ (self, other):
        return isinstance (other, Abstraction) and \
        (other._variable == self._variable) and \
        (other._variable_type == self._variable_type) and \
        (other._body == self._body)

    def normalform(self):
        return True
