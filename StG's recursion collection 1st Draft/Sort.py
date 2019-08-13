def rec_sort(p):
    #'Return a list of numbers sorted from least to greatest.'
    # You've done well if you solved this problem,
    # but for some reason feel like your solution
    # does some extraneous things. When you take a
    # course in algorithms, you'll recall this.
    if len(p) == 0:
    	return []
    pivot = p[0]
    less = []
    great = []
    i = 1
    while i < len(p):
    	if p[i] >= pivot:
    		great.append(p[i])
    	else:
    		less.append(p[i])
    	i += 1
    return rec_sort(less) + [pivot] + rec_sort(great)

def iter_sort(p):
	i = 0
	j = 0
	while i < len(p):
		least = p[i]
		j = i + 1
		while j < len(p):
			if least > p[j]:
				least = p[j]
				p[j],p[i] = p[i],p[j]
			j += 1
		i += 1
	return p 

A = [9,8,6,7,4,5,2,3,1]

print iter_sort(A)
print rec_sort(A)