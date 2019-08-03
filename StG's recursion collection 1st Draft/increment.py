def rec_increment(p):
    #'Return a list of numbers with each of its elements increased by 1.'
    # This is a small jump in difficulty from the previous problem,
    # so here's a hint: You don't need to mutate a list.
    incre = [p]
    if incre[0] == 0:
    	return incre
    else:
    	incre = rec_increment(p - 1) + incre
    return incre
    
def iter_increment(p):
	increse = []
	for a in range(0,p+1):
		increse.append(a)
	return increse

print iter_increment(5)
print rec_increment(5)