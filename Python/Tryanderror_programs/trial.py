'''N = int(input())
count = 0
while N>0:
  t,c = map(int,input().split())
  if c - t >=2:
    count +=1
print(count)'''


n = int(input())
val =ord("A")
a = ord("a")
for i in range(n):
  for j in range(n):
    if j==n//2:
        print(chr(val+i),end=" ")
        val+=1
    elif i==n//2:
      print(chr(a+j),end=" ")
      a+=1
    elif i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()