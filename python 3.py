#program to find factorial of any entered number.
n=int(input('enter the number'))
fact=1
for i in range(1,n+1):
    fact=fact*i
print('factorial is',fact)
            
