'''t1=(1,2,3,4,5,6,7,8,2,5,6,1)
print(t1.index(2,1))'''



'''row = int(input("row: "))
column = int(input("column: "))
val = 1
for i in range(1,row+1):
      for j in range(1,column+1):
            print(val,end=" ")
      print()
      val +=1
      if val>9:
            val = 1'''




'''row = int(input("row: "))
column = int(input("column: "))
for i in range(1,row+1):
      val = 1
      for j in range(1,column+1):
            print(val,end=" ")
            val +=1
            if val>9:
                  val = 1
      print()'''



'''row = int(input("row: "))
for i in range(1,row+1):
      for j in range(1,i):
            print(j,end=" ")
      print()'''



for i in range(5,0,-1):
      for j in range(5,i,-1):
            print("1",end=" ")
      print()

#another try
pattern = 4
for i in range(1,6):
      for k in range(1,pattern+1):
            print(end=" ")
      pattern -=1
      for j in range(i,0,-1):
            print(j,end="")
      print()


#v pattern
'''
1        1
12      21
123    321
1234  4321
1234554321'''
#ch = input()
pattern = 8
for i in range(1,6):
      for j in range(1,i+1):
            print(j,end="")
      for k in range(1,pattern+1):
            print(end=" ")
      pattern -=2
      for j in range(i,0,-1):
            print(j,end="")
      print()