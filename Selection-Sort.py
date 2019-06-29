"""Selection Sort"""
lst=[]
def sort(lst):
    for i in range(len(lst)-1):
        minpos = i
        for j in range(i,len(lst)):
            if lst[j]<lst[minpos]:
                minpos=j
        lst[minpos],lst[i]=lst[i],lst[minpos]
n=int(input('Enter no. of elements'))
for i in range(n):
    x=int(input())
    lst.append(x)
sort(lst)
print(lst)
