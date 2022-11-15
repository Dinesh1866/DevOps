'''N = int(input())
count = 0
while N>0:
  t,c = map(int,input().split())
  if c - t >=2:
    count +=1
print(count)'''


n = int(input())
for i in range(1,n+1):
  print("* "*i)