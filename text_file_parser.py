
def min_location(lis,k) :
    min=lis[0]
    for x in range(k+1,len(lis)) :
        if lis[x] < min :
            min = lis[x]
    
    return x
    

def swap(a,b) :
    temp=a
    a=b
    b=temp    
    
    
def selection_sort() :
    lis=[10.-5,6,1,-4,5,144]
    k=0
    
    for i in range(len(lis)) :
        j = min_location(lis,k)
        k+=1
        swap(lis[j],lis[i])
    print(lis)

selection_sort()


