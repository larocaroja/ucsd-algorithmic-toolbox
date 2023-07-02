def maximum_loot(W, weight, cost):
    if W == 0 or len(weight) == 0:
        return 0
    
    a = min(W, weight[0])
    value = a * cost[0] / weight[0]

    weight.pop(0)
    cost.pop(0)
    W -= a

    return round(value + maximum_loot(W, weight, cost), 4)

if __name__ == '__main__':
    n, W = map(int, input().split(' '))
    weight = []
    cost = []

    for _ in range(n):
        c_i, w_i = map(int, input().split(' '))
        cost.append(c_i)
        weight.append(w_i)

    # sort weight and cost in descending order of unit_price
    unit_price = [cost[i]/weight[i] for i in range(n)]
    weight = [x for (y,x) in sorted(zip(unit_price, weight), key=lambda pair: pair[0], reverse = True)]
    cost = [x for (y,x) in sorted(zip(unit_price, cost), key=lambda pair: pair[0], reverse = True)]

    print(maximum_loot(W, weight, cost))