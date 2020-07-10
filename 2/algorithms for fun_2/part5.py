def sat(m):
    L=[] #put variables in list
    control=0#to control whether its satisfied
    for current in m:#to compare al variable with one of them
        for node in m:#during list length
            if current==node:#if tey are equals continue
                control+=1#increase 1 control
                if control>=len(m):#if it is on last variable
                    return 1#it measn all variable comparisons finished so return true
            return 0#else return 0   
