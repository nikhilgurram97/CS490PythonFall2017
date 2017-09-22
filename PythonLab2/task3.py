class Student:                                                     #first class
    def __init__(self, name, id, country, password=None):          #using init function
        self.studentname=name
        self.studentid=id
        self.studentcountry=country
        self.__studentpassword=password                            #private data member "Password"

class course(Student):                                             #child class of parent class Student
    def __init__(self,cid,cname,id,name,country):                  #using init function
        Student.__init__(self,name,id,country)                     #implementing a super call
        self.studentcid=cid
        self.studentcname=cname

class mark(Student):                                               #child class of parent class Student
    def __init__(self, marks,id,cid,name,country,cname):           #using init function
        Student.__init__(self,name,id,country)                     #implementing a super call of Student class init
        course.__init__(self,cid,cname,id,name,country)            #implementing a super call of course class init
        self.studentmarks=marks

class gpa(mark):                                                   #child class of parent class mark
    def __init__(self, marks,id,cid,name,country,cname):           #using init function
        mark.__init__(self, marks,id,cid,name,country,cname)       #implementing a super call of mark class init
        self.marks=marks
    def calc1(self,marks):                                         #function to calculate GPA
        k=int(marks)*4/50
        return(k)

class grade(mark):
    def __init__(self, marks,id,cid,name,country,cname):           #child class of parent class mark
        mark.__init__(self, marks,id,cid,name,country,cname)       #using init function
        self.marks=marks                                           #implementing a super call of mark class init
    def calc2(self,marks):
        j=int(marks)*100/50                                        #function to calculate grade
        return(j)



while True:                                                        #implementing loop to iterate over all the classes
    val=int(input("\nWhat is your task selection?:\n1)Add Student Info\n2)Show Student Info\n3)Add Student Course\n4)Show Added Student Courses\n5)Add Student Marks\n6)Show Calculated GPA\n7)Show Calculated Percentage\n0)Exit Program\n"))

    if (val == 1):
        a1=input("Enter Student Name: ")
        a2=input("Enter Student ID: ")
        a3=input("Enter Student Country: ")
        a4=input("Enter password: ")
        ins1=Student(a1,a2,a3,a4)                                   #giving input to class using instances
        print("Created Student Successfully!")
            

    if (val == 2):
        print("Name: "+ins1.studentname+"\nID: "+ins1.studentid)    #printing output from class using instances


    if (val == 3):
        b1=input("Enter Course Name: ")
        b2=input("Enter Course ID: ")
        b3=input("Enter Student ID: ")
        ins2=course(b1,b2,b3,ins1.studentname,ins1.studentcountry)  #using instances for input
        print("Added Course Successfully")


    if (val == 4):
        print("Student ID: "+ins2.studentid+"Course Info: "+ins2.studentcid+ins2.studentcname)  #using instances for output


    if (val == 5):
        c1=int(input("Enter marks out of 50: "))
        c2=input("Enter Student ID: ")
        c3=input("Enter Course ID: ")
        ins3=mark(c1,c2,c3,ins1.studentname,ins1.studentcountry,ins2.studentcname)        #using instances


    if (val == 6):
        d1=ins3.studentmarks
        ins4= gpa(d1,ins2.studentid,ins2.studentcid,ins1.studentname,ins1.studentcountry,ins2.studentcname)    #using instances
        print("Your GPA out of 4: "+str(ins4.calc1(d1)))                                         #using instances and member function of class

    if (val == 7):
        e1=ins3.studentmarks
        ins5=grade(e1,ins2.studentid,ins2.studentcid,ins1.studentname,ins1.studentcountry,ins2.studentcname)   #using instances
        print("Your Percent out of 100: "+str(ins5.calc2(e1)))                                     #using instances and member function of class

    if (val == 0):
        break                                                                                     #ending condition for loop to stop program