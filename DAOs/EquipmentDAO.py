import sqlite3
import pickle

from DAOs.RequestDAO import RequestDAO

class EquipmentDAO:
    def __init__(self):
        self.conn = sqlite3.connect('RentalSystem.db')
        self.cursor = self.conn.cursor()
    
    def get_boots(self, current_request):
        
        self.cursor.execute("SELECT equipment FROM equipments")

        equipments = self.cursor.fetchall()
        self.conn.close()

        available_boots_list = []
        for equipment_data in equipments:
            equipment = pickle.loads(equipment_data[0])
            if equipment.equipment_type == 'Boot' and equipment.size == str(current_request.associatedUser.shoe_size):
                for request in RequestDAO().get_requests():
                    if request.status == "IN_PROGRESS" and request.boots[0] == equipment.equipment_id and request.boots[1]:
                        available = False
                        break
                    available = True
                if available:
                    available_boots_list.append(equipment.equipment_id)
        
        return available_boots_list
    
    def get_helmets(self):
        
        self.cursor.execute("SELECT equipment FROM equipments")

        equipments = self.cursor.fetchall()
        self.conn.close()

        available_helmets_list = []
        for equipment_data in equipments:
            equipment = pickle.loads(equipment_data[0])
            if equipment.equipment_type == 'Helmet':
                for request in RequestDAO().get_requests():
                    if request.status == "IN_PROGRESS" and request.helmet[0] == equipment.equipment_id and request.boots[1]:
                        available = False
                        break
                    available = True
                if available:
                    available_helmets_list.append(equipment.equipment_id)
        
        return available_helmets_list
    
    def get_skis_boards(self, current_request, length):

        if current_request.sport == 'SKI':
            equipment_type = 'Ski'
        else:
            equipment_type = 'Snowboard'
        
        self.cursor.execute("SELECT equipment FROM equipments")

        equipments = self.cursor.fetchall()
        self.conn.close()

        available_skis_boards_list = []
        for equipment_data in equipments:
            equipment = pickle.loads(equipment_data[0])
            if equipment.equipment_type == equipment_type and equipment.size == length:
                for request in RequestDAO().get_requests():
                    if request.status == "IN_PROGRESS" and request.ski_board[0] == equipment.equipment_id and request.ski_board[1]:
                        available = False
                        break
                    available = True
                if available:
                    available_skis_boards_list.append(equipment.equipment_id)
        
        return available_skis_boards_list