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

def f1(n):
  val=ord("A")
  for i in range(n):
    a=val
    for j in range(n):
      if j<n-i:
        print(chr(val),end=" ")
        val= val+(n-j)
    val = a+1
    print()

f1(int(input()))