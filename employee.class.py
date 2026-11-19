class Employee:

    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

employee1 = Employee('Bram', 'Neij', 'aaaaaaa')
print(employee1.first)