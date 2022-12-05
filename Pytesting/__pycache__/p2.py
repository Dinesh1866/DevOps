# function takes in a list of numbers and returns the sum of the numbers

class sum:
    def sumofnumbers(list):
        sum=0
        for i in list:
            sum+=i
        print("avg",sum//len(list))
        return sum//len(list)

n = int(input("Enter the number of elements : "))
list = []
for i in range(0, n):
    ele = int(input())
    list.append(ele)
#list = map(int,input("\nEnter the numbers : ").split())


sum.sumofnumbers(list)