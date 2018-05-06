# THIS FUNCTION HELPS TO SEARCH INDEX OF NUMBER IN ARRAY

def  LineSearch (x,array):
     for i in range (len(array)):
         if array[i]==x:
             return i
         elif 1==1:
             i=i+1
         else:
             return -1
arr=[5,0,535,4]
print(LineSearch(0,arr))
