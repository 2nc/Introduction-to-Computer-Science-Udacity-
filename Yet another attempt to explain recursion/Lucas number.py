def Lucas_number(n):
	if n == 0:
		return 2
	if n == 1:
		return 1
	return Lucas_number(n - 1) + Lucas_number(n - 2)

print Lucas_number(0)
print Lucas_number(1)
print Lucas_number(2)
print Lucas_number(3)