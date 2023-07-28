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
    
    # divide
    mid = l + (r-l)//2
    d_left = closest_points(seq, l, mid)
    d_right = closest_points(seq, mid+1, r)



if __name__ == '__main__':
    n = int(input())

    seq = []
    for _ in range(n):
        x, y = map(int, input().split(' '))
        seq.append(PointData(x = x , y = y))
    
    # sort the sequence of points in ascending order of x coordinates
    seq = sorted(seq, key = lambda x: x.x)

    print(closest_points(seq))