#program to check prime no.
x = int(input('Enter the number:- '))
if(x>1):
    for i in range (1,int(x/2)+1):
        if(x%i)==0:
            print("the no is not a prime no.",x)
            break
    else:
        print('the no is a prime no.',x)
else:
    print("the no is not a prime no.",num)
