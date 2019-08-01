def list_binary_search_depth_2( my_list, the_value):
    #pass your code here
    if my_list == []:
    	return [False,0]
    if len(my_list) == 1:
    	if the_value == my_list[0]:
    		return [True,0]
    	else:
    		return [False,0]
    mid_index = len(my_list) / 2
    if the_value == my_list[mid_index]:
        return [True,0]
    if the_value < my_list[mid_index]:
        result,depth =  list_binary_search_depth_2(my_list[:mid_index],the_value)
    else:
    	result,depth =  list_binary_search_depth_2(my_list[mid_index + 1:],the_value)
    return [result,depth + 1]

A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]

assert( list_binary_search_depth_2( A, 0) == [False, 4] )

assert( list_binary_search_depth_2( A, 1) == [True, 4] )

assert( list_binary_search_depth_2( A, 2) == [True, 3] )

assert( list_binary_search_depth_2( A, 13) == [True, 0] )

assert( list_binary_search_depth_2( A, 24) == [False, 3] )

assert( list_binary_search_depth_2( A, 25) == [True, 3] )

assert( list_binary_search_depth_2( A, 26) == [False, 3] )

print("tests of list_binary_search_depth_2() passed")
