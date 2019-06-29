"""Linear search"""
def finder(lst,n):
    for i in lst:
        if i==n:
            return True
            break
    else:
        return False
lst=[]
n=int(input('Enter no. of elements'))
for i in range(n):
    x=int(input())
    lst.append(x)
k=int(input("Enter element to search:"))
if finder(lst,k):
    print("Found!!")
else:
    print("Not found :(")
