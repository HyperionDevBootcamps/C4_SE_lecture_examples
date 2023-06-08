# Create a House class
class House:
    # Class variable
    city = "London"
    garden = False
    # Create a constructor
    def __init__(self,address,type,bedrooms,bathrooms,rent):
        #Define instance variables
        self.address = address
        self.type = type
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.rent = rent   

    #Create methods
    def has_garden(self):
        self.garden = True
        print("This house has a garden")

    def has_no_garden(self):
        self.garden = False
        print("This house does not have a garden")

#Create the main function
def main():
    #Create objects of the house class
    house1 = House("123 4th ave","simplex",3, 2, 3000)
    house2 = House("567 8th ave", "flat",2, 1, 1000)

    #print(house1.address)
    
    print(house1.type)
    print(house2.type)
    print(house1.city)
    print(house2.city)

    #Call the methods on the objects
    house1.has_garden()

main()