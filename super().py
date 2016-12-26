class Person():
    def __init__(self,name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        self.email = email
    
bob = EmailPerson('Bob Frapples','bob@frapples.com')

print bob.name
print bob.email