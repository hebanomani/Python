num=input('Enter the number');
digit=input('Enter the digit to search');
count=0
for value in num:
    if(value==digit):
        count=count+1;
if count==0:
    print(digit, " is not available in ", num);
else:
    print("The total count of ", digit, " in ",num, " is ",count);
