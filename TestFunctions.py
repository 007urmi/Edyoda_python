# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

#b1 = Book('Shoe Dog','Phil Knight', '2015',312)
#b1.addBookItem('123hg','H1B2')
#b1.addBookItem('124hg','H1B3')

#b1.printBook()

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '124hg','H1B4')
catalog.addBookItem(b, '125hg','H1B5')

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(b, '463hg','K1B2')

b = catalog.addBook('Pax','Sara Pennypacker', '2017', 288)
catalog.addBookItem(b,'554jk','M24A')
catalog.addBookItem(b,'556jk','M25A')
catalog.addBookItem(b,'557jk','M26A')
#catalog.displayAllBooks()



# #member
# m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')
# m1.availableBooks(catalog)
# print (m1)
# #print (librarian)




# m1.issueBook('Moonwalking with Einstien',catalog)
# m1.returnBook('Moonwalking with Einstien',catalog)


#

# catalog.displayAllBooks()

#b = catalog.searchByName('Shoe Dog')
#print (b)

#b = catalog.searchByAuthor('J Foer')
#print(b)

catalog.removeBookItem('Shoe Dog','124hg')
catalog.removeBook('Shoe Dog')
catalog.displayAllBooks()

# #reference to Librarian class object
# librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 

# # adding a book by librarian
# b2 =librarian.addBook("This is Going to Hurt: Secret Diaries of a Junior Doctor","Adam Key",'2017', 302,catalog)
# #adding details
# librarian.addBookItem(b2,'234c','l203',catalog)

# #displaying all the books till now added
# librarian.displayAddedBook(catalog)

# #library remove book
# librarian.removeBook('Shoe Dog')
# #displaying book after removing
# librarian.displayAddedBook(catalog)

