import math

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

disq = pow(b, 2) - 4*a*c
if disq < 0:
        print("No real root")
else:
    m1 = ((b*-1) + math.sqrt(disq)) / (2*a)
    m2 = ((b*-1) - math.sqrt(disq)) / (2*a)

    print(m1)
    print(m2)
