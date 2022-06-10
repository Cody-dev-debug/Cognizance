for i in range(0,50):
    d=0
    n=i
    while(n>0):
       r=n%10
       d=d+r
       n=int(n/10) 
    if(d==5):
       print("Good Evening, Cognizance",i)
