def isMonotonic(array):
	if len(array) <= 2:
		return True
	i = 1
	t = 'inc' if array[i - 1] <= array[i] <= array[i + 1] else 'dec'
	while i < len(array) - 1:
		if t == 'inc' and array[i - 1] <= array[i] <= array[i + 1]:
			i += 1
		elif t == 'dec' and array[i - 1] >= array[i] >= array[i + 1]:
			i += 1
		else:
			return False
	return True