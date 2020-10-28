t = int(input())
lst = []
for i in range(t):
    waste = int(input())
    lst.append(input().split(' '))
#print(lst)
for i in range(t):
    fn = []
    for j in lst[i]:
        fn.append(int(j))
    fn.sort()
    print(str(fn[::-1])[1:-1].replace(",",''))
