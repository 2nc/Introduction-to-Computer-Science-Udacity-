def list_binary_search_where( my_list, the_value,index = 0):
    #pass your code here
    if my_list == []:
    	return [False,None]
    if len(my_list) == 1:
    	if the_value == my_list[0]:
    		return [True, index]
    	else:
    		return [False,None]
    mid_index = len(my_list) / 2 
    if the_value < my_list[mid_index]:
        return list_binary_search_where(my_list[:mid_index],the_value,index)
    else:
    	return list_binary_search_where(my_list[mid_index:],the_value,index + mid_index)

A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]

assert( list_binary_search_where( A, 0) == [False, None] )

assert( list_binary_search_where( A, 1) == [True, 0] )

assert( list_binary_search_where( A, 2) == [True, 1] )

assert( list_binary_search_where( A, 13) == [True, 9] )

assert( list_binary_search_where( A, 24) == [False, None] )

assert( list_binary_search_where( A, 25) == [True, 15] )

assert( list_binary_search_where( A, 26) == [False, None] )

print("tests of list_binary_search_where() passed")