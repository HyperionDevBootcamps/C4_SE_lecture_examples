#Create a House class 

class House(object):
    # Declare class variables
    is_locked = True
    tenant =[]
    # Create constructor method to initialise instance variables
    def __init__(self, address, bedrooms, bathroom, rent):
        self.address = address
        self.bedrooms = bedrooms
        self.bathroom = bathroom
        self.rent = rent

    # Create method to lock the house 
    def locked(self):
        self.is_locked = True
        print(f"The house at {self.address} is locked")
        
    # Create method to unlock the house
    def unlocked(self):
        self.is_locked = False
        print(f"The house at {self.address} is unlocked")
    
    #Create method to check who is the tenant of the house
    def check_tenant(self):
        print(f"The tenant at {self.address} is ",end="")
        for person in self.tenant:
            print(person)
      

# Create a person class 
class Person(object):
    qualify = False
    is_signed = False
# Create a constructor method to initialise instance variables
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method to determine if the person qualifies to rent a house based on a salary check
    def salary_check(self, House):
        if self.salary > House.rent:
            self.qualify = True
            print(f"{self.name} qualifies to rent house at {House.address}")
        else:
            self.qualify = False
            print(f"{self.name} does not qualify to rent house at {House.address}")
    
    # Method to confirm that the contract has been signed
    def contract_signed(self):
        self.is_signed = True
        print(f"{self.name} has signed the contract")

    # Method to determine who moves into the house based on a salary check
    def move_into_house(self, House):
        if self.qualify == True and self.is_signed == True:
            House.tenant.append(self.name)
            print(f"{self.name} has moved into {House.address}")
        else:
            print(f"{self.name} has not moved into {House.address}")



def main():
    # Create objects of the House class
    house1 = House("123 4th street", 2, 1, 2000)

    # Call the locked/unlocked method on the objects
    house1.locked()
    house1.unlocked()

    # Create object of the Person class
    person1 = Person("Clare", 1800)  
    person2 = Person("Sam", 4000)

    #Call salary_check method on person object
    person1.salary_check(house1)
    person2.salary_check(house1)
    

    #Call signed_contract method on person2
    person1.contract_signed()
    person2.contract_signed()
    
    
    # Call move_into_house method on person object
    person1.move_into_house(house1)
    person2.move_into_house(house1)
    

    # Call the tenants_check method on house object
    house1.check_tenant()


main()    