from controllers.EquipmentsController import EquipmentsController
from controllers.AssociatedUsersController import AssociatedUsersController
from controllers.RegisteredUsersController import RegisteredUsersController
from views.EmployeeHomeView import EmployeeHomeView
from views.GuestHomeView import GuestHomeView
from controllers.RequestDetailsController import RequestDetailsController
from models.Request import Request
from models.enums import StatusEnum
from datetime import datetime
from DAOs.RequestDAO import RequestDAO

class HomeController:
    def __init__(self, login_controller, user):
        self.login_controller = login_controller
        self.logged_employee = user

    def open_employee_home_page(self, user):
        self.view = EmployeeHomeView(self, user)
        self.view.mainloop()
    
    def open_guest_home_page(self, user):
        self.view = GuestHomeView(self, user)
        self.view.mainloop()

    def open_equipments_page(self):
        equipments_controller = EquipmentsController(self.login_controller)
        equipments_controller.equipments_page(self.logged_employee)

    def logout(self):
        self.view.root.withdraw()
        self.login_controller.reset_login_fields() 
        self.login_controller.view.root.deiconify()

    def open_registered_users_page(self, user):
        registered_users_controller = RegisteredUsersController(self.login_controller)
        registered_users_controller.registered_users_page(user)

    def open_associated_users_page(self, user):
        associated_users_controller = AssociatedUsersController(self.login_controller)
        associated_users_controller.associated_users_page(user)
    
    def open_guest_edit_page(self, user):
        registered_users_controller = RegisteredUsersController(self.login_controller)
        registered_users_controller.guest_edit_page(user)

    def open_request_details_page(self, request, user):
        self.view.root.withdraw()
        RequestDetailsController(self, request, user, self.logged_employee)

    def get_usersAssociated(self, user):
        return AssociatedUsersController.get_all_associated_users(self, user)
      
    def register_request(self, for_who, sport, includes_skis, includes_boots, includes_helmet, user):
        
        if not sport:
            GuestHomeView.message_box('Error', 'select at least 1 sport in the (SPORT) field')
            return
        if not for_who:
            GuestHomeView.message_box('Error', 'select at least 1 person in the (FOR WHO) field')
            return
        
        if (for_who != user.full_name):
            associatedName = for_who
        else:
            associatedName = None
        
        if (includes_skis == 1):
            if sport == 'SKI':
                includes_skis = "Skis Requested"
            else:
                includes_skis = "Board Requested"
        else:
            includes_skis = "Not Requested"
        
        if (includes_boots == 1):
            includes_boots = "Requested"
        else:
            includes_boots = "Not Requested"
        
        if (includes_helmet == 1):
            includes_helmet = "Requested"
        else:
            includes_helmet = "Not Requested"

        timestamp = datetime.now().strftime('%m/%d/%Y - %I:%M %p')
        try:
            Request(StatusEnum.SENT.value, sport, timestamp, user, includes_boots, includes_helmet, includes_skis, associatedName).create_request()
            GuestHomeView.message_box('Success', 'Order placed successfully, collect your equipment if necessarie from the employee!')
        except Exception as e:
            GuestHomeView.message_box('Error', 'An error occurred while trying to register the request')
    
    def get_requests(self):
        return RequestDAO().get_requests()