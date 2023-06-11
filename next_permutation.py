a = [3,2,4,5,2,1]
a.reverse()
el = [a[0]]
for value in a[1::]:
    if value >= max(el):
        el.append(value)
    else:
        el.append(value)
        el.sort()
        b = el[el.index(value) + 1]
        nextValue = el[el.index(value) + 1]
        a[a.index(value)] = nextValue
        a[a.index(b)] = value
        firstlist = a[:a.index(nextValue):]
        a.reverse()
        a = a[:a.index(nextValue)+1:]
        a.extend(firstlist) 
        break
print(a)