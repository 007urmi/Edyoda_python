from Book import Book
from Catalog import Catalog
from User import Member, Librarian

catalog = Catalog()


#reference to Librarian class object
librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
#details of librarian
print (librarian)
# adding a book by librarian
b2 =librarian.addBook("This is Going to Hurt: Secret Diaries of a Junior Doctor","Adam Key",'2017', 302,catalog)
#adding details
librarian.addBookItem(b2,'234c','l203',catalog)

#displaying all the books till now added
librarian.displayAddedBook(catalog)

#library remove book
librarian.removeBook('Shoe Dog',catalog)


librarian.addBookItem(b2,'235c','1204',catalog)

librarian.removeBookItemFromCatalog(catalog,"This is Going to Hurt: Secret Diaries of a Junior Doctor",'235c')