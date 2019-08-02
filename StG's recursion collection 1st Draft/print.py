def rec_print(p):
    #'Print the elements of a list, each on a separate line.'
    # If you have at least a vague idea of the recursive structure
    # -- in particular, the base case and the recursive call, this
    # should serve as no more than a warm-up.
    if p:
    	print p[0]
    	rec_print(p[1:])


def iter_print(p):
	for a in p:
		print a

A = [1,2,3,4,5]

iter_print(A)
rec_print(A)