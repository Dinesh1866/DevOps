#print based * on the rows based on given input
n = int(input())
for i in range(n):
      print("*")


# now in coloumns with space
for i in range(n):
      print("*", end=" ") 


#both coloumns and rows
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
s2 = "THOR"
for i in range(n):
      for i in s2:
            print(i,end=" ")
      print()


#print alphabets
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
n = int(input())
for i in range(n):
      val =ord("A")
      for i in range(n):
            print(chr(val),end=" ")
            val +=1
            if val > ord("Z"):
                  val = ord("A")
      print()


#
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


#print * for odd and @ for even values
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
n = int(input())
for i in range(n):
      for j in range(n):
            print("*" if i%2==0 else "@",end=" ")
      print()


#mix of caps and small letters
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
n = int(input())
val =1
for i in range(n):
      for j in range(n):
            print(val, end=" ")
            val+=1
            if val >9:
                  val =1
      print()