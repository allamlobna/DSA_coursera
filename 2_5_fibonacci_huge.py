def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    else:
        second_last, last = 0, 1
        for i in range(0,m*m):
            second_last, last = last, (second_last+last)%m
            if second_last == 0 and last == 1:
                period = i+1
    n_reduced = n%period

    if n_reduced <= 1:
        return n_reduced
    else:
        second_last, last = 0,1
        for _ in range(n_reduced - 1):
            second_last, last = last, (second_last+last)%m
        return last


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
