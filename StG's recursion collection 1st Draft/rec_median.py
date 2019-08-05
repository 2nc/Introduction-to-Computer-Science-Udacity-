def rec_median(p):  
    #'Find the median of a sorted (assume that) list of numbers.'
    # This problem is a bit different from the rest.
# In addition to recursion and iteration, find a direct
# solution -- in other words, one that doesn't use loops.
	if len(p) == 1:
		return p[0]
	if len(p) == 2:
		return (p[0] + p[1]) / 2.0
	return rec_median(p[1:len(p) - 1])

def iter_median(p):
	while True:
		if len(p) == 1:
			return p[0]
		if len(p) == 2:
			return (p[0] + p[1]) / 2.0
		p = p[1:len(p) - 1]

	


def direct_median(p):
	if len(p) % 2 == 1:
		return p[len(p)/2]
	else:
		return (p[len(p)/2] + p[len(p)/2 - 1]) / 2.0

A = [1,2,3]
B = [1,2,3,4]

print rec_median(A)
print rec_median(B)

print iter_median(A)
print iter_median(B)

print direct_median(A)
print direct_median(B)