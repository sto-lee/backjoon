def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    fir = merge_sort(arr[:mid])
    fin = merge_sort(arr[mid:])

    return sort(fir, fin)

def sort(fir, fin):
    result = []
    i = j = 0

    while i < len(fir) and j < len(fin):
        if fir[i] > fin[j]:
            result.append(fir[i])
            i += 1
        else:
            result.append(fin[j])
            j += 1
            
    result.extend(fir[i:])
    result.extend(fin[j:])
    return result

N, k = map(int, input().split())
x = list(map(int, input().split()))
x=x[:N]
x = merge_sort(x)
print(x[k-1])