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

def r270(n):
  for i in range(n):
    print("* "*(n-i))
r270(int(input()))


def r270(n):
  for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

r270(int(input()))