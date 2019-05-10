#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    fn1 = 0
    fn2 = 1
    i = 2
    while i <= n:
        sum = fn1 + fn2
        fn1 = fn2
        fn2 = sum
        i = i + 1
    return sum




print fibonacci(36)
#>>> 14930352