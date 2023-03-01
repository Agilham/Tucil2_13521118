from lib.point import *
from lib.solve import *
from lib.input import *
from lib.conquer import *
from lib.bruteforce import *
from time import *

n = getValid()

points = generatePoints(n)
points = sortPoints(points)

closestDC, pdc1, pdc2 = conquer(points)
timeFinishDC = process_time()
pointsDC = [pdc1, pdc2]
countDC = getCount()

print("\nMencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer")
print("Pasangan titik terdekat")
printPoints(pointsDC)
print(f"Jarak terdekat: {closestDC}")
print(f"Banyak operasi: {countDC}")
print(f"Waktu komputasi: {timeFinishDC} seconds")

closestBF, pbf1, pbf2 = bruteforce(points)
timeFinishBF = process_time()
pointsBF = [pbf1, pbf2]
countBF = getCount()-countDC

print("\nMencari Pasangan Titik Terdekat 3D dengan Algoritma Brute Force")
print("Pasangan titik terdekat")
printPoints(pointsBF)
print(f"Jarak terdekat: {closestBF}")
print(f"Banyak operasi: {countBF}")
print(f"Waktu Komputasi: {timeFinishBF} seconds")

print("\nPenggambaran titik dalam bidang 3D, pasangan titik terdekat ditunjukkan dengan warna merah")
points.remove(pdc1)
points.remove(pdc2)
displayPoints(points, pointsDC)