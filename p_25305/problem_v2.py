N, k = map(int, input().split())
x = list(map(int, input().split()))

y=x[:N]
y.sort()
y.reverse()
print(y[k-1])