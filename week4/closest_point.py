import math

class PointData():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calculate_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def closest_points_iterative(seq):
    n = len(seq)
    d_minimum = math.inf

    for i in range(n):
        p1 = seq[i]

        for j in range(i+1, n):
            p2 = seq[j]

            d = calculate_distance(p1, p2)

            if d < d_minimum:
                d_minimum = d

    return d_minimum

def closest_points(seq, l, r):
    if r-l <= 2:
        return closest_points_iterative(seq[l:r+1])
    
    mid = l + (r-l)//2
    d_left = closest_points(seq, l, mid)
    d_right = closest_points(seq, mid+1, r)
    d_minimum = min(d_left, d_right)

    x_mid = seq[mid]
    l_strip, r_strip = l, r
    for i, p in enumerate(seq[l:r+1]):
        if (p.x > x_mid.x - d_minimum) and (l_strip == l):
            l_strip = l + i
        if (p.x >= x_mid.x + d_minimum) and (r_strip == r):
            r_strip = l + i - 1
            break

    strip = seq[l_strip:r_strip+1]
    sorted(strip, key = lambda p: p.y)

    d_strip = math.inf
    for i in range(0, r_strip - l_strip):
        for j in range(i+1, r_strip - l_strip):
            if j-i > 7:
                break

            p1 = strip[i]
            p2 = strip[j]
            d_temp = calculate_distance(p1, p2)

            if d_temp < d_strip:
                d_strip = d_temp

    return min(d_minimum, d_strip)

if __name__ == '__main__':
    n = int(input())

    seq = []
    for _ in range(n):
        x, y = map(int, input().split(' '))
        seq.append(PointData(x = x , y = y))
    
    # sort the sequence of points in ascending order of x coordinates
    seq = sorted(seq, key = lambda p: p.x)

    print(closest_points(seq, 0, n-1))