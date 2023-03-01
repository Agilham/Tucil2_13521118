from lib.divide import *
from lib.solve import *

# fungsi utama mencari pasangan titik terdekat 3D dengan algoritma divide and conquer
def conquer(points):
    # kondisi basis, maka jarak antara titik dihitung langsung dengan rumus Euclidean
    if len(points) <= 3:
        return findNonStrip(points)
    # rekurens, menerapkan algoritma divide and conquer pada masing-masing bagian untuk mencari sepasang titik terdekat
    else:
        leftPoints, rightPoints, middleStrip = divide(points)

        closestLeft, pl1, pl2 = conquer(leftPoints)
        closestRight, pr1, pr2 = conquer(rightPoints)
        
        if (closestLeft <= closestRight):
            closestDistance = closestLeft
            p1, p2 = pl1, pl2
        else:
            closestDistance = closestRight
            p1, p2 = pr1, pr2

        strip = makeStrip(points, middleStrip, closestDistance)
        strip = sortStrip(strip)
        
        closestInStrip, ps1, ps2 = findInStrip(strip, p1, p2, closestDistance)

        if (closestDistance <= closestInStrip):
            return closestDistance, p1, p2
        else:
            return closestInStrip, ps1, ps2
        
# fungsi mendapatkan banyaknya operasi perhitungan rumus euclidian
def getCount():
    return countSolve