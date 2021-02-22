class student:
	raise_amt=1.04
	def __init__(self,name,age,grade):
		self.name=name
		self.age=age
		self.grade=grade
	def get_grade(self):
		return self.grade
class trader(student):
	def __init__(self,name,corpus,risk):
		self.corpus=corpus
		self.risk=risk
	def place_traders(self):
		print("placing traders risking "+str(self.risk))
traderx=trader("jesso",100000,1000)
traderx.place_traders()
class course:
	def __init__(self,name,max_student):
		self.name=name
		self.max_student=max_student
		self.students=[]
	def add_student(self,student):
		self.students.append(student)
	def average_grade(self):
		value=0
		for i in self.students:
			value=value+i.get_grade()
		return value/len(self.students)
s1=student("jesso",23,56)
s2=student("john",24,78)
s3=student("joy",67,99)
# print(s1.get_grade())
# print(s2.get_grade())
c1=course("physics",2)
c1.add_student(s1)
c1.add_student(s2)
print(c1.students[1].grade)
print(c1.average_grade())
