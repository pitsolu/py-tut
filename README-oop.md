Example 1
===

### Classes/Objects
```python
class Student:
	def getRole():
  		print("study")

class Teacher:
	def getRole():
  		print("lecture")
```
### Inheritance
```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def getName(self):
    print(self.firstname, self.lastname)

class Student(Person): #Inheritance happens here
	def getRole():
  		print("study")

class Teacher(Person): #Inheritance happens here also
	def getRole():
  		print("lecture")
```
### Polymorphism

```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def getName(self):
    print(self.firstname, self.lastname)

  def getRole(self): #Polymorphism happens here
    print(self.role)

class Student(Person):
  role = "study"
  pass

class Teacher(Person):
  role = "lecture"
  pass
```
### Modules

Firstly, create file `person.py`. File `person.py` is a module.

```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  # def printname(self):
    # print(self.firstname, self.lastname)

  def getName(self):
    print(self.firstname, self.lastname)

  def getRole(self):
    print(self.role)
```

Secondly, create file `student.py`. File `student.py` is also a module.

```python
from person import Person # Import class Person from module person

class Student(Person):
  role = "study"
  pass
```

Thirdly, create file `teacher.py`. File `teacher.py` is a module.

```python
from person import Person # Import class Person from module person

class Teacher(Person):
  role = "lecture"
  pass
```

Finally, create our execution base `test.py`.

```python
from student import Student # Import class Student from module student
from teacher import Teacher # Import class Teacher from module teacher

for x in (Student("John", "Doe"), Teacher("Jane", "Doel")):
	x.getName()
	x.getRole()
```

Run the above code in your terminal.

```sh
python test.py
```
