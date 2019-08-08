def rec_RemDup(p):
    #'Remove duplicate entries in a list.'
    # You'll also need to think outside of the box for this one.
    single = []
    if len(p) == 1:
    	return [p[0]]
    single = rec_RemDup(p[1:])
    if p[0] not in single:
    	single = [p[0]] + single
    return single
    

def iter_RemDup(p):
	single = []
	for a in p:
		if a not in single:
			single.append(a)
	return single

A = [1,1,2,2,3]

print rec_RemDup(A)
print iter_RemDup(A)