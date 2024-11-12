import sqlite3
import pickle
from controllers.EquipmentsController import EquipmentsController
from controllers.AssociatedUsersController import AssociatedUsersController
from controllers.RegisteredUsersController import RegisteredUsersController
from views.EmployeeHomeView import EmployeeHomeView
from views.GuestHomeView import GuestHomeView
from controllers.RequestDetailsController import RequestDetailsController
from models.Request import Request
from models.enums import StatusEnum
from datetime import datetime

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
        equipments_controller = EquipmentsController(self.login_controller)
        equipments_controller.equipments_page()

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
        RequestDetailsController(self, request, user)

#TESTE POIS AINDA NÃO TEM A PARTE DE ASSOCIATED USERS

    def get_usersAssociated(self, user):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT userAssociated FROM associatedUsers WHERE emailUser = ?
        ''', (user.email,))

        all_users = cursor.fetchall()
        conn.close()

        users_list = []
        for user_data in all_users:
            user = pickle.loads(user_data[0])
            users_list.append(user.full_name)

        return users_list
      
    def register_request(self, for_who, sport, includes_skis, includes_boots, includes_helmet, user): #Self, status, sport, timestamp, user, boots, helmet, ski_board       
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
            includes_skis = "Requested"
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

        timestamp = datetime.now().timestamp()
        request = Request(StatusEnum.SENT, sport, timestamp, user, includes_boots, includes_helmet, includes_skis, associatedName)
        self.open_request_details_page(request, user)
        self.view.message_box('Success', 'Request submitted successfully!')