# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:07:43 2018
@author: G Sriram
"""
import os
class Books(object): 
    def __init__(self, isbn,name,author,stock,dept):
        '''
        Function to initialise the isbn, name, author and stock of any book
        '''
        self.isbn=isbn
        self.name=name
        self.author=author
        self.stock=stock
        self.dept=dept
    def getisbn(self):
        '''
        Function that returns the ISBN of the book
        '''
        return self.isbn
    def getname(self):
        '''
        Function which returns the name of the book
        '''
        return self.name
    def getauthor(self):
        '''
        Function which returns the author of the book
        '''
        return self.author
    def getstock(self):
        '''
        Function which returns the stock
        '''
        return self.stock
    def getdept(self):
        '''
        Function which returns the department which the book is related to.
        '''
        return self.dept

class Students(object):
    def __init__(self,name,reg_no,email,num):
        '''
        Function to assign the student name, registration number, E-Mail ID and Ph.No of the student issuing the book
        '''
        self.name=name
        self.reg_no=reg_no
        self.email=email
        self.num=num
    def getname(self):
        '''
        Returns the name of the student
        '''
        return self.name
    def get_rno(self):
        '''
        Returns the Registration number of the Student
        '''
        return self.reg_no
    def get_email(self):
        '''
        Returns the E-Mail of the student
        '''
        return self.email
    def get_num(self):
        '''
        Returns the Phone number of the student
        '''
        return self.num

class faculty(object):
    def __init__(self,name,e_no,dept):
        '''
        Function to assign the Faculty name, Employee Number and Department of Faculty
        '''
        self.name=name
        self.e_no=e_no
        self.dept=dept
    def getname(self):
        '''
        Returns the name of the Faculty
        '''
        return self.name
    def get_eno(self):
        '''
        Returns the employee number of the faculty
        '''
        return self.e_no
    def get_dept(self):
        '''
        Returns the Department of the Faculty
        '''
        return self.dept
    
def addStudent():
    '''
    A function which prompts a user to enter the details of students and returns an instance containing all info.
    The function also writes into a text file the details of the student. 
    Arguments: None
    Return: s of type Student containing all information about a student. 
    '''
    regno=str(input("Enter the registration number of the student: "))
    name=str(input("Enter the name of the student:")) 
    email=str(input("Enter the E-Mail ID of the student: "))
    while True:    
        number=str(input("Enter Phone Number of student: "))
        if(len(number)==10):
            break
        else:
            print("Please enter a valid Phone Number.")       
    s=Students(name,regno,email,number)
    return s


def addBook():
    '''
    Function which prompts the user to enter the details of the book and returns an instance containing all the info.
    The function also writes into a text file the details of the book
    Arguments: None
    Return: b of type Books containing all the information about a book.
    '''
    isbn=str(input("Enter the ISBN of the book: "))
    name=str(input("Enter the Name of the book: "))
    author=str(input("Enter the Author of the book: "))
    stock=int(input("Enter the number of books available: "))
    while True:
        dept=str(input("Enter the department to which the book is related to(CSE,ECE,ME,IT,Others) :"))
        if(dept in ('CSE','ECE','ME','IT','Others')):
            break
        else:
            print("Please enter a valid department name.")

    b=Books(isbn,name,author,stock,dept)
    return b

def addFaculty():
    '''
    Function which prompts the user to enter the details of faculty and returns an instance containing all the info.
    The function also writes into a text file the details of the Faculty
    Arguments: None
    Return: f of type faculty containing all the information about a Faculty.
    '''
    name=str(input("Enter the name of the Faculty: "))
    e_no=str(input("Enter the Employee ID of the Faculty: "))
    dept=str(input("Enter the Department of the Faculty: "))

    f=faculty(name,e_no,dept)
    return f

def writeStudent(s):
    '''
    Function which writes into a text file the details of student each time the function is called.
    Arguments: s of type Student.
    Return: None.
    '''
    fw=open('studlist.txt','a')
    writelist=str(s.getname()+'$$'+s.get_rno()+'$$'+s.get_email()+'$$'+s.get_num()+'\n')
    fw.write(writelist)
    fw.close()

def writeBook(b):
    '''
    Function which writes into a text file the details of Book each time the function is called.
    Arguments: b of type Book.
    Return: None.
    '''
    fw=open('booklist.txt','a')
    writelist=str(b.getisbn()+'$$'+b.getname()+'$$'+b.getauthor()+'$$'+str(b.getstock())+'$$'+b.getdept()+'\n')
    fw.write(writelist)
    fw.close()
def writeFaculty(f):
    '''
    Function which writes into a text file the details of Faculty each time the function is called.
    Arguments: f of type Faculty.
    Return: None.
    '''
    fw=open('facultylist.txt','a')
    writelist=str(f.getname()+'$$'+f.get_eno()+'$$'+f.get_dept()+'\n')
    fw.write(writelist)
    fw.close()
def readStudent():
    '''
    Function to read the student list from text file and return a list of students details.
    Arguments: None. 
    Return: List with elements of type Student
    '''
    fr=open('studlist.txt','r')
    a=[]
    for line in fr:
        x=line.split('$$')
        a.append(Students(x[0],x[1],x[2],x[3]))
    fr.close()
    return a
def readBooks():
    '''
    Function to read the books list from text file and return a list of books details.
    Arguments: None. 
    Return: List with elements of type Books
    '''
    fr=open('booklist.txt','r')
    a=[]
    for line in fr:
        x=line.split('$$')
        a.append(Books(x[0],x[1],x[2],x[3],x[4]))
    fr.close()
    return a
def readFaculty():
    '''
    Function to read the faculty list from text file and return a list of faculty details.
    Arguments: None. 
    Return: List with elements of type Faculty
    '''
    fr=open('facultylist.txt','r')
    a=[]
    for line in fr:
        x=line.split('$$')
        a.append(faculty(x[0],x[1],x[2]))
    fr.close()
    return a
def searchStudents(reg_no):
    '''
    Function to search for student in the file and return the details of the student.
    Arguments: reg_no of type string.
    Return: s of type Student.
    '''
    studlist=readStudent()
    for i in studlist:
        if(i.get_rno()==reg_no):
            return i
    
    
def searchBooks(isbn):
    '''
    Function to search for book in the file and return the details of the book.
    Arguments: isbn of type string.
    Return: b of type Books.
    '''
    booklist=readBooks()
    for i in booklist:
        if(i.getisbn()==isbn):
            return i
      
    
def searchFaculty(eno):
    '''
    Function to search for faculty in the file and return the details of the faculty.
    Arguments: eno of type string.
    Return: f of type faculty.
    '''
    flist=readFaculty()
    for i in flist:
        if(i.get_eno()==eno):
            return i
     

def modifyStudent(reg_no):
    '''
    Function to Modify list of students, given the registration number.
    Arguments: reg_no of type string.
    Return: None
    '''
    studlist=readStudent()
    fw=open('studlist1.txt','a')
    for i in studlist:
        if(i.get_rno()==reg_no):
            s=addStudent()
            writelist=str(s.getname()+'$$'+s.get_rno()+'$$'+s.get_email()+'$$'+s.get_num()+'\n')
            fw.write(writelist)
        else:
            writelist=str(i.getname()+'$$'+i.get_rno()+'$$'+i.get_email()+'$$'+i.get_num())
            fw.write(writelist)           
    fw.close()
    os.remove('studlist.txt')
    os.rename('studlist1.txt','studlist.txt')
    
def modifyBook(isbn):
    '''
    Function to Modify list of Book, given the ISBN.
    Arguments: isbn of type string.
    Return: None
    '''
    booklist=readBooks()
    fw=open('booklist1.txt','a')
    for i in booklist:
        if(i.getisbn()==isbn):
            b=addBook()
            writelist=str(b.getisbn()+'$$'+b.getname()+'$$'+b.getauthor()+'$$'+str(b.getstock())+'$$'+b.getdept()+'\n')
            fw.write(writelist)
        else:
            writelist=str(i.getisbn()+'$$'+i.getname()+'$$'+i.getauthor()+'$$'+str(i.getstock())+'$$'+i.getdept())
            fw.write(writelist)           
    fw.close()
    os.remove('booklist.txt')
    os.rename('booklist1.txt','booklist.txt')
def modifyFaculty(e_no):
    '''
    Function to Modify list of faculty, given the Employee.
    Arguments: e_no of type string.
    Return: None
    '''
    flist=readFaculty()
    fw=open('facultylist1.txt','a')
    for i in flist:
        if(i.get_eno()==e_no):
            f=addFaculty()
            writelist=str(f.getname()+'$$'+str(f.get_eno())+'$$'+f.get_dept()+'\n')
            fw.write(writelist)
        else:
            writelist=str(i.getname()+'$$'+str(i.get_eno())+'$$'+i.get_dept())
            fw.write(writelist)    
    fw.close()
    os.remove('facultylist.txt')
    os.rename('facultylist1.txt','facultylist.txt') 
def deleteStudent(reg_no):
    '''
    Function to delete a student, given the registration number.
    Arguments: reg_no of type string.
    Return: None
    '''
    studlist=readStudent()
    fw=open('studlist1.txt','a')
    for i in studlist:
        if(i.get_rno()==reg_no):
            continue
        else:
            writelist=str(i.getname()+'$$'+i.get_rno()+'$$'+i.get_email()+'$$'+i.get_num())
            fw.write(writelist)           
    fw.close()
    os.remove('studlist.txt')
    os.rename('studlist1.txt','studlist.txt')

def deleteBook(isbn):
    '''
    Function to delete a book, given the ISBN.
    Arguments: isbn of type string.
    Return: None
    '''
    booklist=readBooks()
    fw=open('booklist1.txt','a')
    for i in booklist:
        if(i.getisbn()==isbn):
            continue
        else:
            writelist=str(i.getisbn()+'$$'+i.getname()+'$$'+i.getauthor()+'$$'+i.getstock()+'$$'+i.getdept())
            fw.write(writelist)           
    fw.close()
    os.remove('booklist.txt')
    os.rename('booklist1.txt','booklist.txt')

def deleteFaculty(e_no):
    '''
    Function to delete a faculty, given the employee number.
    Arguments: e_no of type string.
    Return: None
    '''
    flist=readFaculty()
    fw=open('facultylist1.txt','a')
    for i in flist:
        if(i.get_eno()==e_no):
            continue
        else:
            writelist=str(i.getname()+'$$'+i.get_eno()+'$$'+i.get_dept())
            fw.write(writelist)    
    fw.close()
    os.remove('facultylist.txt')
    os.rename('facultylist1.txt','facultylist.txt') 
    
def sendFacultyEmail(b):
    '''
    A Function which notifies the faculty belonging to a certain department whenever a new book comes in the library.
    Arguments: b of type books
    Retrun: None.
    '''
    email={'CSE':'YOUR EMAIL HERE','ECE':'YOUR EMAIL HERE','ME':'YOUR EMAIL HERE','IT':'YOUR EMAIL HERE','Others':'YOUR EMAIL HERE'}
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    fromaddr = "YOUR EMAIL HERE"
    toaddr = email[b.getdept()]
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "New Book added to the Library!"
    body = "Dear Sir/Ma'am, \n\n"+"A New book has been added to the library which is related to your department. \n"+ "\nThe details are as follows: \n"+ "\nName: " + b.getname()+ "\nAuthor: "+b.getauthor()+"\n\nPlease inform the students of your department.\n"+ "Thank You." 
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "YOUR PASSWORD HERE")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def BookIssueStudent(isbn,reg_no):
    '''
    A Function which issues books to students.
    Arguments: isbn of type str and reg_no of type str
    Return: None
    '''
    b=searchBooks(isbn)
    if(int(b.getstock())>0):
        fw=open("BookIssueStudent.txt",'a')
        writeText=str(reg_no+'$$'+isbn+'\n')
        fw.write(writeText)
        fw.close()
        b.stock=int(b.stock)-1
        booklist=readBooks()
        fw=open('booklist1.txt','a')
        for i in booklist:
            if(i.getisbn()==isbn):
                writelist=str(b.getisbn()+'$$'+b.getname()+'$$'+b.getauthor()+'$$'+str(b.getstock())+'$$'+b.getdept())
                fw.write(writelist)
            else:
                writelist=str(i.getisbn()+'$$'+i.getname()+'$$'+i.getauthor()+'$$'+str(i.getstock())+'$$'+i.getdept())
                fw.write(writelist)           
        fw.close()
        os.remove('booklist.txt')
        os.rename('booklist1.txt','booklist.txt')
    else:
        print("Book not in stock")
        
def BookIssueFaculty(isbn,e_no):
    '''
    Function which issues books to Faculty
    Arguments: isbn and e_no of type str
    Return: None
    '''
    b=searchBooks(isbn)
    if(int(b.getstock())>0):
        fw=open("BookIssueFaculty.txt",'a')
        writeText=str(e_no+'$$'+isbn+'\n')
        fw.write(writeText)
        fw.close()
        b.stock=int(b.stock)-1
        booklist=readBooks()
        fw=open('booklist1.txt','a')
        for i in booklist:
            if(i.getisbn()==isbn):
                writelist=str(b.getisbn()+'$$'+b.getname()+'$$'+b.getauthor()+'$$'+str(b.getstock())+'$$'+b.getdept())
                fw.write(writelist)
            else:
                writelist=str(i.getisbn()+'$$'+i.getname()+'$$'+i.getauthor()+'$$'+str(i.getstock())+'$$'+i.getdept())
                fw.write(writelist)           
        fw.close()
        os.remove('booklist.txt')
        os.rename('booklist1.txt','booklist.txt')
    else:
        print("Book not in stock")
        
def BookReturnStudent(isbn,reg_no):
    '''
    Function which returns books from students
    Arguments: isbn and reg_no of type str
    Return: None
    '''
    b=searchBooks(isbn)
    fr=open("BookIssueStudent.txt",'r')
    fw=open("BookIssueStudent1.txt",'a')
    a=[]
    for line in fr:
        x=line.split('$$')
        a.append((x[0],x[1][:-1]))
    fr.close()
    for i in a:
        if((i[0]==reg_no and i[1]==isbn)==False):
            writeList=(i[0]+'$$'+i[1]+'\n')
            fw.write(writeList)
    fw.close()
    os.remove('BookIssueStudent.txt')
    os.rename('BookIssueStudent1.txt','BookIssueStudent.txt')
    b.stock=int(b.stock)+1
    booklist=readBooks()
    fw=open('booklist1.txt','a')
    for i in booklist:
        if(i.getisbn()==isbn):
            writelist=str(b.getisbn()+'$$'+b.getname()+'$$'+b.getauthor()+'$$'+str(b.getstock())+'$$'+b.getdept())
            fw.write(writelist)
        else:
            writelist=str(i.getisbn()+'$$'+i.getname()+'$$'+i.getauthor()+'$$'+str(i.getstock())+'$$'+i.getdept())
            fw.write(writelist)           
    fw.close()
    os.remove('booklist.txt')
    os.rename('booklist1.txt','booklist.txt')    
    
    
def BookReturnFaculty(isbn,e_no):
    '''
    Function which returns books from faculty
    Arguments: isbn and e_no of type str
    Return: None
    '''
    b=searchBooks(isbn)
    fr=open("BookIssueFaculty.txt",'r')
    fw=open("BookIssueFaculty1.txt",'a')
    a=[]
    for line in fr:
        x=line.split('$$')
        a.append((x[0],x[1][:-1]))
    fr.close()
    for i in a:
        if((i[0]==e_no and i[1]==isbn)==False):
            writeList=(i[0]+'$$'+i[1]+'\n')
            fw.write(writeList)
    fw.close()
    os.remove('BookIssueFaculty.txt')
    os.rename('BookIssueFaculty1.txt','BookIssueFaculty.txt')
    b.stock=int(b.stock)+1
    booklist=readBooks()
    fw=open('booklist1.txt','a')
    for i in booklist:
        if(i.getisbn()==isbn):
            writelist=str(b.getisbn()+'$$'+b.getname()+'$$'+b.getauthor()+'$$'+str(b.getstock())+'$$'+b.getdept())
            fw.write(writelist)
        else:
            writelist=str(i.getisbn()+'$$'+i.getname()+'$$'+i.getauthor()+'$$'+str(i.getstock())+'$$'+i.getdept())
            fw.write(writelist)           
    fw.close()
    os.remove('booklist.txt')
    os.rename('booklist1.txt','booklist.txt')  

def SearchStudentBooks(reg_no):
    '''
    Function which searches for the list of books which a student has borrowed
    Arguments: reg_no of type str
    Return: List of Books of type Books
    '''
    fr=open('BookIssueStudent.txt','r')
    borrowedBooks=[]
    borrowedBooks1=[]
    for line in fr:
        x=line.split('$$')
        if(x[0]==reg_no):
             borrowedBooks.append(x[1][:-1])
    fr.close()
    for i in borrowedBooks:
        borrowedBooks1.append(searchBooks(i))
    return borrowedBooks1

def SearchFacultyBooks(e_no):
    '''
    Function which searches for the list of books which a faculty has borrowed
    Arguments: e_no of type str
    Return: List of Books of type Books
    '''
    fr=open('BookIssueFaculty.txt','r')
    borrowedBooks=[]
    borrowedBooks1=[]
    for line in fr:
        x=line.split('$$')
        if(x[0]==e_no):
             borrowedBooks.append(x[1][:-1])
    fr.close()
    for i in borrowedBooks:
        borrowedBooks1.append(searchBooks(i))
    return borrowedBooks1

            
def menu():
    
    '''
    A Function which acts as a menu to the program which takes in the input of the user and performs function calls as necessary
    Arguments: None
    Return: None
    '''
    
    while True:
        os.system('clear')
        print("Main Menu".center(40))
        print("1. Add Book")
        print("2. Add Student Member")
        print("3. Add Faculty Member")
        print("4. View Book Details")
        print("5. View Student Details")
        print("6. View Faculty Details")
        print("7. Modify Book Details")
        print("8. Modify Student Details")
        print("9. Modify Faculty Details")
        print("10. Delete Book")
        print("11. Delete Student Member")
        print("12. Delete Faculty Member")
        print("13. Book Issue for Students")
        print("14. Book Issue for Faculty")
        print("15. Book Return for Students")
        print("16. Book Return for Faculty")
        print("17. Exit")
        ch=int(input("Enter your choice: " ))
        if(ch in range(1,18)):
            break
        else:
            print("Please Enter a valid choice!")
            input("Press <Enter> to return back to the menu.")
    if(ch==1):
        os.system('clear')
        print("Add a Book".center(40))
        b=addBook()
        writeBook(b)
        #sendFacultyEmail(b)
        print("Book Successfully added!")
        input("Press <Enter> to return back to the menu.")
        menu()
    if(ch==2):
        os.system('clear')
        print("Add a Student Member".center(40))
        s=addStudent()
        writeStudent(s)
        print("Student Member Successfully added!")
        input("Press <Enter> to return back to the menu.")
        menu() 
    if(ch==3):
        os.system('clear')
        print("Add a Faculty Member".center(40))
        s=addFaculty()
        writeFaculty(s)
        print("Faculty Member Successfully added!")
        input("Press <Enter> to return back to the menu.")
        menu()   
    if(ch==4):
        try:
            os.system('clear')
            isbn=input("Enter the ISBN of the book to display the details: ")
            b=searchBooks(isbn)
            os.system('clear')
            print("Book Details".center(40))
            print("ISBN:",b.getisbn())
            print("Name:",b.getname())
            print("Author:",b.getauthor())
            print("Stock:",b.getstock())
            print("Department:",b.getdept())
        except:
            print("Book not found!")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()
    if(ch==5):
        try:
            os.system('clear')
            reg_no=input("Enter the Registration Number of the Student to display the details: ")
            s=searchStudents(reg_no)
            sb=SearchStudentBooks(reg_no)
            os.system('clear')
            print("Student Details".center(40))
            print("Registration Number:",s.get_rno())
            print("Name:",s.getname())
            print("E-Mail ID:",s.get_email())
            print("Phone Number:",s.get_num())
            print("Borrowed Books: ")
            x=1
            for i in sb:
               print(str(x)+'.',i.getname())
               x+=1
        except:
            print("Student not found!")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()
    if(ch==6):
        try:
            os.system('clear')
            e_no=input("Enter the Employee Number of the Faculty to display the details: ")
            f=searchFaculty(e_no)
            sb=SearchFacultyBooks(e_no)
            os.system('clear')
            print("Faculty Details".center(40))
            print("Employee Number:",f.get_eno())
            print("Name:",f.getname())
            print("Department: ",f.get_dept())
            print("Borrowed Books: ")
            x=1
            for i in sb:
               print(str(x)+'.',i.getname())
               x+=1
        except:
            print("Faculty not found!")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()
    if(ch==7):
        try:
            os.system('clear')
            isbn=input("Enter the ISBN of the book to modify: ")
            if(searchBooks(isbn)==None):
                raise ValueError("X")
            modifyBook(isbn)
            print("Successfully Modified!")
        except:
            print("Book not found/Unable to modify the book.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()            
    if(ch==8):
        try:
            os.system('clear')
            reg_no=input("Enter the Registration Number of the Student to modify: ")
            if(searchStudents(reg_no)==None):
                raise ValueError("X")
            modifyStudent(reg_no)
            print("Successfully Modified!")
        except:
            print("Student not found/Unable to modify the details.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()             
    if(ch==9):
        try:
            os.system('clear')
            e_no=input("Enter the Employee Number of the Faculty to modify: ")
            if(searchFaculty(e_no)==None):
                raise ValueError("X")
            modifyFaculty(e_no)
            print("Successfully Modified!")
        except:
            print("Faculty not found/Unable to modify the details.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu() 
             
    if(ch==10):
        try:
            os.system('clear')
            isbn=input("Enter the ISBN of the book to delete: ")
            if(searchBooks(isbn)==None):
                raise ValueError("X")
            deleteBook(isbn)
            print("Successfully Deleted!")
        except:
            print("Book not found/Unable to delete the book.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu() 
    if(ch==11):
        try:
            os.system('clear')
            reg_no=input("Enter the Registration Number of the Student to delete: ")
            if(searchStudents(reg_no)==None):
                raise ValueError("X")
            deleteStudent(reg_no)
            print("Successfully deleted!")
        except:
            print("Student not found/Unable to remove the details.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()
            
    if(ch==12):
        try:
            os.system('clear')
            e_no=input("Enter the Employee Number of the Faculty to delete: ")
            if(searchFaculty(e_no)==None):
                raise ValueError("X")
            deleteFaculty(e_no)
            print("Successfully Deleted!")
        except:
            print("Faculty not found/Unable to delete the details.")
        finally:
            input("Press <Enter> to return back to the menu.")
            menu()
            
    if(ch==13):
        os.system('clear')
        reg_no=input("Enter the Registration Number of the Student: ")
        isbn=input("Enter the ISBN of the Book to be issued: ")
        if(searchBooks(isbn)==None):
            print("Book not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif(searchStudents(reg_no)==None):
            print("Student Member not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        else:
            BookIssueStudent(isbn,reg_no)
            print("Book Successfully issued!")
            input("Press <Enter> to return back to the menu.")
            menu()
            
    if(ch==14):
        os.system('clear')
        e_no=input("Enter the Employee Number of the Faculty: ")
        isbn=input("Enter the ISBN of the Book to be issued: ")
        if(searchBooks(isbn)==None):
            print("Book not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif(searchFaculty(e_no)==None):
            print("Faculty Member not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        else:
            BookIssueFaculty(isbn,e_no)
            print("Book Successfully issued!")
            input("Press <Enter> to return back to the menu.")
            menu()
    if(ch==15):
        os.system('clear')
        reg_no=input("Enter the Registration Number of the Student: ")
        isbn=input("Enter the ISBN of the Book to be issued: ")
        fr=open("BookIssueStudent.txt",'r')
        a=[]
        for line in fr:
            x=line.split('$$')
            a.append((x[0],x[1][:-1]))
        fr.close()
        if(searchBooks(isbn)==None):
            print("Book not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif(searchStudents(reg_no)==None):
            print("Student Member not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif((reg_no,isbn) not in a):
            print("Student has not borrowed the book of given ISBN.")
            input("Press <Enter> to return back to the menu.")
            menu()
        else:
            BookReturnStudent(isbn,reg_no)
            print("Book Successfully returned!")
            input("Press <Enter> to return back to the menu.")
            menu()
    
    if(ch==16):
        os.system('clear')
        e_no=input("Enter the Employee Number of the Faculty: ")
        isbn=input("Enter the ISBN of the Book to be issued: ")
        fr=open("BookIssueFaculty.txt",'r')
        a=[]
        for line in fr:
            x=line.split('$$')
            a.append((x[0],x[1][:-1]))
        fr.close()
        if(searchBooks(isbn)==None):
            print("Book not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif(searchFaculty(e_no)==None):
            print("Faculty Member not found!")
            input("Press <Enter> to return back to the menu.")
            menu()
        elif((e_no,isbn) not in a):
            print("Faculty has not borrowed the book of given ISBN.")
            input("Press <Enter> to return back to the menu.")
            menu()
        else:
            BookReturnFaculty(isbn,e_no)
            print("Book Successfully returned!")
            input("Press <Enter> to return back to the menu.")
            menu()    
             
menu()      
 
    
