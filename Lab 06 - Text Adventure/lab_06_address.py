
class Address:
    def __init__(self):
        self.name = ""
        self.line1 = ""
        self.line2 = ""
        self.city = ""
        self.state = ""
        self.zip = ""
def main():
        home_address = Address()

        home_address.name = "Chaerin Yeom"
        home_address.line1 = "1234 S. hey Street"
        home_address.line2 = "Hello building"
        home_address.city = "Very City"
        home_address.state = "CR"
        home_address.zip = "12345"

        # create another address
        vacation_home_address = Address()

        # Set the fields in the address
        vacation_home_address.name = "Chaerin Yeom"
        vacation_home_address.line1 = "4321 OK Street"
        vacation_home_address.line2 = "Goodbye building"
        vacation_home_address.city = "Almost City"
        vacation_home_address.state = "CC"
        vacation_home_address.zip = "54321"

        print("The Chaerin's main home is in " + home_address.city)
        print("Her vacation home is in " + vacation_home_address.city)

main()

