
import datetime
from models.Equipment import Equipment
from views.EquipmentEditView import EquipmentEditView
from views.EquipmentsHomeView import EquipmentsHomeView
from views.EquipmentRegistrationView import EquipmentRegistrationView


class EquipmentsController:
    def __init__(self, login_controller):
        self.login_controller = login_controller
        self.view = None

    def equipments_page(self):
        equipments = Equipment.get_all_equipments()
        self.view = EquipmentsHomeView(self, equipments)
        self.view.mainloop()
    
    def edit_equipment_page(self, equipment):
        self.view = EquipmentEditView(self, equipment)
        self.view.mainloop()
    
    def register_equipment_page(self):
        self.view = EquipmentRegistrationView(self)
        self.view.mainloop()

    def delete_equipment(self, equipment):
        try:
            if equipment.availability == "Rented":
                self.view.show_message("Error", "Cannot delete equipment that is currently rented.")
                return
            Equipment.delete_equipment(equipment_id=equipment.equipment_id)
            self.view.show_message("Success", "Equipment deleted successfully.")
            self.view.root.withdraw()
            self.equipments_page()

        except Exception as e:
            self.view.show_message("Error", f"Error deleting equipment: {str(e)}")
            return

    def add_new_equipment(self, type, id, size):
        if not all([type, id, size]):
            self.view.show_message("Error", "Please fill in all fields.")
            return

        if not str(size).isnumeric() or int(size) < 0 or int(size) > 300:
            self.view.show_message("Error", "Invalid size.")
            return

        try:
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            Equipment(id, type, size, date).create_equipment()
            self.view.show_message("Success", "Equipment registered successfully.")
            self.view.root.withdraw()
            self.equipments_page()

        except Exception as e:
            self.view.show_message("Error", f"Error registering equipment: {str(e)}")
            return