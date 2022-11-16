'''N = int(input())
count = 0
while N>0:
  t,c = map(int,input().split())
  if c - t >=2:
    count +=1
print(count)'''

'''
A B C D E
J I H G F
K L M N O
T S R Q P
U V W X Y'''
n = int(input())
val = ord("A")
for i in range(1,n+1):
  for j in range(n):
    if i%2==1:
      print(chr(val),end=" ")
      val+=1
    else:
      print(chr(val),end=" ")
      if j==n-1:
        val+=1
      else:val-=1
  val+=(n-1)
  print()