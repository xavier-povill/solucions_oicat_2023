from PIL import Image, ImageDraw
from easyinput import read
from queue import Queue


n = read(int)
m = read(int)
r = read(int)
v = [read(str) for _ in range(n)]


def IsValid(x):
	return x[0] >= 0 and x[0] < n and x[1] >= 0 and x[1] < m and v[x[0]][x[1]] != 'A'


img = Image.new('RGB', (10*m, 10*n), 'Grey')
dib = ImageDraw.Draw(img)

q = Queue()
for i in range(n):
	for j in range(m):
		if v[i][j] == 'E':
			q.put((i, j))

inf = 1000000000

dist = [[0 if x == 'E' else inf for x in fila] for fila in v]
df = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
while not q.empty():
	x = q.get()
	for k in range(4):
		noux = (x[0] + df[k], x[1] + dc[k])
		if not IsValid(noux):
			continue
		if dist[noux[0]][noux[1]] > dist[x[0]][x[1]] + 1:
			dist[noux[0]][noux[1]] = dist[x[0]][x[1]] + 1
			q.put(noux)

for i in range(n):
	for j in range(m):
		col = 'Grey'
		if v[i][j] == 'A':
			col = 'Aqua'
		elif v[i][j] == 'E':
			col = 'Brown'
		elif dist[i][j] <= r:
			col = 'Green'
		else:
			continue
		dib.polygon([(10*j, 10*i), (10*j + 9, 10*i), (10*j + 9, 10*i + 9), (10*j, 10*i + 9)], col)


img.save('output.png')