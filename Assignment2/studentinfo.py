def filterCourse(courseList, branch, year):
        i=0
        filteredList=[]
        for course in courseList:
            if(course.courseId[0]==branch and int(course.courseId[2])==year):
                filteredList.append(course)
            i=i+1
        return filteredList

class Courses:
    def __init__(self, name, C_id):
        self.courseName=name
        self.courseId=C_id

class Student:
    #This is How you declare a constructor
    #Read More about self
    def __init__ (self, name ,rollno, semester):
        self.studentName=name
        self.studentRollno=rollno
        self.studentSem=semester
        self.studentCourseList=[]
        if semester is "I" or semester is "II":
            self.studentYear=1
        elif semester is "III" or semester is "IV":
            self.studentYear=2
        elif semester is "V" or semester is "VI":
            self.studentYear=3
        else:
            self.studentYear=4
    def assigncourse(self, courseList):
        i=0
        while(i<3):
            self.studentCourseList.append(courseList[i])
            i=i+1
        
def main():
    #List of all students taking courses
    studentList=[
            Student("Akshay", "CS30000", "V"), 
            Student("Naman", "EC40001", "VII"),
            Student("Deepak", "CS10002", "I"),
            Student("Aditya", "EC30000", "V"),
            Student("JJ", "EC20007", "III")]

    #List of all courses offered
    courseList=[
            Courses("Cloud Computing", "CS351"),
            Courses("Analog Circuits", "EC200"),
            Courses("Digital Design", "EC201"),
            Courses("Digital Signal Processing", "EC251"), 
            Courses("Analog Signal Processing", "EC451"),
            Courses("Image Processing", "EC452"),
            Courses("Instrumentation and Measurement", "EC453"),
            Courses("Data Structures", "CS352"),
            Courses("Algorithms", "CS353"),
            Courses("Discrete Mathematics", "CS355"),
            Courses("Optimation Techniques", "CS151"),
            Courses("Programming in C", "CS101"),
            Courses("IT-Workshop 1", "CS112"),
            Courses("VLSI Design", "EC301"),
            Courses("Control Systems", "EC371"),
            Courses("Electromagnetism", "EC351"),
            ]
    #Iterating over students and assigning them 3 courses each
    i=0
    #Opening File where records will be put into
    fo=open("studentCourseInfo.txt", 'w')
    content="Student Name \t\t Roll Number\t\t Year \t\t Courses Taken\n"
    fo.write(content)
    for student in studentList:
        requiredList=filterCourse(courseList, student.studentRollno[0], student.studentYear)
        student.assigncourse(requiredList)
        content=student.studentName+"\t\t"+student.studentRollno+"\t\t"+str(student.studentYear)+"\t\t"
        j=0
        for courseTaken in student.studentCourseList:
            content=content+courseTaken.courseName +" ("+courseTaken.courseId+"), "
            j=j+1
        content=content+"\n"
        fo.write(content)
        i=i+1
    fo.close()

if __name__=="__main__":
    main()
