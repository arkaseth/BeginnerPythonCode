lst=[]
def sort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
n=int(input('Enter no. of elements'))
for i in range(n):
    x=int(input())
    lst.append(x)
sort(lst)
print(lst)
