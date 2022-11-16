from citizen import citizen,student,employee
from government import government_services

c1=citizen("Dinesh",22,"M")
s1=student("Sanjay",17,"M",1234,80,"A")
e1=employee("Subramanian",52,"M",1247,45000,"Agent")
e2=employee("Radha",47,"F",1248,55000,"Agent")

g1=government_services()
g1.aadhaar(c1)
g1.scholarship(s1)
g1.taxpay(e1)
g1.taxpay(e2)