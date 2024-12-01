import bcrypt

from controllers.HomeController import HomeController
from controllers.RegistrationController import RegistrationController
from views.LoginView import LoginView
from views.RoleSelectionView import RoleSelectionView
from DAOs.UserDAO import UserDAO

class LoginController:
    def __init__(self):
        self.view = LoginView(self)

    def handle_login(self, email, password):
        user = UserDAO().get_user(email)
        if user and bcrypt.checkpw(password.encode(), user.password_hash):
            self.view.root.withdraw()
            if user.is_employee:
                RoleSelectionView(self, user).mainloop()
            else:
                self.guest_page(user)
        else:
            self.view.show_message("Login Failed", "Invalid email or password")

    def handle_open_registration(self):
        self.view.root.withdraw()
        registration_controller = RegistrationController(self) 
        registration_controller.open_registration() 

    def run(self):
        self.view.mainloop()

    def guest_page(self, user):
        employee_home_controller = HomeController(self, user)
        employee_home_controller.open_guest_home_page(user)

    def employee_page(self, user):
        employee_home_controller = HomeController(self, user)
        employee_home_controller.open_employee_home_page(user)

    def reset_login_fields(self):
        self.view.email_entry.delete(0, 'end')
        self.view.password_entry.delete(0, 'end')
