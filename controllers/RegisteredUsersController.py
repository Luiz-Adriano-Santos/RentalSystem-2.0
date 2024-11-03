from controllers.Utils import hash_password
from models.User import User
from views.EmployeeUserEditView import EmployeeUserEditView
from views.RegisteredUsersView import RegisteredUsersView
from views.GuestEditView import GuestEditView

class RegisteredUsersController:
    def __init__(self, controller):
        self.controller = controller
        self.view = None

    def registered_users_page(self, user):
        users = user.get_all_users()
        self.view = RegisteredUsersView(self, users)
        self.view.mainloop()

    def open_employee_user_edit_page(self, user):
        self.view.root.withdraw()
        self.view = EmployeeUserEditView(self, user)
        self.view.mainloop()

    def guest_edit_page(self, user):
        self.view = GuestEditView(self, user)  
        self.view.mainloop()

    def return_employee_home(self):
        self.view.root.withdraw()
        self.controller.employee_page()
    
    def return_guest_home(self, user):
        self.view.root.withdraw()
        self.controller.guest_page(user)

    def update_user_as_employee(self, user, full_name, new_password, password_confirmation, gender, shoe_size, age,
                    is_employee, weight, height):
        if self.update_user(user, full_name, new_password, password_confirmation, gender, shoe_size, age,
                        is_employee, weight, height):
            self.registered_users_page()

    def update_user_as_guest(self, user, full_name, new_password, password_confirmation, gender, shoe_size, age, weight, height):
        if self.update_user(user, full_name, new_password, password_confirmation, gender, shoe_size, age, user.is_employee, weight, height):
            self.return_guest_home(user)

    def update_user(self, user, full_name, new_password, password_confirmation, gender, shoe_size, age, is_employee, weight, height):
        if not full_name or not gender or not age or not shoe_size or not weight or not height:
            self.view.show_message("Error", "All fields (except password) are required.")
            return False

        if not isinstance(age, int) or age <= 0:
            self.view.show_message("Error", "Age must be a positive integer.")
            return False

        if not isinstance(shoe_size, int) or shoe_size <= 0:
            self.view.show_message("Error", "Shoe size must be a positive number.")
            return False

        if not isinstance(weight, int) or weight <= 0:
            self.view.show_message("Error", "Weight must be a positive number.")
            return False

        if not isinstance(height, int) or height <= 0:
            self.view.show_message("Error", "Height must be a positive number.")
            return False

        if new_password:
            if new_password != password_confirmation:
                self.view.show_message("Error", "Password confirmation does not match.")
                return False

            password_hash = hash_password(new_password)
        else:
            password_hash = user.password_hash

        user.update_user(full_name, age, gender, height, weight, shoe_size, password_hash, is_employee)
        self.view.show_message("Success", "User updated successfully.")
        self.view.root.withdraw() 
        return True

    def delete_user(self, user):
        user.delete_user()
        self.view.show_message("Success", "User deleted successfully.")
        self.view.root.withdraw()
        self.registered_users_page()