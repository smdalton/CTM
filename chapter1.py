# task 1.4.10
from plotting import plot
import image
import time

a = image.file2image('img01.png')
a = image.color2gray(a)
cols = range(len(a[0]))
rows = range(len(a))
result = [(x, y) for y in cols for x in rows if a[x][y] < 120]
plot(result, 300)

time.sleep(3)