# 📚 TBR Library Manager

A simple Python class to manage your personal **To-Be-Read (TBR)** book list.

## ✨ Features

- 📥 Add books to your TBR list  
- 🗑️ Remove books from the list  
- 📃 Display all books with a total count  

## 🧾 Class Overview

### `Library`

#### Methods:
- `add(book_name)`  
  Adds a new book to your TBR list.

- `remove(book_name)`  
  Removes the specified book from your list.

- `show()`  
  Prints all books in your TBR list along with the total number.

## 🧪 Example Usage

```python
from library import Library

p1 = Library()
p1.add("48 Laws of Power")
p1.show()
p1.remove("48 Laws of Power")
p1.show()
