# Done By Eng.Belal.s.El_Radei
class book:
    def __init__(self, price, Name=" ", Id=0, author=" ", edition=0, rackNo=0, subjectCode=0, quantity=0, Available=True):
        self.Id = Id
        self.Name = Name
        self.author = author
        self.price = price
        self.quantity = quantity
        self.rackNo = rackNo
        self.subjectCode = subjectCode
        self.edition = edition
        self.Available = Available

    def __str__(self):
        return "Book_Id: "+"["+str(self.Id)+"]" + " ,Book_Name: "+"["+str(self.Name)+"]" + " ,Book_Author: "+"["+str(self.author)+"]"+" ,Book_Edition: "+"["+str(self.edition)+"]"\
            + " ,Book_Price: " + \
            "["+str(self.price)+" $]" + " ,Book_Available: " + \
            "["+str(self.Available)+"]"+"\n"


class Issue_Book:
    def __init__(self, Name, Date_Issue, Return_Date, User_Id=0, Book_Id=0):
        self.Name = Name
        self.Date_Issue = Date_Issue
        self.Return_Date = Return_Date
        self.User_Id = User_Id
        self.Book_Id = Book_Id

    def __str__(self):
        return "Book_Id: "+"["+str(self.Book_Id)+"]"+" ,Book_Name: "+"["+str(self.Name)+"]"+" ,User_Id: "+"["+str(self.User_Id)+"]"\
               + " ,Date_Issue: "+"["+str(self.Date_Issue) + "]" + \
            " ,Date_Return: "+"["+str(self.Return_Date)+"]"+"\n"


class user:
    def __init__(self, Name, Id, Address):
        self.Name = Name
        self.Id = Id
        self.Address = Address
    List_Of_Book = []
    List_Of_Issue_Books = []
    listOfUser = []

    def __str__(self):
        return "User_Id: "+"["+str(self.Id)+"]"+" ,User_Name: "+"["+str(self.Name)+"]"+" ,User_Address: "+"["+str(self.Address)+"]"+"\n"


class admin(user):
    def __init__(self, Name, Id, Address):
        super().__init__(Name, Id, Address)

    def Add_Books(self, Id, Name, author, edition, price):
        if not self.CheakBook(Id):
            b = book(price, Name, Id, author, edition)
            self.List_Of_Book.append(b)
            self.Copy_To_File(self.List_Of_Book)
            print(
                "******************************* Book Added 😘 *******************************")
        else:
            print("Id Is Uesed 😢")

    def Update_Book(self, Id_Before, Id_After):
        if self.CheakBook(Id_Before):
            for b in self.List_Of_Book:
                if b.Id == Id_Before:
                    b.Id = Id_After
                    self.Copy_To_File(self.List_Of_Book)
                    print(
                        "******************************* Book Updated 😘 *******************************")
        else:
            print("Not Found")

    def Delete_Books(self, Id):
        if self.CheakBook(Id):
            for b in self.List_Of_Book:
                if b.Id == Id:
                    self.List_Of_Book.remove(b)
                    self.Copy_To_File(self.List_Of_Book)
                    print(
                        "******************************* Book Deleted 😘 *******************************")
        else:
            print("Not Found")

    def Add_User(self, Name, Id, Address):
        if not self.CheakUser(Id):
            u = Student(Name, Id, Address)
            self.listOfUser.append(u)
            self.copyToFileUser(self.listOfUser)
            print(
                "******************************* User Added 😘 *******************************")
        else:
            print("Id Is Used 😢")

    def Display_Users(self):
        print("---------------------------List of User---------------------------\n"
              "User Id:         User Name:           User Address:\n")
        for u in self.listOfUser:
            print(u, end="")

    def Delete_User(self, Id):
        if self.CheakUser(Id):
            for u in self.listOfUser:
                if u.Id == Id:
                    self.listOfUser.remove(u)
                    self.copyToFileUser(self.listOfUser)
                    print(
                        "******************************* User Deleted 😘 *******************************")
        else:
            print("Not Found")

    def Update_User(self, oldId, newId):
        if self.CheakUser(oldId):
            for u in self.listOfUser:
                if u.Id == oldId:
                    u.Id = newId
                    self.copyToFileUser(self.listOfUser)
                    print(
                        "******************************* User Updated 😘 *******************************")
        else:
            print("Not Found")

    def Searching_Books(self, Id):
        for bo in self.List_Of_Book:
            if bo.Id == Id:
                if bo.Available == True:
                    return True

    def Show_Books(self):
        print("------------------------------------------List of Books------------------------------------------------------\n"
              "Book Id:         Book Name:         Book Author:       Book Edition:      Book Price:         Book Available:\n")
        for bo in self.List_Of_Book:
            print(bo)

    def Show_Issued_Books(self):
        print(
            "---------------------------List of Issued Books------------------------------\n"
            "Book Id:       Book Name:        User Id:      Data Issue:      Data Return: \n")
        for bo in self.List_Of_Issue_Books:
            print(bo)

    def Copy_To_File(self, List_OF_Book):
        Write_In_File = open("books.txt", "w")
        for b in List_OF_Book:
            Write_In_File.write(str(b))

    def copyToFileUser(self, listOFuser):
        Write_In_File = open("user.txt", "w")
        for u in listOFuser:
            Write_In_File.write(str(u))

    def CheakBook(self, Id):
        cheak = False
        for b in self.List_Of_Book:
            if b.Id == Id:
                cheak = True
        return cheak

    def CheakUser(self, Id):
        cheak = False
        for u in self.listOfUser:
            if u.Id == Id:
                cheak = True
        return cheak


