from numpy import *
import matplotlib.pyplot as plt

# definisi tipe data point (titik) pada bidang 3D
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# fungsi membangkitkan secara acak titik dalam koordinat (x, y, z)
def generatePoints(n):
    points = []
    while len(points) < n:
        x = random.randint(1000)
        y = random.randint(1000)
        z = random.randint(1000)
        p = Point(x, y, z)
        if p not in points:
            points.append(p)
    return points

# fungsi mengurutkan titik berdasarkan komponen absis (x) dengan mneggunakan algoritma quicksort
def sortPoints(points):
    if len(points) <= 1:
        return points
    else:
        pivot = points[len(points)//2] # choose pivot as middle element
        left = [p for p in points if p.x < pivot.x]
        middle = [p for p in points if p.x == pivot.x]
        right = [p for p in points if p.x > pivot.x]
        return sortPoints(left) + middle + sortPoints(right)

# prosedur menampilkan titik pada bidang 3D
def printPoints(points):
    for i in range(len(points)):
        print(f"P{i+1} ({points[i].x}, {points[i].y}, {points[i].z})")

# prosedur menggambarkan titik dalam bidang 3D
def displayPoints(points, psol1):
    figure = plt.figure()
    subPlot = figure.add_subplot(projection='3d')

    pxs = [p.x for p in psol1]
    pys = [p.y for p in psol1]
    pzs = [p.z for p in psol1]
    subPlot.scatter(pxs, pys, pzs, color='red')

    pxs = [p.x for p in points]
    pys = [p.y for p in points]
    pzs = [p.z for p in points]
    subPlot.scatter(pxs, pys, pzs, color='black')

    subPlot.set_xlabel('X')
    subPlot.set_ylabel('Y')
    subPlot.set_zlabel('Z')

    plt.show()