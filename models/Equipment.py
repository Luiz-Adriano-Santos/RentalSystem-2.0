import sqlite3
import pickle

class Equipment:
    def __init__(self, equipment_id, equipment_type, size, registration_date, availability):
        self.equipment_id = equipment_id
        self.equipment_type = equipment_type
        self.size = size
        self.registration_date = registration_date
        self.availability = availability


    def create_equipment(self):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO equipments (equipment_id, equipment) VALUES (?, ?)", 
                   (self.equipment_id, pickle.dumps(self)))

        conn.commit()
        conn.close()