def main():
    print("\tEntry")
    output = []
    while True:
        T = int(input())
        if 1 <= T <= 5000:
            break
        print('Try again, T value is not correct, the ' 
                + 'following condition must be met: (1 <= T <= 5000)')
    for _ in range(int(T)):
        while True:
            nm = input()
            n,m = map(int,nm.split())
            if 1 <= n <= 10**9 and 1 <= m <= 10**9:
                break
            print('Try again, N and M values are not correct, the '
                    + 'following condition must be met: (1 <= N,M <= 10^9)')
        if m >= n:
            if n % 2 == 0:
                output.append('L')
            else:
                output.append('R')
        elif m % 2 == 0:
            output.append('U')
        else:
            output.append('D')
    print('\tOutput')
    print('\n'.join(output))


main()