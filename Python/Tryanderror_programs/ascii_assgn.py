alpha = input()
if (ord(alpha)>=65 and ord(alpha)<=90) or (ord(alpha)>=97 and ord(alpha)<=122):
      if alpha in "aeiouAEIOU":
            print("vowel")
      else:
            print("conconent")
else:
      print("special character or numbers")


#if input is string and want to restrict to 1 digit then can use index
alpha = input()[0]
if (ord(alpha)>=65 and ord(alpha)<=90) or (ord(alpha)>=97 and ord(alpha)<=122):
      if alpha in "aeiouAEIOU":
            print("vowel")
      else:
            print("conconent")
else:
      print("special character or numbers")