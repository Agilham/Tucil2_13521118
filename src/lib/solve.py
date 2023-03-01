from math import *

countSolve = 0

# fungsi mencari jarak antara dua bauh titik pada bidang 3D
def findDistance(p1, p2):
    global countSolve
    countSolve += 1
    return sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2)

# fungsi mencari jarak terdekat di antara n buah titik, dengan n <= 3
def findNonStrip(points):
    closestDistance = inf
    p1, p2 = points[0], points[0]
    for i in range(len(points) - 1):
        for j in range(i+1, len(points)):
            distance = findDistance(points[i], points[j])
            if distance < closestDistance:
                closestDistance = distance
                p1 = points[i]
                p2 = points[j]
    return closestDistance, p1, p2

# fungsi mencari jarak terdekat antara pasangan titik dalam strip
def findInStrip(strip, pnon1, pnon2, closesDistance):
    closestInStrip = closesDistance
    p1, p2 = pnon1, pnon2
    for i in range(len(strip)-1):
        for j in range(i+1, len(strip)):
            distance = findDistance(strip[i], strip[j])
            if distance < closestInStrip:
                closestInStrip = distance
                p1 = strip[i]
                p2 = strip[j]
    return closestInStrip, p1, p2

def getCount():
    return countSolve