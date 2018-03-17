x=int(input('Enter the maximum limit'));
num1=0;
num2=1;
print(num1);
print(num2);
num3=num1+num2;
while(num3<x):
    print(num3)
    num1=num2;
    num2=num3;
    num3=num1+num2;
