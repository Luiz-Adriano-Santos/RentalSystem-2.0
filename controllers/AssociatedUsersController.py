from models.UserAssociated import UserAssociated
from views.UserEditView import UserEditView
from views.RegisterAssociatedUserView import RegisterAssociatedUserView
from views.UsersView import UsersView


class AssociatedUsersController:
    def __init__(self, controller):
        self.controller = controller
        self.view = None

    def associated_users_page(self, user):
        associated_users = UserAssociated.get_associated_users(user.email)
        is_associated_users = True
        self.view = UsersView(self, user, associated_users, is_associated_users, )
        self.view.mainloop()

    def create_associated_user_view(self, user):
        self.view.root.withdraw()
        self.view = RegisterAssociatedUserView(self, user)
        self.view.mainloop()

    def return_guest_home(self, user):
        self.view.root.withdraw()
        self.controller.guest_page(user)

    def create_associated_user(self, logged_user, user_data):
        full_name = user_data["full_name"]
        age = user_data["age"]
        gender = user_data["gender"]
        height = user_data["height"]
        weight = user_data["weight"]
        shoe_size = user_data["shoe_size"]
        parent_user_email = logged_user.email

        if not all([full_name, age, gender, height, weight, shoe_size]):
            self.view.show_message("Error", "Please fill in all fields.")
            return

        if not str(age).isnumeric() or int(age) < 0 or int(age) > 120:
            self.view.show_message("Error", "Invalid age.")
            return

        if not str(height).isnumeric() or int(height) < 0 or int(height) > 300:
            self.view.show_message("Error", "Invalid height.")
            return

        if not str(weight).isnumeric() or int(weight) < 0 or int(weight) > 300:
            self.view.show_message("Error", "Invalid weight.")
            return

        if not str(shoe_size).isnumeric() or int(shoe_size) < 0 or int(shoe_size) > 50:
            self.view.show_message("Error", "Invalid shoe size.")
            return

        try:
            UserAssociated(parent_user_email, full_name, gender, shoe_size, age, weight, height).create_associated_user()
            self.view.show_message("Success", "Associated User registered successfully.")
            self.view.root.withdraw()
            self.associated_users_page(logged_user)
        except Exception as e:
            self.view.show_message("Error", f"Error registering user: {str(e)}")
            return

    def update_associated_user(self, logged_user, editing_user, user_data):
        full_name = user_data["full_name"]
        age = user_data["age"]
        gender = user_data["gender"]
        height = user_data["height"]
        weight = user_data["weight"]
        shoe_size = user_data["shoe_size"]

        if not all([full_name, age, gender, height, weight, shoe_size]):
            self.view.show_message("Error", "Please fill in all fields.")
            return

        if not str(age).isnumeric() or int(age) < 0 or int(age) > 120:
            self.view.show_message("Error", "Invalid age.")
            return

        if not str(height).isnumeric() or int(height) < 0 or int(height) > 300:
            self.view.show_message("Error", "Invalid height.")
            return

        if not str(weight).isnumeric() or int(weight) < 0 or int(weight) > 300:
            self.view.show_message("Error", "Invalid weight.")
            return

        if not str(shoe_size).isnumeric() or int(shoe_size) < 0 or int(shoe_size) > 50:
            self.view.show_message("Error", "Invalid shoe size.")
            return

        editing_user.update_associated_user(user_data)
        self.view.show_message("Success", "User updated successfully.")
        self.view.root.withdraw()
        self.associated_users_page(logged_user)

    def delete_user(self, logged_user, user):
        user.delete_associated_user()
        self.view.show_message("Success", "User deleted successfully.")
        self.view.root.withdraw()
        self.associated_users_page(logged_user)


    def open_associated_user_edit_page(self, logged_user, user):
        self.view.root.withdraw()
        self.view = UserEditView(self, logged_user, user, is_associated_user=True)
        self.view.mainloop()
        
    def get_all_associated_users(self, user):
        associated_users = UserAssociated.get_associated_users(user.email)
        return [user_associated.full_name for user_associated in associated_users]