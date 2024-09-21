p1=input("enter name 1")
p2=input("enter name 2")
x=list(p1)
y=list(p2)
il=list("flames")
for i in x:
  for j in y:
    if(i==j):
        p=x.index(i)
        q=y.index(j)
        x=x[:p]+x[p+1:]
        y=y[:q]+y[q+1:]
        break
c=len(x)+len(y)
if(c<7):
  ii=c-1
  il.remove(il[ii])
  for i in range(4):
  
    ii=(ii+c-1)%len(il)
    if(ii>len(il)):
      ii=ii%len(il)
    il.remove(il[ii])
  print(il)
else:
  ii=c%6-1
  il.remove(il[ii])
  for i in range(4):
  
    ii=(ii+c-1)%len(il)
    if(ii>len(il)):
      ii=ii%len(il)
    il.remove(il[ii])
  print(il)
