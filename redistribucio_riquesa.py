from easyinput import read

n, k = read(int, int)
while n is not None:
	a = read(int, amount=n)
	if n == 1:
		a = [a]
	a.sort()
	r = n-1
	big = a[n-1]
	acum = 0
	while r >= 1 and acum < k:
		d = min(a[r] - a[r-1], (k-acum)//(n-r)) 
		acum += d*(n-1 - r + 1)
		big -= d
		if d != a[r] - a[r-1]:
			break
		r -= 1

	l = 0
	small = a[0]
	acum = 0
	while l <= n-2 and acum < k:
		d = min(a[l+1] - a[l], (k-acum) // (l+1))
		acum += d * (l+1)
		small += d
		if d != a[l+1] - a[l]:
			break
		l += 1

	if small >= big:
		if sum(a) % n == 0:
			print(0)
		else:
			print(1)
	else:
		print(big - small)

	n, k = read(int, int)