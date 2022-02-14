def fun(arr, n):
    d = -1
    for i in range(0, n):
        j = n - 1
        while (j > i):
            if arr[j] > arr[i] and d < (j - i):
                d = j - i
            j -= 1

    return d

a= int(input())
b=[ ]
for i in range(a):
    i=int(input())
    b.append(i)

print(fun(b,a))