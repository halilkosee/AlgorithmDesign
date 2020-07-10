def findOptimal(n,m,A,B):
    moving=0
    plan=[]
    cost=0
    for i in range(n):
        if A[i]<B[i]:
            plan.append(A[i])
            cost=cost+A[i]
            #for first city there is no movement
            if moving==0:
                #curent city number
                moving=1
                #if move from other city
            if moving==2:
                #change the currrent city number
                moving=1
                #sum with movement cost M
                cost=cost+m
                
        if A[i]>B[i]:
            plan.append(B[i])
            cost=cost+B[i]
            #for first city there is no movement
            if moving==0:
                #curent city number
                moving=2
                #if move from other city
            if moving==1:
                #change the currrent city number
                moving=2
                #sum with movement cost M
                cost=cost+m      
    return ("cost of optimal plan",plan,"is",cost)
#Driver Part    
Ny=[1,3,50,60]
Sf=[40,30,4,5]            
print(findOptimal(4,10,Ny,Sf))                 
