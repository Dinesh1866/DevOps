#print based * on the rows based on given input
'''eg: n =3 ->o/p:
*
*
*'''
n = int(input())
for i in range(n):
      print("*")


# now in coloumns with space
'''eg:n=3
o/p: * * *'''
for i in range(n):
      print("*", end=" ") 


#both coloumns and rows
'''eg: n=3
o/p:
* * *
* * *
* * *'''
for i in range(n):
      for i in range(n):
            print("*",end=" ")
      print()

#or 
for i in range(n):
      print("* "*n)


#if we want to print the letters from string then
s1 = "Dinesh"
for i in range(n):
      print(f"{s1[i]} "*n)


#if we want each letter in each column means
'''eg:THOR
o/p:
T H O R
T H O R
T H O R'''
s2 = "THOR"
for i in range(n):
      for i in s2:
            print(i,end=" ")
      print()


#print alphabets
'''eg:n=3
A B C
D E F
G H I'''
n = int(input())
val =ord("A")
for i in range(n):
      for i in range(n):
            print(chr(val),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()


#print repeated alphabets and change alphabets for every row
'''eg: n=3
A A A
B B B
C C C'''
n = int(input())
val =ord("A")
for i in range(n):
      for i in range(n):
            print(chr(val),end=" ")
      val +=1
      if val > ord("Z"):
                  val = ord("A")
      print()


#change values for every column and print same o/p for every row
'''eg: n=4
o/p:
A B C D
A B C D
A B C D
A B C D'''
n = int(input())
for i in range(n):
      val =ord("A")
      for i in range(n):
            print(chr(val),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()


#if a value is 5 the letters should start from E and go on
'''eg: n=3 -> 3 rows and 3 columns
o/p:
C D E
F G H
I J K

eg:n=100 -> 100 rows and 100 columns
o/p: V W X Y Z ....'''
n = int(input())
res = n
while res>=26:
      res-=26
val =ord("A")+ (res-1)
for i in range(n):
      for i in range(n):
            print(chr(val),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()

#or
n = int(input())
val =ord("A")+ (n-1)
while val>=ord("Z"):
      val-=26
for i in range(n):
      for i in range(n):
            print(chr(val),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()


#print * for odd and @ for even values of j/ column
'''eg: n=4
o/p:
@ * @ *
@ * @ *
@ * @ *
@ * @ *
'''
n = int(input())
symbol =["*","@"]
for i in range(n):
      for j in range(n):
            print(symbol[j%2],end=" ")
      print()

#or
n = int(input())
for i in range(n):
      for j in range(n):
            print("*" if j%2==0 else "@",end=" ")
      print()


#for every rows now
'''
n = 4
@ @ @ @
* * * *
@ @ @ @
* * * *'''
n = int(input())
for i in range(n):
      for j in range(n):
            print("*" if i%2==0 else "@",end=" ")
      print()


#mix of caps and small letters
'''eg: n=4
A b C d
E f G h
I j K l
M n O P'''
n = int(input())
val = ord("A")
for i in range(n):
      for j in range(n):
            if val%2==0:
                  newval=val+ 32
                  print(chr(newval),end=" ")
            else:
                  print(chr(val),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()

#or
n = int(input())
val = ord("A")
for i in range(n):
      for j in range(n):
            print(chr(val) if j%2==0 else chr(val+32),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()


#print * and @ wise versa
'''eg: n=3
* @ *
@ * @
* @ * '''
n = int(input())
l1 = ["*","@"]
val =0
for i in range(1,n+1):
      for j in range(1,n+1):
            print(l1[val],end=" ")
            val+=1
            if val>1:
                  val=0
      print()

#or
n = int(input())
White=True
for i in range(1,n+1):
      for j in range(1,n+1):
            print("*"if White==True else "@", end=" ")
            White = not White
      print()


#print values for every columns
'''eg: n=4
1 2 3 4
5 6 7 8
9 1 2 3
3 4 5 6`'''
n = int(input())
val =1
for i in range(n):
      for j in range(n):
            print(val, end=" ")
            val+=1
            if val >9:
                  val =1
      print()


#print values -> 1 to 99 as 01 to 09 everything 2 digits
'''eg:n =4
01 02 03 04
05 06 07 08
09 10 11 12
13 14 15 16'''
n = int(input())
val =1
for i in range(n):
      for j in range(n):
            print(f"0{val}" if val<10 else val , end=" ")
            val +=1
            if val >99:
                  val =1
      print()


#Print the following pattern
'''
* * * * *
* C B A *
* D C B *
* E D C *
* * * * *'''
n=int(input())
val = ord("A")+n//2-1
for i in range(n):
      a = val
      for j in range(n):
            if j==0 or j==n-1 or i==0 or i==n-1:
                  print("*", end=" ")
            else:
                  print(chr(val),end=" ")#here in first loop val is 66 but during 2nd its increased to 67 so now val start printing from C
                  val -=1
                  if val< ord("A"):
                        val = ord("Z")
      print()
      val=a+1
      if val>ord("Z"):
            val= ord("A")



#by using functions fun(n)
'''
A B C D E
B       F
C       G
D       H
E F G H I'''
def fun1(n):
      val = ord("A")
      for i in range(n):
            a = val
            for j in range(n):
                  if j==0 or j==n-1 or i==0 or i==n-1:
                        print(chr(val), end=" ")
                  else:
                        print(" ",end=" ")
                  val+=1
                  if val> ord("z"):
                        val = ord("A")
            print()
            val=a+1

n = int(input())
fun1(n)



#reverse of above
'''
E D C B A
F       B
G       C
H       D
I H G F E'''
#by using functions fun(n)
def fun1(n):
      val = ord("A")+n-1
      for i in range(n):
            a = val
            for j in range(n):
                  if j==0 or j==n-1 or i==0 or i==n-1:
                        print(chr(val), end=" ")
                  else:
                        print(" ",end=" ")
                  val-=1
                  if val< ord("A"):
                        val = ord("Z")
            print()
            val=a+1
            if val>ord("Z"):
                  val= ord("A")

n = int(input())
fun1(n)


'''
* * * * * 
*   a   *
* b c d *
*   e   *
* * * * *'''
n = int(input())
val =ord("a")
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    elif i==n//2 or j==n//2:
      print(chr(val),end=" ")
      val+=1
    else:
      print(" ",end=" ")
  print()


'''
* * a * * 
*   b   *
c d e f g
*   h   *
* * i * *
'''
n = int(input())
val =ord("A")
a = ord("a")
for i in range(n):
  for j in range(n):
    if j==n//2:
      print(chr(val),end=" ")
      val+=1
    elif i==n//2:
      print(chr(a),end=" ")
      a+=1
    elif i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()


'''
* * A * * 
*   B   *
a b C d e
*   D   *
* * E * *'''
#but this will work till 26 coz a-z is 26
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


#or
n = int(input())
val =ord("A")
a = ord("a")
for i in range(n):
  for j in range(n):
    if j==n//2:
      if i==j:
        a+=1
      print(chr(val),end=" ")
      val+=1
    elif i==n//2:
      print(chr(a),end=" ")
      a+=1
    elif i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()


#instead small if every letter is caps then
n = int(input())
val =ord("A")
a = ord("A")
for i in range(n):
  for j in range(n):
    if j==n//2:
      if i==j:
        a+=1
      print(chr(val),end=" ")
      val+=1
    elif i==n//2:
      print(chr(a),end=" ")
      a+=1
    elif i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()



'''
* * * * *
* *     *
*   *   *
*     * *
* * * * *'''
n = int(input())
val =ord("A")
a = ord("A")
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1 or i==j:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()


'''
* * * * *
*     * *
*   *   *
* *     *
* * * * *'''
n = int(input())
val =n-1
for i in range(n):
  for j in range(n):
    if j==val:
      print("*",end=" ")
      val-=1
    elif i==0 or i==n-1 or j==0 or j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()

#or
n = int(input())
val =ord("A")
a = ord("A")
for i in range(n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1 or i+j==n-1:
      print("*", end=" ")
    else:
      print(" ",end=" ")
  print()


'''
*
* *
* * *
* * * *
* * * * *'''
n = int(input())
for i in range(n):
  for j in range(i+1):
    print("*",end=" ")
  print()

# or
n = int(input())
for i in range(1,n+1):
  print("* "*i)

#or
n = int(input())
for i in range(n):
  for j in range(n):
      if i>=j:
            print("*",end=" ")
  print()


#instead start print characters
n = int(input())
val = ord("A")
for i in range(n):
  for j in range(i+1):
    print(chr(val),end=" ")
  val+=1
  print()

# or
val = ord("A")
for i in range(1,n+1):
  print(f"{chr(val)} "*i)
  val +=1


'''
A
B A
C B A
D C B A
E D C B A'''
n = int(input())
val = ord("A")
for i in range(n):
  a=val
  for j in range(i+1):
    print(chr(val),end=" ")
    val-=1
  val=a+1
  print()


