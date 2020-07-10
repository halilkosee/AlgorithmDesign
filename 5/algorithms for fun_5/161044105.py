#------------------------#
#      CSE 321 HW-4      #
#   HALIL IBRAHIM KOSE   #
#        161044105       #
#------------------------#

#-----------------------------------PART-1------------------------------------------#
  #1b
def findSpecial(array):
    posibility = False;
    found = False
    positions = []
    for i in range(len(array)-1):
        for j in range(len(array[i])-1):
            if (array[i][j] + array[i+1][j+1]) <= (array[i][j+1] + array[i+1][j]):
                continue
            else:
                posibility=True;
                positions.append(str(i)+" "+str(j+1))
                positions.append(str(i+1)+" "+str(j))

    if posibility == True:
        for i in range(len(positions)):
            if positions.count(positions[i])==True:
                found=True
                print ("Chance positions "+ str(positions[i]) + " to reach special array")
        if found==False:
            print ("No way with one move")

    else:
        print ("its already special!")
  #----------------------------------------

  #1c
def helperFindLeftMost(arr):
    leftMin=0
    Min = arr[0]
    for item in arr :
        if item <= Min :
            leftMin = item
            Min = item
    return leftMin,Min

def findLeftMost(arr) :
    
    
    for item in arr:

        leftMin,min_element = helperFindLeftMost(item)
        
        print("Minimum value of " + str(item) + " is : "+ str(leftMin)),

# Driver code to test above

def DrivePart_1():
    print("                ***1-B***\n")
    special = [ [10,17,13,28,23],[17,22,16,29,23],[11,13,6,17,7],[24,28,22,34,24],[45,44,32,37,23],[36,33,19,21,6],[75,66,51,53,34] ]
    
    print("Array is :" + str(special))
    findSpecial(special)
    print("\n")
    print("                *********\n")
    print("                ***1-C***\n")
    findLeftMost(special)
    print("\n")
    print("                *********\n")


#-----------------------------------------------------------------------------------#

#-----------------------------------PART-2------------------------------------------#

def  kthElement(arr1,arr2,k):
    if len(arr1) == 0:
        return arr2[k]
    if len(arr2) == 0:
        return arr1[k]

    mid1 = len(arr1) // 2
    mid2 = len(arr2) // 2

    if mid1+mid2<k:
        if arr1[mid1] > arr2[mid2]:
            return kthElement(arr1, arr2[mid2+1:], k-mid2-1)
        else:
            return kthElement(arr1[mid1+1:], arr2, k-mid1-1)
    
    else:
        if arr1[mid1]>arr2[mid2]:
            return kthElement(arr1[:mid1], arr2, k)

        else:
            return kthElement(arr1, arr2[:mid2], k) 


# Driver code to test above

def DrivePart_2():
    arr1 = [2, 3, 6, 7, 9] 
    arr2 = [1, 4, 8, 10] 
    k = 5 
    print ("First Array Is :" + str(arr1))
    print ("Second Array Is :" + str(arr2))

    print(str(k) + "th Element Of Merged Two Sorted Arrays Is " + str(kthElement(arr1, arr2, k-1))) 

#-----------------------------------------------------------------------------------#

#-----------------------------------PART-3------------------------------------------#

def helper(array, left, right):
    #Helper recursive function. Return the boundary of subset as low and high indexes.

    if left == right: 
        return (left, right)

    # middle.
    mid = (left + right) // 2

    # divide
    left = helper(array, left, mid)

    # divide
    right = helper(array, mid + 1, right)

    # conquer
    return helper2(array, left, right)

def helper2(array, left, right):
    #Helper to merge the left and right subsets.

    left_sum = sum(array[left[0]:left[1] + 1])

    right_sum = sum(array[right[0]:right[1] + 1])

    # If left and right subsets are contiguous.
    if (right[0] - left[1]) == 1:

        # Calculate the both subset sum.
        left_right_sum = left_sum + right_sum

        # return low from left subset, high from right subset.
        if right_sum <= left_right_sum and left_sum <= left_right_sum:
            return (left[0], right[1])
    else: 

        # Calculate the sum of range.
        range_sum = sum(array[left[0]:right[1] + 1])

        # between two subsets and return low and high indexes.
        if right_sum <= range_sum and left_sum <= range_sum:
            return (left[0], right[1])

    # Otherwise, return the subset that has largest sum.
    return right if left_sum < right_sum else left

