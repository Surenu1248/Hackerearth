MAX =1000000
t = int(input())
lst = []
for i in range(t):
    lst.append(int(input()))
 
s_p = [0 for i in range(MAX+4)]
s_c = [0 for i in range(MAX+4)]
def my_prime_factor():
    s_p[1]=1
 
    for i in range(2,MAX+1):
        if(s_p[i]==0):
            for j in range(i*2,MAX+1,i):
                if(s_p[j]==0):
                    s_p[j]=1
                    s_c[i]+=1
my_prime_factor()
 
for i in lst:
    print(s_c[i]+1)
