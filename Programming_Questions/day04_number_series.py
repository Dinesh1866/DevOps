# print first n even numbers for given value of n
'''n = int(input())
count = 0
val = 0
while count < 5:
      if val%2==0:
            print(val,end=" ")
            count+=1
      val+=1
print()

#print without 0
n = int(input())
count = 0
val = 1
while count < 5:
      if val%2==0:
            print(val,end=" ")
            count+=1
      val+=1
print()


#with for loop
n = int(input())
for i in range(1,n*2+1):
      if i%2==0:
            print(i,end=" ")
print()


#or just mul by 2
n = int(input())
for i in range(n):
      print(i*2,end=" ")
print()

#first n odd numbers
n = int(input())
for i in range(n):
      print(i*2+1,end=" ")
print()'''

#print one even number and one odd number
'''n = int(input())
val = 1
for i in range(n):
      if i%2==0:
            print(val*2,end=" ")
            val+=1
      else:
            print(i,end=" ")

#or
n = int(input())
for i in range(n):
      if i%2==0:print(i+2,end=" ")
      else:print(i,end=" ")
print()'''


#add odd numbers to previous num eg: 2,5,10,17,26
n = int(input())
for i in range(1,n+1):
      print(i**(2)+1,end=" ")
print()


#eg: 0,7,26,63,124
n = int(input())
for i in range(1,n+1):
      print((i**3)-1,end=" ")
print()


#0,1,1,2,3,5,8,13,21,34,55,89,144
n = int(input())
a,b = 0,1
for i in range(n):
      print(a,end=" ")
      a,b = b,a+b