def edit_distance(a, b, n, m):
    T = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                T[i][j] = j

            elif j == 0:
                T[i][j] = i

            else:
                T[i][j] = min(
                    T[i-1][j] + 1,
                    T[i][j-1] + 1,
                    T[i-1][j-1] if a[i-1] == b[j-1] else T[i-1][j-1] + 1
                )

    return T[n][m]

if __name__ == "__main__":
    a = input()
    b = input()
    n, m = map(len, (a,b))

    print(edit_distance(a, b , n, m))