from lib.point import *
from lib.solve import *
from lib.iofile import *
from lib.conquer import *
from lib.bruteforce import *
from time import *

n = int(input("Masukkan nilai n: "))

points = generatePoints(n)
points = sortPoints(points)

closestDC, pdc1, pdc2 = conquer(points)
timeFinishDC = process_time()

pointsDC = [pdc1, pdc2]
countSolve = getCount()

printPoints(pointsDC)
print(f"Distance: {closestDC}")
print(f"Time: {timeFinishDC} seconds")
print(f"Euclidean performed: {countSolve}")

closestBF, pbf1, pbf2 = bruteforce(points)
timeFinishBF = process_time()

pointsBF = [pbf1, pbf2]

printPoints(pointsBF)
print(f"Distance: {closestBF}")
print(f"Time: {timeFinishBF} seconds")

points.remove(pdc1)
points.remove(pdc2)
displayPoints(points, pointsDC)