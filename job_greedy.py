job=[1,2,3,4,5,6]
deadlines=[5,3,3,2,4,2]
profit=[200,180,190,300,120,100]
max_d=max(deadlines)
n=len(job)
optimal_schedule=[None]*max_d
for i in range(n):
    for j in range(i+1,n):
        if(profit[i]<profit[j]):
            temp=profit[i]
            profit[i]=profit[j]
            profit[j]=temp
            
            temp=deadlines[i]
            deadlines[i]=deadlines[j]
            deadlines[j]=temp

            temp=job[i]
            job[i]=job[j]
            job[j]=temp           
total_profit=0
for i in range(n):
    d=deadlines[i]-1
    while(d>=0):
        if(optimal_schedule[d]==None):
            optimal_schedule[d]=job[i]
            total_profit+=profit[i]
            break
        else:
            d=d-1  
print(job)         
print(optimal_schedule)
print(total_profit)