class student:
    def __init__(self,student_id,name,department,mark1,mark2,mark3,):
        self.student_id=student_id
        self.name=name
        self.department=department
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3

    def display_details(self):
        print("student_id:",self.student_id)
        print("name:",self.name)
        print("department:",self.department)
        print("mark1:",self.mark1)
        print("mark2:",self.mark2)
        print("mark3",self.mark3)

    def calculate_total(self):
        total=self.mark1+self.mark2+self.mark3
        return total
    def calculate_avarge(self):
        avarage=self.calculate_total/3
        return avarage
    def is_passed(self):
        if self.mark1>=40 and self.mark2>=40 and self.mark3>=40:
            return True
        else:
            return False

student1=student("SS01","aju","cs",60,70,80)
student2=student("SS02","sinan","bs",65,75,85)
student3=student("SS03","ashmal","commerce",88,98,100)

if student2.is_passed():
    print("Status: Passed")
else:
    print("Status: Failed")



