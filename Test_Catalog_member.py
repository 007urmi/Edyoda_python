from Catalog import Catalog
from User import Member


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

catalog.displayAllBooks()

catalog.removeBook('Pax')


catalog.displayAllBooks()

catalog.removeBookItem('Shoe Dog','124hg')
catalog.displayAllBooks()

b = catalog.searchByName('Shoe Dog')
print (b)

b = catalog.searchByAuthor('J Foer')
print(b)

#member
m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')
m1.availableBooks(catalog)
print (m1)

m1.issueBook('Moonwalking with Einstien',catalog)
m1.returnBook('Moonwalking with Einstien',catalog)


