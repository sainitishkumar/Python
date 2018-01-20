def fn(a):
   x=0
   for i in range(0,len(str(a))):
      x=x+int(a[i])
      
   print(x)
integer=input()
list1=''
for i in range(0,len(str(integer))) :
   if i+1<len(str(integer)):
      if (integer[i]==integer[i+1]):
           list1=list1+str(integer[i])

if integer[len(str(integer))-1]==integer[0]:
   list1=list1+integer[0]

fn(list1)
print('nitish')
