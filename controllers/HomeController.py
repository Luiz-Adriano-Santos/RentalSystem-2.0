from controllers.RegisteredUsersController import RegisteredUsersController
from views.EmployeeHomeView import EmployeeHomeView
from views.GuestHomeView import GuestHomeView
from controllers.RequestDetailsController import RequestDetailsController

class HomeController:
    def __init__(self, login_controller):
        self.login_controller = login_controller

    def open_employee_home_page(self, user):
        self.view = EmployeeHomeView(self, user)
        self.view.mainloop()
    
    def open_guest_home_page(self, user):
        self.view = GuestHomeView(self, user)
        self.view.mainloop()

    def open_equipments_page(self):
        pass

    def logout(self):
        self.view.root.withdraw()
        self.login_controller.reset_login_fields() 
        self.login_controller.view.root.deiconify()

    def open_registered_users_page(self, user):
        registered_users_controller = RegisteredUsersController(self.login_controller)
        self.view.root.withdraw()
        registered_users_controller.registered_users_page(user)
    
    def open_guest_edit_page(self, user):
        registered_users_controller = RegisteredUsersController(self.login_controller)
        registered_users_controller.guest_edit_page(user)

    def open_request_details_page(self, request):
        self.view.root.withdraw()
        RequestDetailsController(self, request)