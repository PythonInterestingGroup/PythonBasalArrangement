L = [('john','B',15),('jane','A',12),('dave','B',10),('ethan','C',20),('peter','B',20),('mike','C',16)]

def by_score(t):
	return t[1],t[2]
print(sorted(L, key=by_score, reverse = False))