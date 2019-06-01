def string_split(l):
	l_left = ""
	l_right = ""
	for i in range(0,(len(l) + 1)/2):
		l_left += l[i]
	for i in range((len(l) + 1)/2,len(l)):
		l_right += l[i]
	print [l_left,l_right]

string_split(['Hello', ' world!', 'Goodnight', ' moon!'])
string_split(['one', 'two', 'three'])
string_split(["",""])
