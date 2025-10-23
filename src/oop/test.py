from student import Student
from teacher import Teacher

# s = Student("John", "Doe")
# s.getName()
# s.getRole()

# t = Teacher("Jane", "Doel")
# t.getName()
# t.getRole()

for x in (Student("John", "Doe"), Teacher("Jane", "Doel")):
	x.getName()
	x.getRole()
