s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
n=len(s1)
m=len(s2)
lcs=[[0 for x in range(m+1)]for x in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            lcs[i][j]=1+lcs[i-1][j-1]
        else:
            lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])          
for i in range(len(lcs)):
    print(lcs[i],end="\n")
i=len(s1)
j=len(s2)
pattern=''
while i>0 and j>0:
    if s1[i-1] == s2[j-1]:
        pattern+=s1[i-1]
        i-=1
        j-=1 
    elif lcs[i-1][j] > lcs[i][j-1]:
        i -= 1          
    else:
        j -= 1
print(lcs[-1][-1])
print(pattern[::-1])