# Class Restaurant
# ****************

class Restaurant:
 
    def __init__(self, restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type
        # Add an attribute called number_served with a default value of 0
        self.number_served = '0'
        
    def describe_restaurant(self):
        print(f"The name of Restaurant is {self.restaurant_name} ")
        print(f"The cuisine type in the Restaurant is {self.cuisine_type} ")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is OPEN")

    def set_number_served(self,N):

        self.number_served = N
        print(f"The number serve is {self.number_served} is '{N}'.")


    def increment_number_served(self):
        if self.number_served > 0:
            
            self.number_served("0")

            self.number_served += 1
        else:
            print("a day of business.")


# Making an Instance from a Class   
restaurant  = Restaurant('Mac','M')

print(f"The Restaurant name is {restaurant.restaurant_name}.")
print(f"The cuisine type in the Restaurant is {restaurant.cuisine_type} ")

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Calling methods set_number_served
restaurant.set_number_served('66')

# Create three different instances
A = Restaurant('KFS','A')
B = Restaurant ('Moz', 'B')
C = Restaurant ('Pop','C')

# Calling of three different instances
A.describe_restaurant()
B.describe_restaurant()
C.describe_restaurant()

# Making an Instance from a Class   
restaurant  = Restaurant('Mac','M')
print(f"The restaurent {restaurant.restaurant_name} has serve {restaurant.number_served}customers")
restaurant.number_served = '15'
print(f"The restaurent {restaurant.restaurant_name} has serve {restaurant.number_served}customers")

    



