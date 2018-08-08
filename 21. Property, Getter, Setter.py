""" This program defines the usage of getter and setter and
    compare the method to use the same along with the property().
"""


""" Without Getter, Setter and Property() """
class myClass:
    def __init__(self, value=0):
        self.value = value

x = myClass(10)
print(x.value)


""" Using Getter and Setter """
class myClass:
    def __init__(self, value=0):
        self.setValue(value)

    def setValue(self,value):
        self.value = value

    def getValue(self):
        return self.value

x = myClass(40)
x.setValue(250)
print(x.getValue())


""" Using Property()
    Using property() we set the functions to call for get, set, delete etc operations.
    Syntax : property(fget=None, fset=None, fdel=None, doc=None)
"""
class myClass:
    def __init__(self, value=0):
        self.setValue(value) #  or self.value = value --> both works as same

    def setValue(self,value):
        print("Setting Value")
        self._value = value #  use the variable with a leading _.

    def getValue(self):
        print("Getting value")
        return self._value #  use the variable with a leading _.

    value = property(getValue, setValue)

x = myClass(12)     # this will call the setValue() from __init__
print(x.getValue()) # this will call the getValue() directly
print(x.value) # this will also call the getValue() as property is set with the function



""" Using property() in python recommended way """
class myClass:
    def __init__(self, value=0):
        self.value = value #  cannot use _value here in this method

    @property
    def value(self):
        print("Getting value")
        return self._value #  use the variable with a leading _.

    @value.setter
    def value(self,value):
        print("Setting Value")
        self._value = value #  use the variable with a leading _.

    
x = myClass(12)     # this will call the setValue() from __init__
x.value = 15 # this will call the getValue() directly
print(x.value) # this will also call the getValue() as property is set with the function


""" Using the property() for non member attrbutes as well.
    Property can be used for pseudo-private (__) variables as well.
"""

class Robot:

    def __init__(self, name, build_year, lk = 0.5, lp = 0.5 ):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
           return "I feel miserable!"
        elif s <= 0:
           return "I feel bad!"
        elif s <= 0.5:
           return "Could be worse!"
        elif s <= 1:
           return "Seems to be okay!"
        else:
           return "Great!"

    @property
    def name(self):
        print("Getting name")
        return self._name

    @name.setter
    def name(self, name):
        print("Setting name")
        self._name = name

    @property
    def __potential_physical(self):
        print("Getting PP")
        return self.___potential_physical # need to use 3 _ since the variable name contains 2 _ itself

    @__potential_physical.setter
    def __potential_physical(self, val):
        print("Setting __potential_physical")
        self.___potential_physical = val # need to use 3 _ since the variable name contains 2 _ itself
  
if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4 )
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.name, "\t", x.condition)
    print(y.name, "\t", y.condition)
