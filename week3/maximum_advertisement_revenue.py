def max_ad_revenue(prices, clicks):
    prices = sorted(prices)
    clicks = sorted(clicks)

    ret = 0
    for price, click in zip(prices, clicks):
        ret += price * click
    
    return ret


if __name__ == '__main__':
    n = input()

    prices = list(map(int, input().split(' ')))
    clicks = list(map(int, input().split(' ')))

    print(max_ad_revenue(prices, clicks))