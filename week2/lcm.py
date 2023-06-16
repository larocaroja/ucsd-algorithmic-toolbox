def gcd(a, b):
    if b == 0:
        return a
    
    a_prime = a%b
    return gcd(b, a_prime)

def lcm(a, b):
    gcd_ = gcd(a, b)
    p = a/gcd_
    q = b/gcd_

    return int(gcd_ * p * q)

if __name__ == '__main__':
    a, b = map(int, input().split(' '))

    if a>b:
        big = a
        small = b
    else:
        big = b
        small = a

    print(lcm(big, small))