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