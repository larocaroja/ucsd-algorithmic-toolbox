import math

def money_change_dp(money):
    N_COINS = [0 if v == 0 else math.inf for v in range(money+1)]
    denominators = [1, 3, 4]
    
    for i in range(1, money+1):
        for denominator in denominators:
            if denominator <= i:
                if N_COINS[i-denominator] + 1 < N_COINS[i]:
                    N_COINS[i] = N_COINS[i-denominator] + 1

    if N_COINS[money] == math.inf:
        return -1

    return N_COINS[money]

if __name__ == '__main__':
    money = int(input())
    print(money_change_dp(money))