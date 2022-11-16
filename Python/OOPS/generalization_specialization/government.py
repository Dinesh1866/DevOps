from citizen import student,employee

class government_services:
      def aadhaar(self,citizen):
            print("aadhar verification for", citizen.name ,"is successful")

      def scholarship(self,student):
            if isinstance(student,student):
                  if student.mark >=70:
                        print("you got a scholarship!")
                  else:
                        print("sorry you haven't got any scholarship :(")
            else:
                  print("seems youre not a student")

      def taxpay(self,employee):
            if isinstance(employee,employee):
                  if employee.sal >50000:
                        tax = employee.sal * 0.3
                        print("your amount to pay is",tax)
                  else:
                        print("no tax enjoy your sal")
            else:
                  print("you're not a employee it seems")
