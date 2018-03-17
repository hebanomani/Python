n1=0;
n2=1;
limit=int(input('Enter total number required in a series'));
print(n1);
print(n2);
for x in range(1,limit):
    n3=n1+n2;
    print(n3);
    n1=n2;
    n2=n3;
