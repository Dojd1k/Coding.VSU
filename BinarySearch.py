# This function helps to search index of number in ordered list
def BinarySearch (first,last,x,array):
    if last>=first :
        mid=(first+last)//2
        if array[mid]==x:
            return mid
        elif x>array[mid]:
            return (BinarySearch(mid+1,last,x,array))
        else :
            return (BinarySearch(first,mid-1,x,array))

    else:
        return None


arr= [10,20,30,40,50,60,70,80,90,100]
print(BinarySearch(0,len(arr)-1,10,arr))
