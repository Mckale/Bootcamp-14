class BinarySearch(list):
    def __init__(self,a,b):
        length=a
        self.search_list=[x for x in range(b,length+1,b)]
    def search(self,item):
        count=0 #increments whenever iteration is made
        result={'count':0,'index':-1}
        first=0
        last=len(self.search_list)-1
        found=False # will be set to True if element is found in the list
        while (first<=last and not found):
            mid=int((first+last)/2) #mid point
            if self.search_list [mid]==item:
                found=True
            elif self.search_list[mid]>item:
                last=mid-1
            else:
                first=mid+1
            count+=1
        if not found:
            mid=-1
        result['count']=count
        result['index']=mid
        return result
        
#Test case example
#x=binarysearch(20,1)
#print (x.search_list)
y=BinarySearch(880,40)
print (y.search_list)
print (y.search(880))

