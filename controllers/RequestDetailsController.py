from views.RequestDetailsView import RequestDetailsView

class RequestDetailsController:
    def __init__(self, employee_home_controller, request):
        self.employee_home_controller = employee_home_controller
        self.request = request
        self.view = RequestDetailsView(self, request)