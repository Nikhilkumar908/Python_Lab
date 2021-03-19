#program to check entered year is leap year or not.
x=int(input('Enter the year'))
if(x%4)==0:
        if(x%100)!=0:
            print("a leap year",x)
else:
    print('not a leap year',x)
