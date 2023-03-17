n = 100
a = list(range(n+1))
a[1] = 0
i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1
b=[]
for k in a:
    if k != 0:
        b.append(k)

print(len(b))

        