def car_fueling(m, stops):
    current_loc = 0
    n_refills = 0
    i = 0
    next_loc = stops[i]
    
    while True:
        n_move = 0

        while (next_loc - current_loc <= m):
            if i == len(stops) - 1:
                return n_refills
            
            i += 1
            next_loc = stops[i]
            n_move += 1

        if n_move == 0:
            return -1
        
        current_loc = stops[i-1]
        n_refills += 1

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split(' ')))

    stops.append(d)
    
    print(car_fueling(m, stops))