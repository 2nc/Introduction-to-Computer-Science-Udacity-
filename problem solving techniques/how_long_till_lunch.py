def how_long_til_lunch(hour,min,str):
	goal = 11 * 60 + 45
	convert = hour * 60 + min
	if str == 'am':
		diff = goal - convert
		if diff < 0:
			diff = 24 * 60 + diff
	else:
		diff = goal + 12 * 60 - convert
	return diff

print how_long_til_lunch(5,45,'pm')
print how_long_til_lunch(11,47,'am')