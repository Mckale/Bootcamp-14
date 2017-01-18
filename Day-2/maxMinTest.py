

Min_equal_Max=[]
MinMax=[]

def find_max_min(fruits):      
    if (min(fruits))==(max(fruits)):
        Min_equal_Max.append(len(fruits))

        print(Min_equal_Max)
        return Min_equal_Max
    
    elif(min(fruits))<(max(fruits)):
        MinMax.append(min(fruits))
        MinMax.append(max(fruits))

        print (MinMax)
        return MinMax

        

(find_max_min([1,1,1,1]))
(find_max_min([7,2,1,9,3,0,3,2,]))

