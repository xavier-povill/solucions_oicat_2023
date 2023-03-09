from easyinput import read
from math import atan2, pi

# Angle del punt (x, y) amb l'eix X. Retorna un valor en l'interval [-180, 180].
# (per ex. angle(1, 0) = 0, angle(0, 1) = 90, angle(0, -1) = -90).
def angle(x, y):
	return atan2(y, x) * 180 / pi


# Angle en sentit antihorari entre els punts b[l] i b[r].
def diff(l, r):
	if r < l:
		return b[r] - b[l] + 360
	return b[r] - b[l]


n, theta = read(int,int)
while(n is not None):
	a = read(int, amount = 2*n) # llegim les coordenades dels n punts com una llista de longitud 2n.
	b = [angle(a[2*i], a[2*i+1]) for i in range(n)]
	b.sort() # ens construim una llista ordenada amb els angles de cada un dels n punts.
	ans = 1 # maxim nombre de punts que podem veure simultàniament.
	r = 1
	for l in range(n): 
		# l := primer punt que podem veure en sentit antihorari.
		# r := primer punt que no podem veure en sentit antihorari des de l.

		# Augmentem r fins que no poguem veure el punt r. 
		while(diff(l, r%n) <= theta and n != 1):
			r += 1
			if r%n == l:
				break
		ans = max(ans, r-l) # començant des de l podem veure un total de r-l punts.
	print(ans)

	n, theta = read(int,int)