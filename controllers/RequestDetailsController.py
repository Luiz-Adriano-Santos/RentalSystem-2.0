from views.RequestDetailsView import RequestDetailsView

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
        return self.request.get_boots()
    
    def get_helmets(self):
        return self.request.get_helmets()
    
    def get_skis_boards(self, length):
        return self.request.get_skis_boards(length)

    def cancel_request(self):
        self.request.cancel()
    
    def in_progress_request(self, ids):
        self.request.in_progress(ids, self.logged_employee)

    def return_ski_board(self):
        self.request.return_ski_board()

    def return_boots(self):
        self.request.return_boots()

    def return_helmet(self):
        self.request.return_helmet()