def lcs(seq_a, seq_b, n, m):
    T = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0 :
                T[i][j] = 0
            
            elif seq_a[i-1] == seq_b[j-1]:
                T[i][j] = T[i-1][j-1] + 1
                
            else:
                T[i][j] = max(T[i][j-1],T[i-1][j])

    return T[n][m]

if __name__ == "__main__":
    n = int(input())
    seq_a = list(map(int, input().split(' ')))
    m = int(input())
    seq_b = list(map(int, input().split(' ')))

    print(lcs(seq_a, seq_b, n, m))