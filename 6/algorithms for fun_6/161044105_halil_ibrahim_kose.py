#------------------------#
#      CSE 321 HW-5      #
#   HALIL IBRAHIM KOSE   #
#        161044105       #
#------------------------#

#-----------------------------------PART-1------------------------------------------#

def minimumCost(NY,SF,M):
    optN = [NY[0]]
    optS = [SF[0]]
    for i in range(1,len(NY)):
        optN.append(NY[i] + min(optN[i - 1], (M + optS[i - 1])))
        optS.append(SF[i] + min(optS[i - 1], (M + optN[i - 1])))

    return min(optN[len(optN)-1],optS[len(optS)-1])
# Driver program to test above function
def DrivePart_1():
    M = 10
    NY = [1,3,20,30]
    SF = [50,20,2,4]
    print("------------------------")
    print("Number of Months (n) : ", len(NY))
    print("Moving Cost (M) : ", M)
    print("------------------------")
    print("NY : ",NY)
    print("SF : ",SF)
    print("------------------------")
    print("The Cost of Optimal Plan: ", minimumCost(NY,SF,M))
    print("------------------------")
	
#-----------------------------------------------------------------------------------#  

#-----------------------------------PART-2------------------------------------------#
"""The following implementation assumes that the activities 
are already sorted according to their finish time"""

"""Prints a maximum set of activities that can be done by a 
single person, one at a time"""
# n --> Total number of activities 
# s[]--> An array that contains start time of all activities 
# f[] --> An array that contains finish time of all activities 

def printMaxActivities(s , f ): 
    n = len(f) 
    print ("The following seasons are selected")

    # The first season is always selected 
    i = 0
    print (i+1, end = '  ') 

    # Consider rest of the seasons 
    for j in range(n): 

        # If this season has start time greater than 
        # or equal to the finish time of previously 
        # selected season, then select it 
        if s[j] >= f[i]: 
            print (j+1, end = '  ') 
            i = j 

# Driver program to test above function 
def DrivePart_2():
    
    s = [1 , 3 , 0 , 5 , 8 , 5] 
    f = [2 , 4 , 6 , 7 , 9 , 9] 
    print("------------------------")
    for i in range(6):
        print ( "Season " + str(i+1) + " begins at t=" + str(s[i]) +" and finishes at t=" + str(f[i])),
    print("------------------------")

    printMaxActivities(s , f) 

#-----------------------------------------------------------------------------------#  
#-----------------------------------PART-3------------------------------------------#

def subset_with_the_total_sum_of_elements_equal_to_zero (index, Sum, arr, seen, results, current) : 
    
    if (index == len(arr)) : 
        if (Sum == 0) : 
            print("Subset With The Total Sum Of Elements Equal To Zero : " + str(current))
            return -1
        else : 
            return 0 
      
    if (seen[index][Sum + len(arr)]) : 
        return results[index][Sum + len(arr)]
    
    current.append(arr[index])
    seen[index][Sum + len(arr)] = 1 

    results[index][Sum + len(arr) ] = subset_with_the_total_sum_of_elements_equal_to_zero(index + 1, Sum + arr[index], arr, seen, results, current) 
    current.remove(arr[index])  
    results[index][Sum + len(arr)] += subset_with_the_total_sum_of_elements_equal_to_zero(index + 1, Sum, arr, seen, results, current)
    
    return results[index][Sum + len(arr)]


# Driver program to test above function 
def DrivePart_3():
    arr = [-1, 6, 4, 2, 3, -7, -5]
    print("Array is : " + str(arr))
    current = []
    print("------------------------")
    #7 is length of array 100 is memory
    seen = ([[0 for i in range(100)]for i in range(7)])
    results = ([[0 for i in range(100)]for i in range(7)])
    subset_with_the_total_sum_of_elements_equal_to_zero(0, 0, arr , seen, results, current)
    
#-----------------------------------------------------------------------------------#  


#-----------------------------------PART-4------------------------------------------#
def minimum_cost(x, y):
    """Do a local alignment between x and y"""
    # create a zero-filled matrix
    Table = create_table(len(x) + 1, len(y) + 1)

    # fill in A in the right order
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            # the local alignment recurrance rule:
            Table[i][j] = max(
            Table[i][j-1] + (-1),
            Table[i-1][j] + (-1),
            Table[i-1][j-1] + ((2)if x[i] == y[j] else (-2)),
            0 
            )
            # track the cell with the optimal cost
    # return the best location            
    return Table[i][j]           

def create_table(sizex, sizey):
    """Creates a sizex by sizey matrix filled with zeros."""
    return [[0]*sizey for i in range(sizex)]


# Driver program to test above function 
def DrivePart_4():
    S1 = "ALIGNMENT"
    S2 = "SLIME"
    print("First Sequence : " + S1)
    print("Second Sequence : " + S2)
    print("------------------------")
    result=minimum_cost(S1,S2)    
    print("Minimum Cost : " + str(result))
    
#-----------------------------------------------------------------------------------#  

#-----------------------------------PART-5------------------------------------------#
# Python program to find sum of elements in list
def add_elements(arr):
  #1-this algorithm finds first and second smallest integer in array 
  #2-then delete these two smallest alements in array
  #3-then insert sum of these two smallest in array
  #4-recursivly send new array as parameter
  #return if there is one element in array
    if not arr:
        return 0
    elif len(arr)==1:
        return arr[0]
    else:
        m1, m2 = float('inf'), float('inf')
        for x in arr:
            if x <= m1:
                m1, m2 = x, m1
            elif x < m2:
                m2 = x
   
        arr.remove(m1)
        arr.remove(m2)
        arr.append(m1+m2)
    return add_elements(arr)

def DrivePart_5():
    list1 = [11, 5, 17, 18, 23] 
    print("Given Array is : " + str(list1))
    print("------------------------")
    total=add_elements(list1)
    # printing total values 
    print("Sum Of Elements : " + str(total))
   

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

