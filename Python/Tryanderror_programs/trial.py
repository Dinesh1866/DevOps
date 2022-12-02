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



'''
*
* *
* * *
* *
*
'''
'''n =int(input())
l1=[]
for i in range(1,((n+1)//2)+1):
  l1.append("* "*i)
print("\n".join(l1+l1[-2::-1]))


#or 
n =int(input())
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

#with one for loop
n =int(input())
for i in range(n):
  if i<=n//2:
    print("* "*(i+1))
  else:
    print("* "*(n-i))'''

#1
'''n =int(input())
val = ord("A")
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(chr(val),end=" ")
      val+=1
    else:
      print(" ",end=" ")
  print()


#2
n =int(input())
for i in range(n):
  val = ord("A")
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(chr(val),end=" ")
      val+=1
    else:
      print(" ",end=" ")
  print()

#3
n =int(input())
val=ord("A")+n-1
for i in range(n):
  a = val
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(chr(val),end=" ")
      val-=1
    else:
      print(" ",end=" ")
  val =a-1
  print()

#4
n=int(input())
a=1
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(a,end=" ")
      a+=1
  print()

#5
n=int(input())
val=ord("A") 
for i in range(n):
  a = val
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(chr(val),end=" ")
    else:
      print(" ",end=" ")
  val +=1
  print()'''



#diff pattern
n =int(input())
val = 1
for i in range(2*n-1):
  a = val
  for j in range(n):
    if i>=j and i+j<=2*n-2:
      print(val,end=" ")
      val-=1
  if i<n-1:
    val = a+1
  else:
    val = a-1
  print()

n=int(input())
a=1
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(f"0{a}",end=" ")
      a+=1
  print()

#SPIDERMAN
n=int(input())
S = "SPIDERMAN"
a = 0
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1:
      print(S[a],end=" ")
      a+=1
  print()

n = int(input())
a = 0
num = 1
val = ord("A")
for i in range(n):
  for j in range(n):
    if i>=j and i+j<=n-1 and a%2==0:
      print(chr(val),end=" ")
      val+=1
    elif i>=j and i+j<=n-1 and a%2!=0:
      print(num,end=" ")
      num+=1
    else:
      print(" ",end=" ")
    a +=1
  print()

#mistakes
'''n=int(input())
val = ord("A")
for i in range(n):
  a = val
  for j in range(n):
    if i>=j and i+j<=n-1 and i<=n//2:
      print(chr(val),end=" ")
      val-=1
    elif i>=j and i+j<=n-1 and i>n//2:
      print(chr(val),end=" ")
      val+=1
  print()
  val = a+1'''


#1
'''
A
B C
C B A
B A
A'''



#west pryamid
n =int(input())
l1=[]
for i in range(1,n+1):
  l1.append("  "*(n-i)+"* "*i)
print("\n".join(l1+l1[-2::-1]))


#or try with for loop
'''n =int(input())
for i in range(2*n-1):
  for j in range(n):
    if j>=n-i and:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()'''

