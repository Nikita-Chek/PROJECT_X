def gcd(a, b, x=0, y=1):
	if (a == 0):
		x = 0
		y = 1
		return (b, x, y)
	x1 = 0
	y1 = 0
	tupl = gcd(b%a, a, x1, y1)
	d = tupl[0]
	x = tupl[2]- (b // a) * tupl[1]
	y = tupl[1]
	return (d, x, y)

def inverseBM(a, m):
	g = gcd(a, m)
	if (g[0] != 1):
		return Exception
	else:
		x = (g[1] % m + m) % m
	return x