'''N = int(input())
count = 0
while N>0:
  t,c = map(int,input().split())
  if c - t >=2:
    count +=1
print(count)'''



'''
        A
      C B
    F E D
  J I H G
O N M L K'''

n=int(input())
val=ord("A")
for i in range(1,n+1):
  a=val
  for j in range(n):
    if j<n-i:
      print(" ",end=" ")
    else:
      print(chr(val),end=" ")
      val-=1
  val=a+(i+1)
  print()