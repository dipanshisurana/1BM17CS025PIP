def reverse(str):
    str1=str[::-1]
    li=[]
    li=str.split(" ")
    li.reverse()

    for i in li:
        print(i,end=" ")
        
    print("\n",str1)

str=input("enter the string \n")
reverse(str)
