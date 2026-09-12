# # # # # # # # d=["aju","amu","sumu","fa","no","ye","ee"]
# # # # # # # # for i in d:
# # # # # # # #     print(i)

# # # # # # # # d=["aju","amu","sumu","fa","no","ye","ee"]

# # # # # # # # for i in d:
# # # # # # # #     print(i)

# # # # # # # # d=["aju","amu","sumu","fa","no","ye","ee"]
# # # # # # # # d.sort()
# # # # # # # # print(d)

# # # # # # # # numbers = []

# # # # # # # # for i in range(1, 6):
# # # # # # # #     numbers.append(i)

# # # # # # # # print(numbers)

# # # # # # # # d=[]

# # # # # # # # for i in range(1,9):
# # # # # # # #     d.append(i)
# # # # # # # # print(d)

# # # # # # # # numbers=[i for i in range(1,6)if i % 2 == 0]
# # # # # # # # print(numbers)

# # # # # # # # even=[i for i in range(1,10)if i%2==0]
# # # # # # # # print(even)

# # # # # # # # marks=[12,21,34,54,54,32]
# # # # # # # # total=0

# # # # # # # # for i in marks:
# # # # # # # #     total=total+i

# # # # # # # # avarage=total/len(marks)

# # # # # # # # print("total mark:",total)
# # # # # # # # print("total avarage:",avarage)

# # # # # # # # student = ("Ajmal", 20, 85)

# # # # # # # # name, age, mark = student

# # # # # # # # print(name)
# # # # # # # # print(age)
# # # # # # # # print(mark)


# # # # # # # # number=[1,2,3,4,5,67,7,8,9]
# # # # # # # # *first,middle,last=number

# # # # # # # # print(first)
# # # # # # # # print(middle)
# # # # # # # # print(last)

# # # # # # # # number=(10,)
# # # # # # # # print(type(number))


# # # # # # # # student = ("Ajmal", 20, "Python", 85)

# # # # # # # # name, age, course, mark = student

# # # # # # # # print("Student Name:", name)
# # # # # # # # print("Age:", age)
# # # # # # # # print("Course:", course)
# # # # # # # # print("Mark:", mark)

# # # # # # # # number={1,2,3,12,3,12,2,3}
# # # # # # # # print(number)

# # # # # # # # x=set()

# # # # # # # # fruits={12,2,21,221,21,12}
# # # # # # # # fruits.update([1111,1111111])
# # # # # # # # print(fruits)

# # # # # # # # lam={"ajmal","hassan","bro","ashmal"}
# # # # # # # # lam.update(["nooble","jamaal"])
# # # # # # # # print(lam)

# # # # # # # # A={1,2,3,4,5,6,7}
# # # # # # # # B={4,5,6,7,8,9,10}

# # # # # # # # print("union:",A|B)
# # # # # # # # print("inersection:",A&B)
# # # # # # # # print(" A diffrence B:",A-B)
# # # # # # # # print("B diffrence A:",B-A)


# # # # # # # # python_students = {"Ajmal", "Rahul", "Akhil", "Arun"}
# # # # # # # # java_students = {"Rahul", "Arun", "Vishnu", "Manu"}

# # # # # # # # print("All Students:")
# # # # # # # # print(python_students | java_students)

# # # # # # # # print("Students studying both:")
# # # # # # # # print(python_students & java_students)

# # # # # # # # print("Only Python:")
# # # # # # # # print(python_students - java_students)

# # # # # # # # print("Only Java:")
# # # # # # # # print(java_students - python_students)


# # # # # # # # student = {
# # # # # # # #     "name": "Ajmal",
# # # # # # # #     "age": 20,
# # # # # # # #     "mark": 85
# # # # # # # # }

# # # # # # # # student.update({
# # # # # # # #     "age":21,
# # # # # # # #     "mark":90,
# # # # # # # #     "number":233322223
# # # # # # # # })
# # # # # # # # print(student)

# # # # # # # # student = {
# # # # # # # #     "name": "Ajmal",
# # # # # # # #     "age": 20,
# # # # # # # #     "mark": 85
# # # # # # # # }

# # # # # # # # print(student.item())

