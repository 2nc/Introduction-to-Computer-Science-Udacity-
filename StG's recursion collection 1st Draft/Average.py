def rec_average(p):
    #'Find the average of a list of numbers.'
	# *HINT: For the recursive solution, it's easier to use either
	# 1 procedure with 2 parameters, or 2 procedures --
	# one that has 1 parameter and calls the second
	# (which should also have 1 parameter).
	sum = cal_sum(p)
	return (sum + 0.0) / len(p)

def cal_sum(p):
	sum = p[0]
	if len(p) == 1:
		return p[0]
	sum += cal_sum(p[1:])
	return sum

def iter_average(p):
	avg = 0
	sum = 0
	i = 0
	while i < len(p):
		sum += p[i]
		i += 1
	return (sum + 0.0) / len(p)

A = [1,2,3,4,5]
print iter_average(A)
print rec_average(A)