import time 

# Class User
# ****************

class User:
    # Define an attribute called login_attempts to your User class.
    
 
    def __init__(self, first_name , last_name):
        self.first_name  = first_name 
        self.last_name = last_name
        # Add an other attribute 
        self.id = id(self)
        self.y_o_b = '1992'
        self.login_attempts = 0

# Define a method called describe_user() that prints a summary of the user’s information.
        
    def describe_user(self):
        print(f"The First name of User is {self.first_name} ")
        print(f"The Last name of User is {self.last_name} ")
        print(f"The ID of User is {self.id} ")
        print(f"The Year of Birth of User is {self.y_o_b} ")

# Define a another method called greet_user() that prints a personalized greeting to the user.
    def greet_user(self):
      print(f"Welcome {self.first_name} , we are so happy to meeting U")

# Define a method called increment_login_attempts() that increments the value of login_attempts by 1.
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"The {self.first_name} try to login .  after {self.login_attempts} attempet")

# Define another method called reset_login_attempts() that resets the value of login_attempts to 0.
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"reseting login for  {self.first_name.title()} ")

# Create several instances representing different users, and call both methods for each user.
A = User('Alaa','Marashdeh')
B = User('Jana','Snajleh')
C = User('Walaa','AL-Ahmad')

# users = [ A , B , C]
# for user in users:
#     user.greet_user()
#     user.describe_user()

user_longins = [(A,5), (B,3),(C,1)]
for login in user_longins:
    user , n_login = login
    user.describe_user()
    for n in range(n_login):
        if user.login_attempts <= 2:
            print("loging in ")
            time.sleep(1)
            user.increment_login_attempts()

        else :
            print("Maximam lonin attemps is reach, looking around 5 secound")
            time.sleep(5)
            user.reset_login_attempts()


# A.describe_user()
# A.greet_user()
# B.describe_user()
# B.greet_user()

# A.increment_login_attempts()
# B.increment_login_attempts()
# A.increment_login_attempts()
# A.increment_login_attempts()
# B.increment_login_attempts()

# A.reset_login_attempts()
# B.reset_login_attempts()

# A.increment_login_attempts()
# B.increment_login_attempts()

