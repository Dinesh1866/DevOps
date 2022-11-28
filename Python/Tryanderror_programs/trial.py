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

'''
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


'''def f1(n):
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
        print(("  "*i)+("* "(n-i)),end=" ")'''


'''#lets first initialize the size of the matrix
n,m = map(int,input().split())
mat1 = []
for i in range(n):
      mat1.append(list(map(int,input().split())))

mat2 = []
for i in range(n):
      mat2.append(list(map(int,input().split())))

mat3 = []
for i in range(n):
      mat3.append([0]*m)

print("Matrix after Addition: ")
#Adddition
for i in range(n):
      for j in range(m):
            mat3[i][j]=mat1[i][j]+mat2[i][j]

#note even for printing our matrix we want loop
for i in range(n):
      for j in range(m):
            print(mat3[i][j], end=" ")
      print()

print("Matrix after Multiplication: ")
#Multiplication
mat4 = []
for i in range(n):
      mat4.append([0]*m)

for i in range(n):
      for j in range(m):
            for k in range(n):
                  mat4[i][j]=mat4[i][j]+(mat1[i][k]*mat2[k][j])
for i in range(n):
      for j in range(m):
            print(mat4[i][j], end=" ")
      print()'''



#for input 5 print the following pattern'''
'''
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1'''

n=int(input())
for i in range(n):
  val =1
  for j in range(n):
    if i+j>=n-1:
      print(val,end=" ")
      if j<n-1:
        val+=1
      else:
        val-=1
    else:print(" ",end=" ")
  for j in range(i):
    print(val,end=" ")
    val-=1
  print()


'''
        A
      B C D
    E F G H I
  J K L M N O P
Q R S T U V W X Y'''
val=ord("A")
for i in range(n):
  for j in range(n):
    if i+j>=n-1:
      print(chr(val),end=" ")
      val+=1
    else:print(" ",end=" ")
    if val>ord("Z"):
      val =ord("A")
  for j in range(i):
    print(chr(val),end=" ")
    val+=1
    if val>ord("Z"):
      val =ord("A")
  print()


'''
        A
      B A B
    C B A B C
  D C B A B C D
E D C B A B C D E
'''
n=int(input())
val=ord("A")
for i in range(n):
  a= val
  for j in range(n):
    if i+j>=n-1:
      print(chr(val),end=" ")
      if j<n-1:
        val-=1
    else:print(" ",end=" ")
    if val<ord("A"):
      val =ord("Z")
  for j in range(i):
    val+=1
    print(chr(val),end=" ")
    if val>ord("Z"):
      val =ord("A")
  print()
  val =a+1


'''for n=5
print the following pattern
    *    
  * * *  
* * * * *'''
n=int(input())
for i in range(n):
  for j in range(i+1):
    if i+j>=n-1:
      print("*",end=" ")
    else:print(" ",end=" ")
  print()


'''
* * * * *
  * * *
    *'''
n = int(input())
for i in range(n):
  for j in range(n-i):
    if j>=i:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()


'''
A B C D E
  F G H 
    I'''
n = int(input())
val = ord("A")
for i in range(n):
  for j in range(n-i):
    if j>=i:
      print(chr(val),end=" ")
      val+=1
    else:
      print(" ",end=" ")
  print()