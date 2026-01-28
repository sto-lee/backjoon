N = input()
arr = []
for i in N:
    arr.append(i)

arr.sort(reverse=True)
print("".join(arr))