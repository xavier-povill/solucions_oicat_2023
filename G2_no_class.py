from PIL import Image, ImageDraw
import math

def rect(x1, y1, x2, y2, col):
    dib.polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], col)

n = int(input())

# titol, autor, -pagines, any, mes, dia, -alçada, ordre entrada, color
llibres = []

#títol, autor, nombre de pàgines, data de publicació (en format dd/mm/aaaa), alçada del llibre en píxels, i color.
mes_alt = 0
ample_total = 0
for i in range(n):
    titol = input()
    autor = input()
    pagines = int(input())
    data = input()
    data = data.split("/")
    alt = int(input())
    color = input()

    mes_alt = max(mes_alt, alt)
    ample_total += pagines//4
    llibres.append((titol.lower(), autor.lower(), -pagines, data[2], data[1], data[0], -alt, i, color))

img = Image.new('RGB', (ample_total, mes_alt+10), "White")
dib = ImageDraw.Draw(img)
rect(0, mes_alt, ample_total, mes_alt+10, "Brown")

llibres = sorted(llibres)
pos = 0
for (_, _, pagines, _, _, _, alt, _, col) in llibres:
    pagines = -pagines
    pagines //= 4
    alt = -alt
    rect(pos, mes_alt-1,pos+pagines-1, mes_alt-alt, col)
    pos += pagines
img.save('output.png')