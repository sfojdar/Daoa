def findMin(V):
    deno=[1,2,5,10,20,50,100,500,1000]
    n=len(deno)
    ans=[]
    i=n-1
    while(i>=0):
        while(V>=deno[i]):
            V-=deno[i]
            ans.append(deno[i])
        i-=1
    for i in range(len(ans)):
        print(ans[i],end=" ")
a=1254
print(a,":",end="")
findMin(a)
'''
sum=93
sum1=sum
denomination=[1,2,5,10,20,50]
denomination.sort(reverse=True)
ans=[]
while sum>0:
    for i in denomination:
        while i<=sum:
            sum=sum-i
            ans.append(i)
print(f'{sum1}:{ans}')
'''