class citizen:
      def __init__(self,name,age,gender):
            self.name=name
            self.age=age
            self.gender=gender

class student(citizen):
      def __init__(self, name, age, gender, sid, marks, grade):
            super().__init__(name=name, age=age, gender=gender)
            self.sid = sid
            self.marks = marks
            self.grade = grade

class employee(citizen):
      def __init__(self, name, age, gender,eid,sal,desig):
            super().__init__(name=name, age=age, gender=gender)
            self.eid=eid
            self.sal=sal
            self.desig=desig