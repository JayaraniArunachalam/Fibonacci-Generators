def fib(c):
    a,b = 0,1
    count = 0
    while count <=c-1:
        yield a
        a, b= b, a+b
        count +=1
n = int(input("Enter the number of fibonacci numbers to be generated:"))
print("The first", n,"fibonacci series is,")
for i in fib(n):
    print(i,end=" ")


