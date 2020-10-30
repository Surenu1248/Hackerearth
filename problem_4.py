'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
lst1 = [x for x in input().split(' ') if x != '']
lst2 = [x for x in input().split(' ') if x != ''] 
for i in range(0,len(lst1)):
    lst1[i] = int(lst1[i])
for i in range(0,len(lst2)):
    lst2[2] = int(lst2[2])

lst3 = []
for i in range(int(lst1[1])):
    lst3.append(input().strip())
#print(lst1)
#print(lst2)
#print(lst3)

def subArraySum(arr,n):
    temp,res = 0,0
    for i in range(0,n):
        temp = 0
        for j in range(i,n):
            temp +=1
            res+=temp
    return res

for i in lst3:
    t1 = []
    for j in i.split(' '):
        t1.append(int(j))
    #print(t1)
    sum = 0
    if(t1[0] == t1[1]):
        for i in range(t1[1]+1):
            sum+=i
        print(sum)
    else:
        t2 = []
        if t1[1] - t1[0] == 1:
            print(t1[0]*t1[1]+t1[1])
        elif t1[0] != 1:
            for l in range(1,t1[0]):
                t2.append(l)
            xyz = subArraySum(t2,len(t2))
            #print(t2,xyz)
            
            t2 = []
            for k in range(1,t1[1]+1):
                t2.append(k)
            print(subArraySum(t2,len(t2))-xyz)

        else:
            for k in range(1,t1[1]+1):
                t2.append(k)
            #print(t2)
            print(subArraySum(t2,len(t2)))










