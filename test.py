which_array = ''
if (len(f) > len(m)):
	for itr in f:
		try:
			hash_new[itr] += 1
		except:
			hash_new[itr] = 1
else:
	for itr in f:
		try:
			hash_new[itr] += 1
		except:
			hash_new[itr] = 1


