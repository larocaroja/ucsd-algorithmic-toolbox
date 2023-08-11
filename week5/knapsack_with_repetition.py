def knapsack(W, w, v):
    T = [0] * (W + 1 )
    for u in range(1, W+ 1):
        for i in range(len(w)):
            if w[i] <= u: # if there's available space
                T [u] = max ( T [u] , T [u - w [i]] + v [i] )
        print(T)
    return T[W]
print(knapsack(W=10, w=[6, 3, 4, 2], v=[30, 14, 16, 9]))