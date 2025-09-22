from app import *
if __name__ == '__main__':
    c1 = Calculate()
    print("Add:", c1.add(5, 3))
    print("Subtract:", c1.subtract(5, 3))
    print("Multiply:", c1.Multiply(5, 3))
    print("Division:", c1.Division(5, 0))  # Should print ZeroDivisionError