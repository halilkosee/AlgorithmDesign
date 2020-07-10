#dynamic programming algorithm to solve problem
a=[[1,10],[3,2]]
def takefirst(elem):#to use for sort function
    return elem[1]#while sorting elements in list we should take second element from each list
def work(L):
    L.sort(key=takefirst)#sorting list for belong to their priorities
    L.reverse()#after sorting we should reverse to find dicreasing list
   #priority list
    
    temp=0
    total=0
    for i in range(len(L)):#while in list
        total=((L[i][0]+temp)*L[i][1])+total
        temp+=L[i][0]
        
    return total    
        
print(work(a))