def get_largest_sum(array):
 
    if not array:  # If it is empty return None.
        return None

    # The helper returns the lower and higher indexes of the subset.
    low, high = helper(array, 0, len(array) - 1)

    return array[low:high + 1]

# Driver code to test above

def DrivePart_3():
    arr = [5, -6, 6, 7, -6, 7, -4, 3]
    print("The Array Is : " + str(arr))
    largest_sum=get_largest_sum(arr)
    print("The largest contiguous subset for largest sum : ",largest_sum,", Sum : ",sum(largest_sum))
    
#-----------------------------------------------------------------------------------#

#-----------------------------------PART-4------------------------------------------#

# program to find out whether a given 
# graph is Bipartite or not using Divide and Conquer. 

V = 4
def colorGraph(G, color, pos, c): 
    
    if color[pos] != -1 and color[pos] != c: 
        return False
        
    # color this pos as c and all its neighbours and 1-c 
    color[pos] = c 
    ans = True
    for i in range(0, V): 
        if G[pos][i]: 
            if color[i] == -1: 
                ans &= colorGraph(G, color, i, 1-c) 
                
            if color[i] !=-1 and color[i] != 1-c: 
                return False
        
        if not ans: 
            return False
    
    return True


def isBipartite(G): 
    
    color = [-1] * V 
        
    #start is vertex 0 
    pos = 0
    # two colors 1 and 0 
    return colorGraph(G, color, pos, 1) 

def DrivePart_4(): 

    G = [[0, 1, 0, 1], 
        [1, 0, 1, 0], 
        [0, 1, 0, 1], 
        [1, 0, 1, 0]] 
    print("Grap is :",G)
    if isBipartite(G): print("Yes it is Bipartite") 
    else: print("No,it is not Bipartite") 
    
#-----------------------------------------------------------------------------------#  

#-----------------------------------PART-5------------------------------------------#

def helper_to_return_gain_list(firstDay,secondDay):
    #Function to return gain list of all days
    res_list = [ secondDay[i+1] - firstDay[i] for i in range(len(firstDay)-1)]
    return res_list

def find_largest(mylist):
    #finds max profit day
    if len(mylist) == 1:
        return 0
    elif len(mylist) == 2:
        if mylist[0] > mylist[1]:
            return 0
        else:
            return 1
    else:
        m = len(mylist) // 2
        blist = mylist[0:m]
        clist = mylist[m:len(mylist)]
        largest_b = find_largest(blist)
        largest_c = find_largest(clist) + m
        if mylist[largest_b] > mylist[largest_c]:
            return largest_b
        else:
            return largest_c

def DrivePart_5():
    
    C = [5,11,2,21,5,7,8,12,13,0]
    P = [0,7,9,5,21,7,13,10,14,20]

    gain = helper_to_return_gain_list(C,P)
 
    maxday = find_largest(gain)
    print("The best day to buy goods is the " + str(maxday+1) + "th day because if you buy the goods on the " + str(maxday+1) + "th day and sell them on the " + str(maxday+2) + "th day,")
    print("you can make " + str(gain[maxday]) + " units of money, which is the maximum possible gain in the schedule.")
       
#-----------------------------------------------------------------------------------#  

def TEST():
    print("***********PART-1******************\n")
    DrivePart_1()
    print("\n")
    print("***********PART-2******************\n")
    DrivePart_2()
    print("\n")
    print("***********PART-3******************\n")
    DrivePart_3()
    print("\n")
    print("***********PART-4******************\n")
    DrivePart_4()
    print("\n")
    print("***********PART-5******************\n")
    DrivePart_5()
    print("\n")

TEST()