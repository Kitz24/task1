a=input("enter no: ")
x=list(map(int,a.split()))
c=0
for i in x:
    if int(i)>0:
        if str(i)[::-1]==str(i):
            c=c+1
        else:
            pass
    else:
        c=0
        break
if c>0:
    print(True)
else:
    print(False)
