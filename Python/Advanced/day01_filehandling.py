# to count the number of words in a file
f1 = open("E:\\f1.txt","r")
words = f1.readlines()
count = 0
for i in words:
  count+=len(i.split())
print(count)


#could simplified
f1 = open("E:\\f1.txt","r")
words = f1.read().split()
print(len(words))