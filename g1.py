
import time
def binary_search(a,target):
    left, right=0,len(a)-1
    while left<=right:
        mid=(left+right)//2
        if a[mid]==target:
            return mid
        elif a[mid]<target:
            left=mid+1
        else:
            right=mid-1



def linear_search(a,target):
    for i in range(len(a)):
        if a[i]==target:
            return i
    return -1
        
            
            



while True:
    print("__MENU__")
    print("1.binary search")
    print("2.linear search")
    print("3.exit")

    opp=int(input("enter your choice"))
    if opp==1:
        start=time.time()
        a=[]
        b=int(input("enter the range"))
        for i in range(b):
            item=int(input("enter the element"))
            a.append(item)
        
        print(a)
        target=int(input("enter the element to search"))
        print(binary_search(a,target))
        end=time.time()
        print(f"take time is {end-start}")
    elif opp==2:
        a=[]
        b=int(input("enter the range"))
        for i in range(b):
            item=int(input("enter the element"))
            a.append(item)
        print(a)
        start=time.time()
        target=int(input("enter the search element"))
        print(linear_search(a,target))
        end=time.time()
        print(f"take time is {end-start}")
        
    elif opp==3:
        print("exit")
        break
    else:
        print("inavid")
        
    
