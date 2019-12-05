

n, q = list(map(int, input().split()))

c = []
for x in range(n-1):
    c.append(list(map(int, input().split())))

a = list(map(int, input().split()))

v=[]
for x in range(q):
    i = input().split()
    # v.append(i)
    if len(i)==3:
        v.append([ i[0], int(i[1]), int(i[2]) ])
    else:
        v.append([ i[0], int(i[1]) ])

print()
print()
print(n)
print(c)
print(a)
print(q)
print(v)
print()
print()

for i in v:
    # print(i)
    if i[0]=="?":
        print("?    > ",i)
    elif i[0]=="+":
        print("+    > ",i)
    else:
        print("some error")
