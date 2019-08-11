def rec_bricks(small, big, goal): 
    # Get ready to incorporate some math and logic. Aim for a
    # 3-line (1 if + 2 return statements) direct solution. 
    # I think the recursive and iterative solutions are more
    # intuitive, so you might want to start with them.
    if big * 5 <= goal and (big * 5 + small * 1) >= goal:
    	return True
    else:
    	if big >= 0:
    		return rec_bricks(small,big - 1, goal)
    	else:
    		return False


def iter_bricks(small, big, goal):
	i = 0
	j = 0
	while i <= small:
		while j <= big:
			if (goal == 1 * i + 5 * j):
				return True
			j = j + 1
		i = i + 1
		j = 0
	return False


def direct_bricks(small, big, goal):
	if goal / 5 >= big :
		return big * 5 + small >= goal
	return goal - small <= big * 5 

print iter_bricks(3,1,8)
print iter_bricks(3,1,9)
print iter_bricks(3,2,10)

print rec_bricks(3,1,8)
print rec_bricks(3,1,9)
print rec_bricks(3,2,10)

print direct_bricks(3,1,8)
print direct_bricks(3,1,9)
print direct_bricks(3,2,10)