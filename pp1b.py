a=0
b=1
n=int(input("enter the numbers"))
fib=[a,b]
while b<n:
    a,b=b,a+b
    fib.append(b)
print(fib)
