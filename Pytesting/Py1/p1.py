#finding the given number is prime or not
class prime:
      def isprime(n):
            if n==1:
                  return False
            for i in range(2,n):
                  if n%i==0:
                        return False
            return True

      def printprime(n):
            count=0
            sum=0
            i=1
            while count<n:
                  if prime(i):
                        print(i)
                        count+=1
                        sum+=i
                        print("sum=",sum)
                  i+=1
            return sum/count
prime.printprime(10)