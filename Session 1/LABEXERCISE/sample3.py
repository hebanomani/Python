max=0
min=9999999;
for x in range(1,10):
    num=int(input('Enter the number'));
    if max<num:
        max=num;
    if min>num:
        min=num;
print("Maximum number is : ",max);
print("Minimum number is : ",min);


