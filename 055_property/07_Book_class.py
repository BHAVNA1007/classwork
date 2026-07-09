#07_Book_class

'''
wap to create class named Book have varible bookno (read only), bookname, bookwriter.  and use here property deleter

'''  

class Book:

    def __init__(self, book_no, book_name, book_writer):

        self.__book_no = book_no
        self.__book_name = book_name
        self.__book_writer = book_writer

    @property
    def book_no(self):
        return self.__book_no

    @property
    def book_name(self):
        return self.__book_name

    @book_name.setter
    def book_name(self, book_name):
        self.__book_name = book_name

    @book_name.deleter
    def book_name(self):
        del self.__book_name

    @property
    def book_writer(self):
        return self.__book_writer

    @book_writer.setter
    def book_writer(self, book_writer):
        self.__book_writer = book_writer

    @book_writer.deleter
    def book_writer(self):
        del self.__book_writer

b = Book(10001, "la la land", "xyz")
print(b.book_no)
print(b.book_name)
print(b.book_writer)

'''
output:

10001
la la land
xyz
'''

del b.book_name
#print(b.book_name)

'''
AttributeError: 'Book' object has no attribute '_Book__book_name'. Did you mean: '_Book__book_no'?

'''

del b.book_writer
#print(b.book_writer)
'''
AttributeError: 'Book' object has no attribute '_Book__book_writer'
'''

