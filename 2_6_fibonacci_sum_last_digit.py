def fibonacci_sum(n):
    period_10 = 60
    if n <= 1:
        return n
    else:
        n_reduced = n%period_10
        second_last, last, _sum = 0,1,1
        if n_reduced <= 1:
            return n_reduced
        for _ in range(n_reduced-1):
            second_last, last = last, (second_last+last)
            _sum+=last
        return _sum%10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
