'''N = int(input())
count = 0
while N>0:
  t,c = map(int,input().split())
  if c - t >=2:
    count +=1
print(count)'''


n = int(input())
val = ord("A")
for i in range(n):
  a=val
  for j in range(i+1):
    print(chr(val),end=" ")
    val-=1
  val=a+1
  print()

'''val = ord("A")
for i in range(1,n+1):
  print(f"{chr(val)} "*i)
  val +=1'''