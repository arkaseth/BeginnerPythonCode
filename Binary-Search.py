"""Binary search"""
pos=-1
def finder(lst,n):
    l=0
    u=len(lst)-1
    while l<=u:
        mid=(u+l)//2
        if lst[mid]==n:
            globals()['pos']=mid
            return True
            break
        else:
            if lst[mid]<n:
                l=mid+1
            else:
                u=mid-1
    else:
        return False
lst=[]
n=int(input('Enter no. of elements'))
for i in range(n):
    x=int(input())
    lst.append(x)
k=int(input("Enter element to search:"))
if finder(lst,k):
    print("Found at {}!!".format(pos))
else:
    print("Not found :(")
