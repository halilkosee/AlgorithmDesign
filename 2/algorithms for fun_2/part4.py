#function to delete zeros given list
def delete_zeros(lis):
    output=[]
    for i in lis:
        if i>0:
            output.append(i)
    return output
#function taking a graph of all friends relations 
def invited(graph):
    L=[] #to hold invited list
    for a in graph:#Firstly added all friends in invited list,in next steps they will be eliminated.
        L.append(a)
        
    for node in range(1,len(L)):
        if len(graph[node+1])<5:#friends have not have 5 more friends,they will be zero
            for i in range(1,len(L)+1):
                for j in range(len(graph[i])):
                    if graph[i][j]==L[node]:
                        graph[i][j]=0
                graph[i]=delete_zeros(graph[i])#eliminate the zeros in graph       
            L[node]=0
            
    for node in range(len(L)):
        if len(graph[node+1])<5:
            L[node]=0
            del (graph[node+1])
    L=delete_zeros(L)#delete zeros in invited List (divide)
    a=len(L)  
    index=-1
    for node in L:
        index+=1
        if len(graph[node])>a-5:#friend have more than relations (all-5)
            for j in range(len(graph[node])):
                graph[node][j]=0
            graph[node]=delete_zeros(graph[node])#eliminate the zeros here
            L[index]=0#change with 0 node we would eliminate
    index2=-1        
    for node in L:
        index2+=1
        if len(graph[node+1])>a-5:
            L[index2]=0
            del (graph[node+1])
    L=delete_zeros(L)        
        
    return print("Alice can invite",len(L),"friends.The list of the invited friends is",L)      
graph=[]#here will be the graph that shows all relations between friends.
invited(graph)
