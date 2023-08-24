def lcs(seq_a, seq_b, seq_c, n, m, l):
    T = [[[-1 for _ in range(l+1)] for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            for k in range(l+1):
                if i == 0 or j == 0 or k == 0:
                    T[i][j][k] = 0

                elif (seq_a[i-1] == seq_b[j-1]) and (seq_b[j-1] == seq_c[k-1]):
                    T[i][j][k] = T[i-1][j-1][k-1] + 1

                else:
                    T[i][j][k] = max(
                        T[i-1][j][k],
                        T[i][j-1][k],
                        T[i][j][k-1]
                    )
    
    return T[n][m][l]

if __name__ == "__main__":
    n = int(input())
    seq_a = list(map(int, input().split(' ')))
    m = int(input())
    seq_b = list(map(int, input().split(' ')))
    l = int(input())
    seq_c = list(map(int, input().split(' ')))

    print(lcs(seq_a, seq_b, seq_c, n, m, l))