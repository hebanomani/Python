total=0;
avg=0;
for x in range(1,10):
    num=int(input('Enter a number : '));
    total=total+num;
avg=total/10;
print('Sum is : ',total);
print('Average is : ',round(avg,2));
