from views.RequestDetailsView import RequestDetailsView

class RequestDetailsController:
    def __init__(self, employee_home_controller, request, user):
        self.employee_home_controller = employee_home_controller
        self.user = user
        self.request = request
        self.view = RequestDetailsView(self, request).mainloop()
    
    def employee_home_page(self):
        self.employee_home_controller.open_employee_home_page(self.user)

    def get_boots(self):
        return self.request.get_boots()
    
    def get_helmets(self):
        return self.request.get_helmets()

    def cancel_request(self):
        self.request.cancel()