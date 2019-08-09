def rec_largest(p):
    #'Return the largest element of a list.'
    # Ideally, you should only have to switch around one
    # or two <'s and >'s in order to make your solution(s)
    # return the smallest element of the list.
    if p == []:
    	return
    max = p[0]
    num = rec_largest(p[1:])
    if num > max:
    	max = num
    return max

def iter_largest(p):
	i = 0 
	max = p[0]
	for a in p:
		if a > max:
			max = a
	return max

A = [1,2,3,2,1]

print iter_largest(A)
print rec_largest(A)