# # # # # # # # student = {
# # # # # # # #     "name": "Ajmal",
# # # # # # # #     "age": 20
# # # # # # # # }

# # # # # # # # if "name" in student:
# # # # # # # #     print("name is available")

# # # # # # # # student={
# # # # # # # #     "name":"ajmal",
# # # # # # # #     "age":211
# # # # # # # # }
# # # # # # # # # if "name" in student:
# # # # # # # # #     print("name is available")
# # # # # # # # print(len(student))

# # # # # # # # even_squares = {
# # # # # # # #     i: i * i
# # # # # # # #     for i in range(1, 11)
# # # # # # # #     if i % 2 == 0
# # # # # # # # }

# # # # # # # # print(even_squares)

# # # # # # # # squres={
# # # # # # # #     i:i*i
# # # # # # # #     for i in range(1,20)
# # # # # # # #     if i%2==0
# # # # # # # # }
# # # # # # # # print(squres)

# # # # # # # # students = {
# # # # # # # #     "ajmal":85,
# # # # # # # #     "rahul":21,
# # # # # # # #     "aju":23
# # # # # # # # }
# # # # # # # # highest = max(students.values())
# # # # # # # # print("highest:", highest)

# # # # # # # # ajmal={
# # # # # # # #     "ajmal":81,
# # # # # # # #     "ashmal":211
# # # # # # # # }
# # # # # # # # highest=max(ajmal.values())
# # # # # # # # print("highest:",highest)

# # # # # # # # students = {
# # # # # # # #     "Ajmal": 85,
# # # # # # # #     "Rahul": 92,
# # # # # # # #     "Akhil": 78,
# # # # # # # #     "Arun": 88
# # # # # # # # }

# # # # # # # # total = 0

# # # # # # # # for name, mark in students.items():
# # # # # # # #     print(name, ":", mark)
# # # # # # # #     total += mark

# # # # # # # # average = total / len(students)

# # # # # # # # print("Total:", total)
# # # # # # # # print("Average:", round(average, 2))
# # # # # # # # print("Highest:", max(students.values()))
# # # # # # # # print("Lowest:", min(students.values()))

# # # # # # # # name1="ajmal"
# # # # # # # # name2="mp"

# # # # # # # # fullname=name1+" "+ name2
# # # # # # # # print(fullname)

# # # # # # # # name1="ajmal"
# # # # # # # # print(name1.upper())

# # # # # # # # def greet(name):
# # # # # # # #     print("hallo",name)

# # # # # # # # greet("ajmal")

# # # # # # # # def add(a,b):
    
# # # # # # # # def student(name, age):
# # # # # # # #     print("Name:", name)
# # # # # # # #     print("Age:", age)

# # # # # # # # student(age=20, name="Ajmal")

# # # # # # # # def add(a, b):
# # # # # # # #     return a + b


# # # # # # # # result=add(12,21)
# # # # # # # # print(result)

# # # # # # # # age = int(input("Enter your age: "))
# # # # # # # # print(age)

# # # # # # # # try:
# # # # # # # #     age = int(input("Enter your age: "))
# # # # # # # #     print("Your age is:", age)

# # # # # # # # except:
# # # # # # # #     print("Please enter a valid number.")

# # # # # # # # try:
# # # # # # # #     number = int(input("Enter number: "))

# # # # # # # # except ValueError:
# # # # # # # #     print("Invalid input.")

# # # # # # # # else:
# # # # # # # #     print("You entered:", number)

# # # # # # # # finally:
# # # # # # # #     print("Program finished.")

# # # # # # # # balance = 5000

# # # # # # # # try:
# # # # # # # #     amount = int(input("Enter withdrawal amount: "))

# # # # # # # #     if amount > balance:
# # # # # # # #         print("Insufficient balance")
# # # # # # # #     else:
# # # # # # # #         balance -= amount
# # # # # # # #         print("Withdrawal successful")
# # # # # # # #         print("Remaining balance:", balance)

# # # # # # # # except ValueError:
# # # # # # # #     print("Please enter a valid amount.")

# # # # # # # # finally:
# # # # # # # #     print("Thank you for using the ATM.")

# # # # # # # # class Student:

