from PIL import Image, ImageDraw
from dataclasses import dataclass
from functools import cmp_to_key
from typing import List

@dataclass
class book:
	title: str
	author: str
	year: int
	month: int
	day: int
	pages: int
	height: int
	colour: str
	index: int

def compare(a: book, b: book)->int:
	if a.title!=b.title:
		return 2*(a.title>b.title)-1
	if a.author!=b.author:
		return 2*(a.author>b.author)-1
	if a.pages!=b.pages:
		return b.pages-a.pages
	if a.year!=b.year:
		return a.year-b.year
	if a.month!=b.month:
		return a.month-b.month
	if a.day!=b.day:
		return a.day-b.day
	if a.height!=b.height:
		return b.height-a.height
	return a.index-b.index


n=int(input())

llibres: List[book]=[None for _ in range(n)]

amplada_dibuix=0
alcada_dibuix=0

for i in range(n):
	titol=input().lower()
	autor=input().lower()
	pagines=int(input())
	data=input()
	alcada=int(input())
	color=input()
	alcada_dibuix=max(alcada_dibuix,alcada)
	amplada_dibuix+=pagines//4
	llibres[i]=book(title=titol, author=autor, year=int(data[6:]), month=int(data[3:5]), 
		            day=int(data[0:2]), pages=pagines, height=alcada, colour=color, index=i)

llibres.sort(key=cmp_to_key(compare))

alcada_dibuix+=10
img = Image.new('RGB', (amplada_dibuix, alcada_dibuix), 'White')
dib = ImageDraw.Draw(img)
dib.polygon([(0,alcada_dibuix-1),(amplada_dibuix-1,alcada_dibuix-1),(amplada_dibuix-1,alcada_dibuix-10),(0,alcada_dibuix-10)],'Brown')

def dibuixa_llibre(x,amplada,alcada,color):
	dib.polygon([(x,alcada_dibuix-11),(x+amplada-1,alcada_dibuix-11),(x+amplada-1,alcada_dibuix-10-alcada),(x,alcada_dibuix-10-alcada)],color)

x=0
for llibre in llibres:
	dibuixa_llibre(x,llibre.pages//4,llibre.height,llibre.colour)
	x+=llibre.pages//4
img.save("output.png")