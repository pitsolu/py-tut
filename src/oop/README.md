OOP - Object Oriented Programming
===

### Classes/Objects

Run in `python` console.

```python
class Student:
	def getRole():
  		return "study"

class Teacher:
	def getRole():
  		return "lecture"
```
### Inheritance

Run in `python` console.

```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def getName(self):
    return self.firstname + " " + self.lastname

class Student(Person): #Inheritance happens here
	def getRole():
  		return "study"

class Teacher(Person): #Inheritance happens here also
	def getRole():
  		return "lecture"
```
### Polymorphism

Run in `python` console.

```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def getName(self):
    return self.firstname + " " + self.lastname

  def getRole(self): #Polymorphism happens here
    return "study"

class Student(Person):
  pass

class Teacher(Person):
    def getRole(self): #Override base function getRole
      return "lecture"
```
### Modules

Create a directory called `src/oop`

```sh
mkdir -p src/oop
cd src/oop
```

Firstly, create file `person.py`. File `person.py` is a module.

```python
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def getName(self):
    return self.firstname + " " + self.lastname

  def getRole(self): #Polymorphism happens here
    return "study"
```

Secondly, create file `student.py`. File `student.py` is also a module.

```python
from src.oop.person import Person # Import class Person from module person

class Student(Person):
  pass
```

Thirdly, create file `teacher.py`. File `teacher.py` is a module.

```python
from src.oop.person import Person # Import class Person from module person

class Teacher(Person):
  def getRole(self): #Override base function getRole
    return "lecture"
```

Finally run in `python` console where the modules were created (base directory).

```sh
cd ../../ # Go back to base directory i.e above ./src
```

The above modules code is already in `./src/oop/` (base directory) path of `py-tut`

```python
from src.oop.student import Student # Import class Student from module student
from src.oop.teacher import Teacher # Import class Teacher from module teacher

for x in (Student("John", "Doe"), Teacher("Jane", "Doel")):
	print(x.getName())
	print(x.getRole())
```
