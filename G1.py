from PIL import Image, ImageDraw
import math

def rect(x1, y1, x2, y2, col):
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], col)

def quadrat(x,y,c, col):
    rect(x,y,x+c-1,y+c-1, col)

def cercle(coor, r, col):
    (x,y) = coor
    x-=1
    y-=1
    dib.ellipse([(x-r, y-r), (x+r, y+r)], col)

c = int(input())
d = int(input())
m = int(input())

d = d//2
fons = input()
dins = input()
forma = input()

img = Image.new('RGB', (c+2*m, c+2*m), fons)
dib = ImageDraw.Draw(img)

quadrat(m,m,c,dins)

mig = m + (c+1)//2

centres_fora = [(mig, m), (c+m+1, mig), (mig, c+m+1), (m, mig)]
centres_dins = [(mig, m+1), (c+m, mig), (mig, c+m), (m+1, mig)]

for i in range(4):
    if forma[i] == '(':
        cercle(centres_dins[i], d, fons)
    elif forma[i] == ')':
        cercle(centres_fora[i], d, dins)

img.save('output.png')