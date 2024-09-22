def fibonacci_last_digit(n):
    if n <= 1:
        return n
    else:
        fib = (0,1)
        second_last, last = fib
        for _ in range(2,n+1):
            second_last, last = last, (second_last+last)%10
    return last


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
