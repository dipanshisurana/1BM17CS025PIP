def binary_search(list,no):
    start=0
    end=len(list)-1

    while(start<=end):
        mid=(start+end)//2
        if list[mid]==no:
            return True
        elif list[mid]>no:
            end=mid-1
        else:
            start=mid+1

    return False

print("enter number")
list=[int(i) for i in input().split()]
print("enter the number to be search")
no=int(input())
print(binary_search(list,no))
