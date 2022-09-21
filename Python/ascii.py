#ordinal value - will return ascii values
#keyword - ord - give only character not string
print(ord("A"))
print(ord("Z"))


#find ip is a value or char
n = input() #if i gave as int then int value is larger so we get typeerror
if ord(n)>= ord("A") and ord(n)<=ord("Z"):
      print("you enterd an Capital letter")
elif ord(n)>= ord("a") and ord(n)<=ord("z"):
      print("you enterd an Smaller letter")  
else:
      print("you enterd an Digit or special character")

#we can use it to type alphabets like eg: if we wanted to type all the alphabets

#chr 