# # # # # # # #     def __init__(self, name, age):
# # # # # # # #         self.name = name
# # # # # # # #         self.age = age
# # # # # # # # student1 = Student("Ajmal", 21)

# # # # # # # # print(Student)


# # # # # # # # class Model:
# # # # # # # #     framework = "Python"

# # # # # # # #     def __init__(self, name):
# # # # # # # #         self.name = name

# # # # # # # #     def show_model(self):
# # # # # # # #         print("Model:", self.name)


# # # # # # # # class MLModel(Model):
# # # # # # # #     def __init__(self, name, accuracy):
# # # # # # # #         super().__init__(name)
# # # # # # # #         self.accuracy = accuracy

# # # # # # # #     def show_accuracy(self):
# # # # # # # #         print("Accuracy:", self.accuracy)

# # # # # # # #     @classmethod
# # # # # # # #     def show_framework(cls):
# # # # # # # #         print("Framework:", cls.framework)

# # # # # # # #     @staticmethod
# # # # # # # #     def is_good_accuracy(accuracy):
# # # # # # # #         return accuracy >= 80

# # # # # # # # def ajmal(x):
# # # # # # # #     return x*x
# # # # # # # # print(ajmal(5))

# # # # # # # # def best(x):
# # # # # # # #     return x+x
# # # # # # # # print(best(10))

# # # # # # # # ajmal=lambda x:x*x
# # # # # # # # print(ajmal(10))

# # # # # # # # squre=lambda x:x+2
# # # # # # # # print(squre(10))

# # # # # # # # add=lambda a,b:a+b
# # # # # # # # print(add(10,21))

# # # # # # # # numbers=[2,3,4,5,6]
# # # # # # # # result=[]

# # # # # # # # for number in numbers:
# # # # # # # #     result.append(number*2)

# # # # # # # # print(result)

# # # # # # # # number=[12,12,23,34,54]
# # # # # # # # result=[]
# # # # # # # # for i in number:
# # # # # # # # #     result.append(i*3)
# # # # # # # # # print(result)

# # # # # # # # numbers=[2,4,5,6,7,8]

# # # # # # # # result=map(lambda x:x*3,numbers)

# # # # # # # # print(list(result))

# # # # # # # # numbers=[2,3,4,5,6,7,8,9,10]
# # # # # # # # result=map(lambda y:y+3,numbers)
# # # # # # # # print(list(result))

# # # # # # # number=[12,21,23,22,24,3,2,22,334]
# # # # # # # result=filter(lambda x:x>20,number)
# # # # # # # print(list(result))

# # # # # # # number=[1,2,3,4,5,6,7,8,9]
# # # # # # # result=filter(lambda age:age>2,number)
# # # # # # # print(list(result))

# # # # # # # number=["ajmal","rahul","aju"]
# # # # # # # mark=[1,2,3]
# # # # # # # result=zip(number,mark)
# # # # # # # print(list(result))

# # # # # # my_ajmal=iter(number)

# # # # # # def fruits():
# # # # # #     yield"apple"
# # # # # #     yield"banana"
# # # # # #     yield"orange"
# # # # # #     yield"onion"

# # # # # # for fruit in fruits():
# # # # # #     print(fruit)

# # # # # # def count():
# # # # # #     for i in range(1,10):
# # # # # #         yield i

# # # # # # for number in count():
# # # # # #     print(number)

# # # # # # def numbers():
# # # # # #     yield 10
# # # # # #     yield 20
# # # # # #     yield 30

# # # # # # for i in numbers():
# # # # # #     print(i)

# # # # # # with open("students.txt", "w") as file:
# # # # # #     file.write("Ajmal")

# # # # # # marks = [80, 90, 70]

# # # # # # total = sum(marks)
# # # # # # average = total / len(marks)

# # # # # # with open("result.txt", "w") as file:
# # # # # #     file.write("Marks: " + str(marks) + "\n")
# # # # # #     file.write("Total: " + str(total) + "\n")
# # # # # #     file.write("Average: " + str(average))

# # # # # # marks = [80, 90, 70]

# # # # # # total = sum(marks)
# # # # # # average = total / len(marks)

# # # # # # print("Marks:", marks)
# # # # # # print("Total:", total)
# # # # # # print("Average:", average)

