x=int(input('Enter the start value :'));
y=int(input('Enter the last value :'));
for num in range(x,y+1):
    flag=0;
    for each in range(2,num-1):
        if(num%each==0):
            flag=1;
            break;
    if(flag==0):
        print(num);
    
