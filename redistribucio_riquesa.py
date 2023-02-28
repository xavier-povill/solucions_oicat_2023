from easyinput import read

n, k = read(int, int)
while n is not None:
	a = read(int, amount=n)
	if n == 1:
		a = [a] # si nomes hi ha un element, read(int) 
		        # el llegeix com a enter, no com a llista
	a.sort()
	
	# cost_esquerra[i] := diners que hem d'afegir per fer que els elements 
	#                     a l'esquerra d'a[i] siguin iguals a a[i].
	cost_esquerra = [0] * n
	for i in range(1, n):
		cost_esquerra[i] = cost_esquerra[i-1] + (a[i] - a[i-1]) * i

	# cost_dreta[i] := diners que hem de treure per fer que els elements 
    #                  a la dreta d'a[i] siguin iguals a a[i].
	cost_dreta = [0] * n
	for i in range(n-2, -1, -1):
		cost_dreta[i] = cost_dreta[i+1] + (a[i+1] - a[i]) * (n-1 - i)

	petit = a[n-1] # maxim minim del vector que podem aconseguir afegint k euros.
	for i in range(1, n):
		if cost_esquerra[i] > k:
			sobrants = k - cost_esquerra[i-1]
			petit = a[i-1] + sobrants//i
			break

	gran = a[0] # minim maxim del vector que podem aconseguir traient k euros.
	for i in range(n-2, -1, -1):
		if cost_dreta[i] > k:
			sobrants = k - cost_dreta[i+1]
			gran = a[i+1] - sobrants//(n-1 - i)
			break

	if petit >= gran:
		# Tot i que puguem moure molts diners, si la suma no 
		# es divisible per n no ho podrem igualar del tot.
		if sum(a) % n == 0:
			print(0)
		else:
			print(1)
	else:
		print(gran - petit)

	n, k = read(int, int)