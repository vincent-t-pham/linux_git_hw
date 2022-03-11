def sort_list(list):
	n=len(list)
	i=0
	j=0
	while i < n:
		while j < (n-i-1):
			if (list[j]>list[j+1]):
				list[j], list[j+1] = list[j+1], list[j]
			j+=1
		i+=1
	return list

