n=int(input("Enter the no of instances : "))
v=[0]*n
w=[0]*n
r=[0]*n
item=[0]*n
for i in range(n):
    v[i]=int(input("Enter the value of instance "+str(i+1)+" : "))
    w[i]=int(input("Enter the weight of instance "+str(i+1)+" : "))
    r[i]=v[i]/w[i]               
    item[i]=i+1
for i in range(n):
    for j in range(n):
        if r[i]>r[j]:
            temp=r[i]
            r[i]=r[j]
            r[j]=temp
            
            temp=v[i]
            v[i]=v[j]
            v[j]=temp
            
            temp=w[i]
            w[i]=w[j]
            w[j]=temp

            temp=item[i]
            item[i]=item[j]
            item[j]=temp 
print(item)
result=[]
profit=0
bag=int(input("Enter The capacity of the bag : "))
for i in range(n):
    if(bag>0):
        if(w[i] < bag):
            result.append(item[i])
            profit+=v[i]
            bag-=w[i]
        elif (w[i]>bag):
            frac=bag/w[i]
            profit+=(frac*v[i])
            result.append(item[i])
            bag=0
print(result)
print(profit)