class Student(user):

    def __init__(self, Name, Id, Address):
        super().__init__(Name, Id, Address)

    def Issue_Books(self, ID, Date_Issue, Return_Date):
        if self.CheakBook(ID):
            for b in self.List_Of_Book:
                if b.Available == True:
                    if b.Id == ID:
                        b.Available = False
                        self.Copy_To_File(self.List_Of_Book)
                        i = Issue_Book(b.Name, Date_Issue,
                                       Return_Date, self.Id, ID)
                        self.List_Of_Issue_Books.append(i)
                        self.Copy_To_File_Issue_Book(self.List_Of_Issue_Books)
                        print(
                            "******************************* Book Issued 😘 *******************************")
                else:
                    print("Not Available")
        else:
            print("Not Found")

    def Return_Books(self, Id, Date_Issue, Return_Date):
        if self.CheakBook(Id):

            for i in self.List_Of_Issue_Books:
                if self.Id == i.User_Id:
                    if i.Book_Id == Id:
                        self.List_Of_Issue_Books.remove(i)
                        self.Copy_To_File_Issue_Book(self.List_Of_Issue_Books)
            for bo in self.List_Of_Book:
                if self.Id == i.User_Id:
                    if bo.Id == Id:
                        bo.Available = True
                        self.Copy_To_File(self.List_Of_Book)
                        print(
                            "******************************* Book Returned 😘 *******************************")
        else:
            print("Not Found")

    def Show_Issued_Books(self):
        print(
            "---------------------------List of Issued Books------------------------------\n"
            "Book Id:       Book Name:        User Id:      Data Issue:      Data Return: \n")
        for b in self.List_Of_Issue_Books:
            if b.User_Id == self.Id:
                print(b)

    def Show_Books(self):
        print("------------------------------------------List of Books-----------------------------------------------------\n"
              "Book Id:         Book Name:         Book Author:       Book Edition:      Book Price:         Book Available:\n")
        for b in self.List_Of_Book:
            print(b)

    def Copy_To_File(self, List_OF_Book):
        Write_In_File = open("books.txt", "w")
        for b in List_OF_Book:
            Write_In_File.write(str(b))

    def Copy_To_File_Issue_Book(self, List_OF_Issue_Book):
        Write_In_File = open("Issue_Book.txt", "w")
        for b in List_OF_Issue_Book:
            Write_In_File.write(str(b))

    def CheakBook(self, Id):
        cheak = False
        for b in self.List_Of_Book:
            if b.Id == Id:
                cheak = True
        return cheak


print("******************************************************************************************************************")
print("************************************ Welcome To The Library Management System ************************************")
print("******************************************************************************************************************")
print("************************************ Project DONE BY Eng.Belal.s.El_Radei 😉 ***********************************")
print("******************************************************************************************************************")

