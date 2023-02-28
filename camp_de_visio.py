from easyinput import read
from math import atan2, pi

def angle(x, y):
	return atan2(y, x)*180/pi

def diff(l, r):
	if r < l:
		return b[r] - b[l] + 360
	return b[r] - b[l]

n, theta = read(int,int)
while(n is not None):
	a = read(int, amount = 2*n)
	b = [angle(a[2*i], a[2*i+1]) for i in range(n)]
	b.sort()
	r = 1
	ans = 1
	for l in range(n):
		while(diff(l, r%n) <= theta and n != 1):
			r += 1
			if r%n == l:
				break
		ans = max(ans, r-l)
	print(ans)

	n, theta = read(int,int)