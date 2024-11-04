
from views.EquipmentsHomeView import EquipmentsHomeView
from views.EquipmentRegistrationView import EquipmentRegistrationView


class EquipmentsController:
    def __init__(self, login_controller):
        self.login_controller = login_controller
        self.view = None

    def equipments_page(self):
        self.view = EquipmentsHomeView(self)
        self.view.mainloop()
    
    def register_equipment_page(self):
        self.view = EquipmentRegistrationView(self)
        self.view.mainloop()