a = input("PRESS ENTER TO CONTINUE 💛 :")
a = str(a)
if a.isalpha():
    pass

user = " "
while user != "":

    user = input(
        "Welcome, Please Select Is 'Admin'/'A' Or 'Student'/'S': ").capitalize().strip()
    if user == "Admin" or user == "A":
        Name_user = input("Please Enter UserName: ").lower().strip()
        password = input("Please Enter PassWord: ")
        if Name_user == "belal" and password == "0000":
            Admin = admin("Belal", "0000", "Gaza")
            print("Welcome Eng.", Admin.Name, "❤")
            print("What service do you want?🤔 ")
            print("1.  Add Books ✅",
                  "2.  Update Book 🔁",
                  "3.  Delete Books ❎",
                  "4.  Searching Books",
                  "5.  Show Books",
                  "6.  Show Issued Books",
                  "7.  Add User",
                  "8.  Update User",
                  "9.  Delete User",
                  "10. Display Users",
                  "11. Exit", sep="\n")

            service = 0
            while service != 11:
                print()
                service = int(input("Enter Number of Service : "))
                print()
                if service == 1:
                    Name = input("Enter Name of Book: ")
                    Id = int(input("Enter Id of Book: "))
                    author = (input("Enter Author of Book: "))
                    edition = int(input("Enter Edition of Book: "))
                    prices = int(input("Enter Price of Book: "))
                    Admin.Add_Books(Id, Name, author, edition, prices)

                elif service == 2:
                    oldId = int(input("Enter Old Id of Book: "))
                    newId = int(input("Enter New Id of Book: "))
                    Admin.Update_Book(oldId, newId)

                elif service == 3:
                    Id = int(input("Enter Id of Book: "))
                    Admin.Delete_Books(Id)

                elif service == 4:
                    Id = int(input("Enter Id of Book: "))
                    if Admin.Searching_Books(Id):
                        print("Available")
                    else:
                        print("Not Available")
                elif service == 5:
                    print()
                    Admin.Show_Books()

                elif service == 6:
                    print()
                    Admin.Show_Issued_Books()

                elif service == 7:
                    Name = input("Please Enter your User Name: ")
                    Id = int(input("Please Enter your User Id: "))
                    Address = input("Please Enter your User Address: ")
                    Admin.Add_User(Name, Id, Address)

                elif service == 8:
                    oldId = int(input("Please Enter your Old User Id: "))
                    newId = int(input("Please Enter your New User Id: "))
                    Admin.Update_User(oldId, newId)
                elif service == 9:
                    Id = int(input("Please Enter your User Id: "))
                    Admin.Delete_User(Id)

                elif service == 10:
                    print()
                    Admin.Display_Users()
                    print()
        else:
            print("Error !!")
            print("Please Enter The Correct User Name And Password")

    elif user == "Student" or user == "S":
        Id = int(input("Please Enter Your ID: "))
        for u in Admin.listOfUser:
            if u.Id == Id:
                print("Welcome", u.Name)
                print("What Service Do You Want? 🤔 ")
                print("1. Issue Books",
                      "2. Return Books",
                      "3. Show Issued Books",
                      "4. Show Books",
                      "5. Exit", sep="\n")
                service = 0
                while service != 5:
                    print()
                    service = int(input("Enter Number Of Service : "))
                    print()
                    if service == 1:
                        Id = int(input("Enter ID Of Book: "))
                        Date_Issue = (input("Enter Date Issue of Book: "))
                        Return_Date = (input("Enter Return Date of Book: "))
                        u.Issue_Books(Id, Date_Issue, Return_Date)

                    elif service == 2:
                        Id = int(input("Enter Id of Book: "))
                        Date_Issue = (input("Enter Date Issue of Book: "))
                        Return_Date = (input("Enter Return Date of Book: "))
                        u.Return_Books(Id, Date_Issue, Return_Date)

                    elif service == 3:
                        print()
                        u.Show_Issued_Books()
                        print()
                    elif service == 4:
                        print()
                        u.Show_Books()
                        print()
