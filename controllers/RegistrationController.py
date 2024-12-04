from controllers.Utils import hash_password
from models.User import User
from views.RegistrationView import RegistrationView
from models.enums import GenderEnum
class RegistrationController:
    def __init__(self, login_controller):
        self.login_controller = login_controller
        self.registration_view = RegistrationView(self)

    def add_user(self, email, full_name, age, gender, height, weight, shoe_size, password, confirm_password):
        if not all([email, full_name, age, gender, height, weight, shoe_size, password, confirm_password]):
            self.registration_view.message_box("Error", "Please fill in all fields.")
            return

        if '@' not in email or '.' not in email.split('@')[-1]:
            self.registration_view.message_box("Error", "Invalid email.")
            return

        if password != confirm_password:
            self.registration_view.message_box("Error", "Passwords do not match.")
            return

        if not str(age).isnumeric() or int(age) < 0 or int(age) > 120:
            self.registration_view.message_box("Error", "Invalid age.")
            return

        if not str(height).isnumeric() or int(height) < 0 or int(height) > 300:
            self.registration_view.message_box("Error", "Invalid height.")
            return

        if not str(weight).isnumeric() or int(weight) < 0 or int(weight) > 300:
            self.registration_view.message_box("Error", "Invalid weight.")
            return

        if not str(shoe_size).isnumeric() or int(shoe_size) < 0 or int(shoe_size) > 50:
            self.registration_view.message_box("Error", "Invalid shoe size.")
            return

        password_hash = hash_password(password)

        if gender == 'MALE':
            gender = GenderEnum.MALE.value
        else:
            gender = GenderEnum.FEMALE.value
        try:
            User(int(age), email, full_name, gender, int(height), False, password_hash, int(shoe_size), int(weight)).create_user()
            self.registration_view.message_box("Success", "User registered successfully.")
            self.back_to_login()
        except Exception as e:
            self.registration_view.message_box("Error", f"Error registering user: {str(e)}")
            return

    def open_registration(self):
        self.registration_view.root.deiconify()
    
    def back_to_login(self):
        self.registration_view.root.withdraw()
        self.login_controller.view.root.deiconify()
