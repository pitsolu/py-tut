from src.oop.student import Student
from src.oop.teacher import Teacher

persons = (Student("John", "Doe"), Teacher("Jane", "Doel"))

class TestPerson:
	def test_output(self):
		for x in persons:
			if(isinstance(x, Student)):
				assert x.getName() == "John Doe"
				assert x.getRole() == "study"
			elif(isinstance(x, Teacher)):
				assert x.getName() == "Jane Doel"
				assert x.getRole() == "lecture"