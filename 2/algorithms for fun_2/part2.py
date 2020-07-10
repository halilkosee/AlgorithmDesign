#A utility function to check whether a word is present in dictionary or not.
def Dictionary(word):
    dictionary=["the","flower","in","from","high","i", "like","and","go","i","like","ice","cream"]
    size=len(dictionary)/len(dictionary[0])
    for i in range(int(size)):
        if dictionary[i]==word:
            return 1
    return 0 
#Returns true if string can be segmented into space separated 
#words, otherwise returns false 
def Dict(str):
    size=len(str)
    if size==0:
        return 1
    wb=[]
    for x in range(size+1):
        wb.append(0)
# Create the DP table to store results of subroblems. The value wb[i] 
# will be true if str[0..i-1] can be segmented into dictionary words, 
# otherwise false.     
    for i in range(1,size+1):
# if wb[i] is false, then check if current prefix can make it true. 
# Current prefix is "str.substr(0, i)" 
        temp1=Dictionary(str[0:i])
        if wb[i]==0:
            if temp1==1:
                wb[i]=1;
#wb[i] is true, then check for all substrings starting from 
# (i+1)th character and store their results. 
        if wb[i]==1:
#If we reached the last prefix         
            if i==size:
                return 1
            for j in range(i+1,size):
#Update wb[j] if it is false and can be updated 
#Note the parameter passed to dictionaryContains() is 
#substring starting from index 'i' and length 'j-i'                 
                temp2=Dictionary(str[i:j-1])
                if wb[j]==0:
                    if temp2==1:
                        wb[j]=1
                if j==size:
                    if wb[j]==1:
                        return 1               
    return 0         
#-------------DRIVER CODE-----------------#              
if Dict("in")==1:
    print("true")
else:
    print("false")
#-------------------------#    
if Dict("highfrom")==1:
    print("true")
else:
    print("false")    
#-------------------------#     
if Dict("illikeflower")==1:
    print("true")
else:
    print("false")    
#-------------------------# 
if Dict("")==1:
    print("true")
else:
    print("false")    
#-------------------------# 
        
