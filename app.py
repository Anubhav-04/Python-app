class Calculate:
    def add(self,a,b):
        return a + b
    def subtract(self,a,b):
        return a - b
    def Multiply(self,a,b):
        return a * b
    def Division(self,a,b):
        try:
            return a/b
        except:
            return ZeroDivisionError

c1 = Calculate()
