import sqlite3
import pickle
from models.enums import StatusEnum
import random

class Request:
    def __init__(self, status, sport, timestamp, user, boots, helmet, ski_board, associatedName ):
        self.id = random.randint(1,999)
        self.status = status
        self.sport = sport
        self.timestamp = timestamp
        self.user = user
        self.boots = boots
        self.employee = 'Not Assigned'
        self.helmet = helmet
        self.ski_board = ski_board
        self.associatedUser = self.get_associated_user(associatedName)
        self.din = self.calculate_din()
    
    def calculate_din(self):

        if self.ski_board == 'Not Requested' or self.ski_board == 'Board Requested':
            return ''
        
        else:

            first_tier = [0.75, 1, 1.25, 1.5, 2, 2.5, 3, 3.5, 4.25, 5, 6, 7, 8.5, 10, 12]
            second_tier = [0, 0.75, 1, 1.5, 1.75, 2.25, 2.5, 3, 4, 4.75, 5.5, 6.75, 8, 9.5, 11.25]
            third_tier = [0, 0, 0, 0, 0, 1.75, 2.25, 2.5, 3.25, 4, 5, 6, 7, 8.5, 10.25]
            fourth_tier = [0, 0, 0, 0, 0, 1.75, 2, 2.5, 3.25, 4, 4.75, 5.75, 6.75, 8.25, 10]

            if self.associatedUser.shoe_size <= 34:
                tier = first_tier
            elif 34 < self.associatedUser.shoe_size <= 37:
                tier = second_tier
            elif 37 < self.associatedUser.shoe_size <= 42:
                tier = third_tier
            else:
                tier = fourth_tier
            
            if self.associatedUser.height <= 148:
                din_h = 7
            elif 148 < self.associatedUser.height <= 157:
                din_h = 8
            elif 157 < self.associatedUser.height <= 166:
                din_h = 9
            elif 166 < self.associatedUser.height <= 178:
                din_h = 10
            elif 178 < self.associatedUser.height <= 194:
                din_h = 11
            else:
                din_h = 12
            
            if 9 < self.associatedUser.weight <= 13:
                din_w = 0
            elif 13 < self.associatedUser.weight <= 17:
                din_w = 1
            elif 17 < self.associatedUser.weight <= 21:
                din_w = 2
            elif 21 < self.associatedUser.weight <= 25:
                din_w = 3
            elif 25 < self.associatedUser.weight <= 23:
                din_w = 4
            elif 30 < self.associatedUser.weight <= 35:
                din_w = 5
            elif 35 < self.associatedUser.weight <= 41:
                din_w = 6
            elif 41 < self.associatedUser.weight <= 48:
                din_w = 7
            elif 48 < self.associatedUser.weight <= 57:
                din_w = 8
            elif 57 < self.associatedUser.weight <= 66:
                din_w = 9
            elif 66 < self.associatedUser.weight <= 78:
                din_w = 10
            elif 78 < self.associatedUser.weight <= 94:
                din_w = 11
            else:
                din_w = 12
            
            if din_h < din_w:
                index = din_h
            else:
                index = din_w
            
            if self.associatedUser.age < 10 or self.associatedUser.age > 59:
                index -= 1

            if tier[index] == 0:
                return 'Error'
            else:
                return tier[index]
            
    def get_associated_user(self, associatedName):

        if associatedName:

            conn = sqlite3.connect('RentalSystem.db')
            cursor = conn.cursor()

            cursor.execute("SELECT userAssociated FROM UsersAssociated WHERE emailUser = ? AND userAssociatedName = ?", (self.user.email, associatedName))

            userAssociated = pickle.loads(cursor.fetchone()[0])
            conn.close()
            return userAssociated

        else:
            return self.user
            
    def create_request(self):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        repeated_id = True

        while repeated_id:
            
            try:

                if self.associatedUser != self.user:
                    cursor.execute("INSERT INTO requests (id, emailUser, userAssociatedName, request) VALUES (?, ?, ?, ?)", (self.id, self.user.email, self.associatedUser.full_name, pickle.dumps(self)))
                else:
                    cursor.execute("INSERT INTO requests (id, emailUser, userAssociatedName, request) VALUES (?, ?, ?, ?)", (self.id, self.user.email, None, pickle.dumps(self)))

                repeated_id = False

            except:
                self.id = random.randint(1,999)

        conn.commit()
        conn.close()

    @classmethod
    def get_requests(cls):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        cursor.execute("SELECT request FROM requests")

        all_requests = cursor.fetchall()
        conn.close()

        requests_list = []
        for request_data in all_requests:
            request = pickle.loads(request_data[0])
            requests_list.append(request)
        
        return requests_list
    
    def cancel(self):
        self.status = StatusEnum.CANCELED.value

        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()
        
        cursor.execute("UPDATE requests SET request = ? WHERE id = ?", (pickle.dumps(self), self.id))

        conn.commit()
        conn.close()