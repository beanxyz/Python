print ("Welcome to the Student Management Program")
import pickle
class Student:
    def __init__ (self, name, age, gender):
         self.name   = name
         self.age    = age
         self.gender = gender




a =[];
while True:

    choice = int(input("Make a Choice: "))
    if (choice==1):

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        sex = input("Enter Sex: ")

        s = Student(name, age, sex)
        a.append(s)

    elif(choice==2):

        pickle.dump(a, open('file', 'wb'))

    elif(choice==3):

        for item in a:
            print(item.name,item.age,item.gender)

    elif (choice==4):

        fp = pickle.load(open('file', 'rb'))
        print(fp)
        for item in fp:
            print(item.name)




