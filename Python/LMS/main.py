import json

class Book:
    
    def __init__(self,name,author=None,type=None):
        self.name=name
        self.author=author
        self.type=type

class Member:
    
    def __init__(self,name,member_id=None):
        self.name=name
        self.member_id=member_id


class Library():
    
    def addBook(self,book):
        file=open('LMS/books.txt','a')
        file.write(book.name+'*'+book.author+'*'+book.type+'\n')
        file.close()
    
    def displayBooks(self):
        file=open('LMS/books.txt','r')
        for line in file:
            data=line.strip().split('*')
            print('Book Name: ',data[0])
            print('Book Author: ',data[1])
            print('Book Type: ',data[2])
            print('\n')
    
    def removeBook(self,book):
        file=open('LMS/books.txt','r')
        books=[]
        for line in file:
            data=line.strip().split('*')
            if data[0]==book.name:
                print('Book removed successfully')
            else:
                books.append(line)
        file.close()
        file=open('LMS/books.txt','w')
        for book in books:
            file.write(book)
        file.close()

    def addMember(self,member):
        file=open('LMS/members.txt','a')
        file.write(member.name+'*'+member.member_id+'\n')
        file.close()
        
    def removeMember(self,member):
        file=open('LMS/members.txt','r')
        members=[]
        for line in file:
            data=line.strip().split('*')
            if data[0]==member.name:
                print('Member removed successfully')
            else:
                members.append(line)
        file.close()
        file=open('LMS/members.txt','w')
        for member in members:
            file.write(member)
        file.close()

    def searchBook(self,book):
        file=open('LMS/books.txt','r')
        a=0
        for line in file:
            a+=1
            data=line.strip().split('*')
            if data[0]==book.name:
                print('Book Found Index: ',a)
                break
        else:
            print('Book not found')
        file.close()

lib=Library()
print('\n\n ##### Library Management System ##### \n\n')
while True:
    print('1. Add Book \n2. Display Book \n3. Remove Book \n4. Add Member \n5. Remove Member \n6. Search Book \n7. Exit')
    choice=input('Enter your choice: ')
    match choice:
        case '1':
            print('Add Book')
            name=input('Enter book name: ')
            author=input('Enter book author: ')
            type=input('Enter book type: ')
            b1=Book(name,author,type)
            lib.addBook(b1)
        case '2':   
            lib.displayBooks()
        case '3':
            print('Remove Book')
            name=input('Enter book name: ')
            b1=Book(name)
            lib.removeBook(b1)
        case '4':
            print('Add Member')
            name=input('Enter member name: ')
            member_id=input('Enter member id: ')
            m1=Member(name,member_id)
            lib.addMember(m1)
        case '5':
            print('Remove Member')
            name=input('Enter member name: ')
            m1=Member(name)
            lib.removeMember(m1)
        case '6':
            print('Search Book')
            name=input('Enter book name: ')
            b1=Book(name)
            lib.searchBook(b1)
        case '7':
            print('Exiting the program')
            break
        case _:
            print('Invalid choice')