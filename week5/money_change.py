import math

N_COINS = dict()
N_COINS[0] = 0
denominators = [1, 3, 4]

def money_change_dp(money):
    for i in range(1, money+1):
        N_COINS[i] = math.inf

        for denominator in denominators:
            if denominator <= i:
                if N_COINS[i-denominator] + 1 < N_COINS[i]:
                    N_COINS[i] = N_COINS[i-denominator] + 1

    return N_COINS[money]

if __name__ == '__main__':
    money = int(input())
    print(money_change_dp(money))