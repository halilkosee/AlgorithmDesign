#------------------------#
#      CSE 321 HW-3      #
#   HALIL IBRAHIM KOSE   #
#        161044105       #
#------------------------#

#-----------------------------------PART-1------------------------------------------#

def boxesAlternate(arr):
	totalmoves=0
	for i in range((int(len(arr)/2)),(int(len(arr)))):
		rightindex = i
		leftindex  = rightindex
		stop=False
		while not stop :
			leftindex = leftindex - 1
			index=leftindex
			if arr[index] == 1 and index == 10:
				stop = True
			elif arr[index] == 1:
				temp = arr[i]
				arr[i] = arr[index+2]
				arr[index+2] = temp
				totalmoves +=1
				stop = True
			elif index == 0:
				temp = arr[i]
				arr[i] = arr[index+1]
				arr[index+1] = temp
				totalmoves +=1
				stop = True
	return totalmoves

# Driver code to test above 

def DrivePart_1():
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print ( str(len(arr)) + " boxes standing in a row; the first " + str(int(len(arr)/2)) + " of them are black (0) and the remaining n boxes are white (1) :" )
    print (arr)
    # 0 represents black box  
    # 1 represents white box
    totalmoves=boxesAlternate(arr)
    print ("Black-White-Black-White Pattern Is : ")  
    print (arr)
    print ("Number Of Moves Is : " + str(totalmoves))  
    
#-----------------------------------------------------------------------------------#

#-----------------------------------PART-2------------------------------------------#

def FakeCoin(arr):

  coins_total = len(arr)
  even = True

  if coins_total % 2 == 0 :
    left = arr[:coins_total // 2]
    right = arr[coins_total // 2:]
  else :
    left = arr[:coins_total // 2]
    right = arr[(coins_total + 1) // 2:]
    even = False

  if even == False and sum(left) == sum(right):
    return arr[coins_total // 2]
    
  elif sum(left) > sum(right) :
    if len(right) == 1:
      return right[0]
    return FakeCoin(right)
  else:
    if len(left) == 1:
      return left[0]
    return FakeCoin(left) 

# Driver code to test above

def DrivePart_2():
  arr=[1,1,1,0.9,1,1,1] 
  print("Array has a fake coin: " + str(arr))
  print("The fake coin is : " + str(FakeCoin(arr)))

  arr=[0.1,0.1,0.09,0.1] 
  print("Array has a fake coin : " + str(arr))
  print("The fake coin is : " + str(FakeCoin(arr)))

  arr=[1.0001,1.0001,1.0001,1.00000001,1.0001,1.0001,1.0001] 
  print("Array has a fake coin : " + str(arr))
  print("The fake coin is : " + str(FakeCoin(arr)))

#-----------------------------------------------------------------------------------#	

#-----------------------------------PART-3------------------------------------------#

# Function to do quick sort 
def quickSort(arr,left,right):
   i = left
   j = right
   pivot = arr[(left + right)//2]

   swap_count_quick_sort = 0
   while i <= j:
      while arr[i] < pivot:
         i += 1
      while pivot < arr[j]:
         j -= 1
      if i <= j:
         temp = arr[i]
         arr[i] = arr[j]
         arr[j] = temp
         swap_count_quick_sort += 1
         i += 1
         j -= 1

   if left < j:
      swap_count_quick_sort += quickSort(arr, left, j)
   if i < right:
      swap_count_quick_sort += quickSort(arr, i, right)

   return swap_count_quick_sort

# Function to do insertion sort 
def insertionSort(arr): 
    swap_count_insertion_sort = 0
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j]
                swap_count_insertion_sort += 1 
                j -= 1
        arr[j + 1] = key 

    return swap_count_insertion_sort 

# Driver code to test above

def DrivePart_3():
    same_array_for_quicksort  = [ 20, 12, 5, 7, 2, 3, 90, 2 ]
    same_array_for_insertionsort  = [ 20, 12, 5, 7, 2, 3, 90, 2 ]
    print ("Array Is Equal For Each Algorithms : " + str(same_array_for_quicksort))
    swap_count_quick_sort = quickSort(same_array_for_quicksort,0,len(same_array_for_quicksort)-1)
    swap_count_insertion_sort = insertionSort(same_array_for_insertionsort)
    print ("Sorted By QuickSort : " + str(same_array_for_quicksort))
    print ("Total Swap Operations For QuickSort Is : " + str(swap_count_quick_sort))
    print ("Sorted By InsertionSort : " + str(same_array_for_insertionsort))
    print ("Total Swap Operations for InsertionSort is : " + str(swap_count_insertion_sort))
    
#-----------------------------------------------------------------------------------#

#-----------------------------------PART-4------------------------------------------#

# Function for calculating median 
def findMedian(arr): 
    # First we sort the array 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
    # check for even case 
    if len(arr) % 2 != 0: 
        return float(arr[len(arr)/2]) 
      
    return float((arr[int((len(arr)-1)/2)] +
                  arr[int(len(arr)/2)])/2.0)

# Driver code to test above

def DrivePart_4(): 
    arr = [ 1, 3, 4, 2, 7, 5, 8, 6 ]
    print("The Unsorted Array Is: " + str(arr))
    result = findMedian(arr)
    print("Median Of The Array Is: " + str(result))
    
#-----------------------------------------------------------------------------------#  

#-----------------------------------PART-5------------------------------------------#

def subs(l):
    if l == []:
        return [[]]

    x = subs(l[1:])

    return x + [[l[0]] + y for y in x]
def mult(l):
    a=1
    if len(l)==0:
        return 0
    for x in l:
        a=a*x
    return a    
    
def find_optimal_sub_array(L,n,r):
  if n == 1:
    return L[0]
  else:
    Opitimal = find_optimal_sub_array(L[1:],n-1,r)
    if mult(L[0]) < mult(Opitimal) and sum(L[0])>=r:
      return L[0]
    else:
        return Opitimal

# Driver code to test above 
def DrivePart_5():
    arr = [2, 4, 7, 5, 22, 11]
    print("Array is : " + str(arr))
    sub_arrays = subs(arr)
    optimal_sub_array = find_optimal_sub_array (sub_arrays , len(sub_arrays) , (min(arr)+max(arr))*(len(arr)/4))
    print("Opitimal Sub Array Is : " + str(optimal_sub_array))
    
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













