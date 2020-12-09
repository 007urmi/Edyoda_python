# -*- coding: utf-8 -*-
from Catalog import Catalog 
from Book import Book

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issued_book = []
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    def availableBooks(self,Catalog):
        print("Available books are:")
        Catalog.displayAllBooks()
    
    #assume name is unique
    def issueBook(self,name,Catalog,days=10):
        book = Catalog.searchByName(name)
        
        if len(book.book_item) > 0:
            b1= book.book_item[0]
            self.issued_book.append(b1)
            Catalog.removeBookItem(name,b1.isbn)
            print(name ,"book is isssued")
        else:
            print("Book is not available")
    
    #assume name is unique
    def returnBook(self,name,Catalog):
        book = Catalog.searchByName(name)
        for self.items in self.issued_book:
            if book.book_item in self.issued_book:
                b2 = book.book_item
                self.issued_book.remove(book.book_item)
                Catalog.addBookItem(book,b2.isbn,b2.rack)
            print(name,"Book is returned")


        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        self.book2 = []

    def __repr__(self):
        return self.name +  ' ' + self.location + ' ' + self.emp_id
    
    def addBook(self,name,author,publish_date,pages,Catalog):
        b3 = Catalog.addBook(name,author,publish_date,pages)
        self.book2.append(b3)
        print("A book is added by Librarian")
        return b3
    
    def addBookItem(self,book,isbn,rack,Catalog):
        Catalog.addBookItem(book,isbn,rack)
        print("Details of the book is added")
    
    
    def displayAddedBook(self,Catalog):
        Catalog.displayAllBooks()

    
    def removeBook(self,name,Catalog):
        Catalog.removeBook(name)
        Catalog.different_book_count -=1
        print ("Book removed")

    
    def removeBookItemFromCatalog(self,Catalog,name,isbn):
        Catalog.removeBookItem(name,isbn)
    
    
        
