class Calculator :
    digit = 96

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
        print("In a Calculator constructor")

    def __init__(self):
        print("In a Calculator's default constructor")

    def summation(self):
        return self.num1 + self.num2 - self.digit

    def sum(self, a, b):
        return a+b

    def sub(self,a,b):
        return a-b

"""
obj = Calculator(4, 5 )
print(obj.summation())
print(obj.digit)
print(obj.sum(5, 7))
print(obj.sub(7, 15))

"""

print(Calculator.sum(4, 6, 5))