# # # # # # with open("result.txt", "w") as file:
# # # # # #     file.write("Marks: " + str(marks) + "\n")
# # # # # #     file.write("Total: " + str(total) + "\n")
# # # # #     file.write("Average: " + str(average))

# # # # # marks = [80, 90, 70, 85]

# # # # # total = sum(marks)
# # # # # highest = max(marks)
# # # # # lowest = min(marks)
# # # # # average = total / len(marks)

# # # # # with open("result.txt", "w") as file:
# # # # #     file.write(f"Marks: {marks}\n")
# # # # #     file.write(f"Total: {total}\n")
# # # # #     file.write(f"Highest: {highest}\n")
# # # # #     file.write(f"Lowest: {lowest}\n")
# # # # #     file.write(f"Average: {average:.2f}\n")

# # # # marks = [80, 90, 70, 85]

# # # # total = sum(marks)
# # # # highest = max(marks)
# # # # lowest = min(marks)
# # # # average = total / len(marks)

# # # # print(f"Marks: {marks}")
# # # # print(f"Total: {total}")
# # # # print(f"Highest: {highest}")
# # # # print(f"Lowest: {lowest}")
# # # # print(f"Average: {average:.2f}")

# # # # with open("result.txt", "w") as file:
# # # #     file.write(f"Marks: {marks}\n")
# # # #     file.write(f"Total: {total}\n")
# # # #     file.write(f"Highest: {highest}\n")
# # # #     file.write(f"Lowest: {lowest}\n")
# # # #     file.write(f"Average: {average:.2f}\n")

# # # # numbers = [1, 2, 3, 4, 5]
# # # # squares = [number * number for number in numbers]
# # # # print(list(numbers))



# # # # squares = []

# # # # for number in numbers:
# # # #     squares.append(number * number)

# # # print(squares)
# # # numbers = [1, 2, 3, 4, 5]

# # # # squares=[number*number for number in numbers]
# # # # print(squares)

# # # names = ["ajmal", "rahul", "aju"]

# # # uppercase_names=[name.upper() for name in names]
# # # print(uppercase_names)

# # # squares = [1,2,3,4,5,6,7]
# # # square=[]

# # # for number in squares:
# # #     square= number * number

# # #     print(square)

# # squares={}

# # for num in range(1,4):
# #     squares[num]=num*num
# # print(squares)

# # numbers=range(1,11)
# # even_squares={
# #     number:number*number
# #     for number in numbers
# #     if number%2==0
# # }
# # print(even_squares)

# # marks = [80, 45, 90, 65, 30, 75]

# # passed_marks = [mark for mark in marks if mark >= 50]

# # total_marks = sum(marks)
# # highest_mark = max(marks)
# # lowest_mark = min(marks)
# # average_mark = total_marks / len(marks)

# # print("Passed:", passed_marks)
# # print("Total:", total_marks)
# # print("Highest:", highest_mark)
# # print("Lowest:", lowest_mark)
# # print("Average:", average_mark)

# # names=("hallo,world")
# # names =names.replace("h","w")
# # print(names)

# number=[1,2,3,4,5,6,7,8]

# for i in range(len(number)):
#     if number[i]==2:
#         number[i]=100
#     elif number[i]==3:
#         number[i]=200
#     elif number[i]==7:
#         number[i]=700
# print(number)

# name=("hallo,ajmal")
# name=name[:3]+"s"+name[4:]
# print(name)

# name=("hallo,ajmal")
# name=name[:3]+"s"+name[4:10]+"w"+name[11:11]+"xxx"+name[11:]
# print(name)

# a = 10
# b = 3

# print(a + b)
# print(a > b)
# print(a == b)
# print(a > 5 and b < 5)

# name="ajmal"
# age=21
# hight=167
# is_student=True

# print(name)
# print(age)
# print(hight)
# print(is_student)

# a=10
# b=11

# print("addition:",a+b)
# print("substraction:",a-b)
# print("multiplication:",a*b)
# print("division:",round(a/bjgv,1))

# # age=int(input("enter your age: "))
# # future_age = age + 5
# # print("After 5 years:",future_age)
 
# age=int(input("enter your age: "))
