def Calculate(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    try:
        div = a / b
    except:
        div = ZeroDivisionError

    return f"Add :- {add}, Subtract :- {sub}, Multiply :- {mul}, Division :- {div}"

print(Calculate(20,0))