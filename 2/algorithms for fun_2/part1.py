A = [190, 220, 410, 580, 640, 770, 950, 1100, 1350] 
def optimal(List):
    path=[]
    penalties=[]
    for i in range (len(List)):
        penalties.append(pow((200 - List[i]), 2))
        path.append(i)
        for j in range(i):
            temp=penalties[j]+pow((200 - (List[i] - List[j])), 2)
            if temp<penalties[i]:
                penalties[i]=temp
                path[i]=j+1
    finalPath = []
    index=len(path)-1
    while index >= 0:
        finalPath.append(index + 1);
        index = path[index] - 1;
        
   
    finalPath.reverse()
    print('Optimal Sequence :',finalPath)
    print('Penalties :', penalties)
    
    
optimal(A)
