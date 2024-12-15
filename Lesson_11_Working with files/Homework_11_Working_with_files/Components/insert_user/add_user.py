from ..user_data import user_data
from .save_user import save_users

def add_user(users,file_name):
        number = input("Enter the user's number: ")
        user_name = input("Enter the user's first name: ")
        family_name = input("Enter the user's last name: ")
        user_city = input("Enter the user's city: ")
        user_country = input("Enter the user's country: ")

        user_data(users,number,user_name,family_name,user_city,user_country)

        save_users(users,file_name)

        print("User inserted and data saved.")