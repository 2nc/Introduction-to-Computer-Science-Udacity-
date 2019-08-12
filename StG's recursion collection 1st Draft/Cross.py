def rec_cross(p1, p2):
    # 'Return the cross product of two lists. \
    #  E.g., cross([1,2,3],[4,5]) would return \
    #  [[1,4],[1,5],[2,4],[2,5],[3,4],[3,5]].'
# So far you've only had to iterate over one list. 
# It's possible to iterate over two in a 5-line
# recursive solution. Good luck!
	if len(p1) == 0:
		return []
	if len(p2) == 1:
		return [[p1[0],p2[0]]]
	else:
		list_out = [[p1[0],p2[0]]]
		list_out += rec_cross(p1,p2[1:])
		list_out += rec_cross(p1[1:],p2)		
		return list_out

# def rec_cross(p1, p2):
# 	if len(p1)==0 or len(p2)==0:
# 		return []
# 	else:
# 		s=rec_cross(p1,p2[:-1])
# 		s.append([p1[-1], p2[-1]])
# 		print s
# 		return rec_cross(p1[:-1], p2) + s[-len(p2):]


def iter_cross(p1, p2):
	i = 0
	j = 0
	list_out = []
	while i < len(p1):
		while j < len(p2):
			list_out.append([p1[i],p2[j]])
			j += 1
		i += 1
		j = 0
	return list_out


A = [1,2,3]
B = [4,5]

print iter_cross(A,B)
print rec_cross(A,B)