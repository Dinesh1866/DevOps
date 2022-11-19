'''N = int(input())
count = 0
while N>0:
  t,c = map(int,input().split())
  if c - t >=2:
    count +=1
print(count)'''

'''
A F J M O
B G K N
C H L
D I
E'''
'''def f1(n):
  val=ord("A")
  for i in range(n):
    a=val
    for j in range(n):
      if j<n-i:
        print(chr(val),end=" ")
        val= val+(n-j)
    val = a+1
    print()

f1(int(input()))'''

'''
A F K P U
B G L Q V
C H M R W
D I N S X
E J O T Y'''
'''def f1(n):
  val=ord("A")
  for i in range(n):
    a=val
    for j in range(n):
      print(chr(val),end=" ")
      val+=n
    val = a+1
    print()

f1(int(input()))'''
'''n = int(input())
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
  print()'''


'''n = int(input())
val = ord("A")
for i in range(n):
  for j in range(n):
    if i%2==0:
      print(chr(val),end=" ")
      val+=1
    else:
      print(chr(val),end=" ")
      if j==n-1:
        val+=1
      else:val-=1
  val+=(n-1)
  print()'''


def f1(n):
  for i in range(n):
    for j in range(n):
      #if i<=j:
      if j>=i:
        print("*",end=" ")
      else:
        print(" ",end=" ")
    print()

f1(int(input()))

n =5
for i in range(n):
        print(("  "*i)+("* "(n-i)),end=" ")