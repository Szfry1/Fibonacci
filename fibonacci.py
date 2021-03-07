def fibo_maker(n):
    a = 1 
    b = 0
    while a < n:
        print(a, sep='  ')
        a, b = a + b, a
# takes n as a parameter and then while n is larger it will print a
# then a equals a+b and b = a

n = int(input('Input n: '))
fibo_maker(n)

