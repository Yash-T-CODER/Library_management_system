class Library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]
    def add(self,new):
        (self.books).append(new)
        print("Your  selected book has been added in your tbr list")
    def remove(self,remo):
       
        (self.books).remove(remo)
        print("Your  selected book has been removed  from your tbr list")

    def show(self):
       print(f"Your tbr list is\n{self.books}")
       print(f"Your tbr list has {len(self.books)} no. of books")
p1=Library()
p1.add("48 llaws of power ")
p1.show()