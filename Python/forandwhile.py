for i in range(-15,16,1):
      print(i,end=" ")

print()

num = -15
while num<=15:
      print(num,end=" ")
      num +=1

print()

a=1
b=5
for i in range(3):
      c=a^b
      a+=1
      b-=1
print(c)

a=1
b=5
for i in range(3):
      c=(a&b)+1
      if c >3:
            c=8
      a+=1
      b-=1
print(a+b+c)

a=10
b=20
for i in range(3):
      c=(a&b)+1
      if c >3:
            c=8
      a+=1
      b-=1
print(a+b+c)