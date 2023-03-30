from typing import List
from datetime import datetime

class Person:
    def __init__(self, name: str, age: int, address: str, phone: str):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

class Employee(Person):
    def __init__(self, name: str, age: int, address: str, phone: str, salary: float):
        super().__init__(name, age, address, phone)
        self.salary = salary

class Author:
    def __init__(self, name: str, last_name: str):
        self.books = []
        self.name = name
        self.last_name = last_name

class Customer(Person):
    def __init__(self, name: str, age: int, address: str, phone: str, debt: float = 0):
        super().__init__(name, age, address, phone)
        self.debt = debt

class Book:
    def __init__(self, id: int, title: str, author: Author, isbn: str, publisher: str, price: float, quantity_available: int, quantity_sold: int = 0):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.price = price
        self.quantity_available = quantity_available
        self.quantity_sold = quantity_sold

class Sale:
    def __init__(self, id: int, date: datetime, customer: Customer, books: List[Book], total: float):
        self.id = id
        self.date = date
        self.customer = customer
        self.books = books
        self.total = total

class Library:
    def __init__(self):
        self.books = []
        self.customers = []
        self.employees = []

    def registerSale(self, sale: Sale):
        # updates sales and stock records
        for book in sale.books:
            book.quantity_available -= 1
            book.quantity_sold += 1
        self.customers.append(sale.customer)

    def registerBook(self, book: Book):
        # adds a new book to the inventory
        self.books.append(book)

    def registerCustomer(self, customer: Customer):
        # adds a new customer to the database
        self.customers.append(customer)

    def searchBook(self, id: int) -> Book:
        # searches for a book by its id and returns it
        for book in self.books:
            if book.id == id:
                return book

    def searchCustomer(self, name: str) -> Customer:
        # searches for a customer by their name and returns them
        for customer in self.customers:
            if customer.name == name:
                return customer

    def searchEmployee(self, name: str) -> Employee:
        # searches for an employee by their name and returns them
        for employee in self.employees:
            if employee.name == name:
                return employee

    def addEmployee(self, employee: Employee):
        # adds a new employee to the staff
        self.employees.append(employee)
