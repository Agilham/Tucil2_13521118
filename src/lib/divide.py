# fungsi mencari posisi median dari kumpulan titik
def findMidpoint(points):
    return len(points)//2

# fungsi mencari titik yang berada di bagian kiri himpunan
def findLeft(points, middlePoint):
    return points[:middlePoint]

# fungsi mencari titik yang berada di bagian kanan himpunan
def findRight(points, middlePoint):
    return points[middlePoint:]

# fungsi mencari posisi tengah strip
def findMidstrip(leftPoints, rightPoints):
    return (leftPoints[-1].x + rightPoints[0].x) / 2

def divide(points):
        middlePoint = findMidpoint(points)
        leftPoints = findLeft(points, middlePoint)
        rightPoints = findRight(points, middlePoint)
        middleStrip = findMidstrip(leftPoints, rightPoints)
        return leftPoints, rightPoints, middleStrip
    
# fungsi membuat strip berisi titik yang berada di dekat strip
def makeStrip(points, middleStrip, closestDistance):
    strip = [p for p in points if abs(p.x - middleStrip) < closestDistance]
    return strip

# fungsi mengurutkan titik dalam strip berdasarkan komponen ordinat (y) dengan menggunakan algoritma quicksort
def sortStrip(strip):
    if len(strip) <= 1:
        return strip
    else:
        pivot = strip[len(strip)//2]
        left = [p for p in strip if p.y < pivot.y]
        middle = [p for p in strip if p.y == pivot.y]
        right = [p for p in strip if p.y > pivot.y]
        return sortStrip(left) + middle + sortStrip(right)