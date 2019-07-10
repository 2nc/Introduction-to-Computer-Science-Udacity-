def list_binary_search( my_list, the_value):
    #pass your code here
    if my_list == []:
    	return False
    if len(my_list) == 1:
    	if the_value == my_list[0]:
    		return True
    	else:
    		return False
    mid_index = len(my_list) / 2 
    if the_value < my_list[mid_index]:
        return list_binary_search(my_list[:mid_index],the_value)
    else:
    	return list_binary_search(my_list[mid_index:],the_value)

A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]

assert( list_binary_search( A, 0) == False )

assert( list_binary_search( A, 1) == True )

assert( list_binary_search( A, 2) == True )

assert( list_binary_search( A, 13) == True )

assert( list_binary_search( A, 24) == False )

assert( list_binary_search( A, 25) == True )

assert( list_binary_search( A, 26) == False )

print('tests of list_binary_search() passed')