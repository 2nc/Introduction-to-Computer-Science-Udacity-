# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def smaller(a,b):
    if a > b:
        return b
    return a

def set_range(a,b,c):
    # Your code here
    max_num = max(a,b,c)
    if max_num == a:
        return max_num - smaller(b,c)
    if max_num == b:
        return max_num - smaller(a,c)
    return max_num - smaller(a,b)

print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6