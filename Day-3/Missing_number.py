
def Missing_numbers(l1,l2):
    diff=set(l1).symmetric_difference(set(l2))#Gives back the extra numbers missing in the second list
    if len(l1)==0 and len(l2)==0:
        print([0])
        return[0]#Returns [0] when the two lists are empty
    elif len(diff)==0:
        print([0])
        return[0]#Returns [0] when the two lists have similar elements
    else:
        print(list(diff))
        return diff# Returns the missing number in the second list

Missing_numbers([1,2,3],[1,2,3,4])
Missing_numbers([4,66,7],[66,7,4])
Missing_numbers([],[])
