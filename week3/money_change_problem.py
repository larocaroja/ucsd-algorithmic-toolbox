def represents_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True
    
def money_change(money, denominations = [1, 5, 10]):
    denominations = sorted(denominations, reverse = True)

    n_coins = 0
    for denomination in denominations:
        if money == 0:
            break

        n_coin_temp = money // denomination
        n_coins += n_coin_temp
        money -= int(denomination * n_coin_temp)
    
    return n_coins

if __name__ == '__main__':
    money = input()
    assert represents_int(money), f"variable money should be integer, but got {money}"
    money = int(money)

    # denominations = []
    # for denomination in input().split(' '):
    #     assert represents_int(denomination), f"element of denominations should be integer, but got {denomination}"
        
    #     denominations.append(int(denomination))

    n_coins = money_change(money)
    print(n_coins)