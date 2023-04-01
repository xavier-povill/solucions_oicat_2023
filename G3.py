from PIL import Image, ImageDraw
from easyinput import read
from queue import Queue

n = read(int)
m = read(int)
r = read(int)
v = [read(str) for _ in range(n)]


# Retorna True si (x[0], x[1]) és una posició dins de la graella que no està coberta per aigua.
def IsValid(x):
	return x[0] >= 0 and x[0] < n and x[1] >= 0 and x[1] < m and v[x[0]][x[1]] != 'A'


img = Image.new('RGB', (10*m, 10*n), 'Grey')
dib = ImageDraw.Draw(img)

# Afegim totes les pizzeries a la cua.
q = Queue()
for i in range(n):
	for j in range(m):
		if v[i][j] == 'P':
			q.put((i, j))

inf = 1000000000 # valor més gran que qualsevol distància.

dist = [[0 if x == 'P' else inf for x in fila] for fila in v]
df = [1, 0, -1, 0] # moviments verticals
dc = [0, 1, 0, -1] # moviments horitzontals

# BFS.
while not q.empty():
	x = q.get()
	for k in range(4):
		# Tal com hem definit df i dc, tenim que:
		# 	k = 0 -> moviment cap a baix
		# 	k = 1 -> moviment cap a la dreta
		# 	k = 2 -> moviment cap a dalt
		# 	k = 3 -> moviment cap a l'esquerra 
		noux = (x[0] + df[k], x[1] + dc[k])
		if not IsValid(noux):
			continue
		if dist[noux[0]][noux[1]] > dist[x[0]][x[1]] + 1:
			dist[noux[0]][noux[1]] = dist[x[0]][x[1]] + 1
			q.put(noux)
		# També podríem aturar el BFS quan arribem a distància > r, 
		# fent que el codi vagi una mica més ràpid.

# Output. 
for i in range(n):
	for j in range(m):
		col = 'Grey'
		if v[i][j] == 'A':
			col = 'Aqua'
		elif v[i][j] == 'P':
			col = 'Brown'
		elif dist[i][j] <= r:
			col = 'Green'
		else:
			continue
		dib.polygon([(10*j, 10*i), (10*j + 9, 10*i), (10*j + 9, 10*i + 9), (10*j, 10*i + 9)], col)

img.save('output.png')