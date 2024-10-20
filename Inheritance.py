from OopsConcepts import Calculator
class ChildClass(Calculator):
    num2 = 5
    def __init__(self):
        Calculator.__init__(self)
        print("in child class ")

    def childsum(self):
        return self.num2 + self.digit

    def summati(self):
        return self.num2+ self.digit+self.summation()

obj = ChildClass()
#print(obj.summati())

print("Hello" in "Helo world")
print("Helo wolrd there".split(" "))
print("Hello world".replace(" ", ""))