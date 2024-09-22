def gcd(a, b):
    while a%b != 0:
        a, b = b, a%b
    return b


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
