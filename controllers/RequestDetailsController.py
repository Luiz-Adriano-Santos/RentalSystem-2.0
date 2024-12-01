from views.RequestDetailsView import RequestDetailsView

from DAOs.EquipmentDAO import EquipmentDAO
from DAOs.RequestDAO import RequestDAO

class RequestDetailsController:
    def __init__(self, employee_home_controller, request, user, logged_employee):
        self.employee_home_controller = employee_home_controller
        self.user = user
        self.request = request
        self.logged_employee = logged_employee
        self.view = RequestDetailsView(self, request).mainloop()
    
    def employee_home_page(self):
        self.employee_home_controller.open_employee_home_page(self.user)

    def get_boots(self):
        return EquipmentDAO().get_boots(self.request)
    
    def get_helmets(self):
        return EquipmentDAO().get_helmets()
    
    def get_skis_boards(self, length):
        return EquipmentDAO().get_skis_boards(self.request, length)

    def cancel_request(self):
        RequestDAO().cancel(self.request)
    
    def in_progress_request(self, ids):
        RequestDAO().in_progress(ids, self.logged_employee, self.request)

    def return_ski_board(self):
        RequestDAO().return_ski_board(self.request)

    def return_boots(self):
        RequestDAO().return_boots(self.request)

    def return_helmet(self):
        RequestDAO().return_helmet(self.request)