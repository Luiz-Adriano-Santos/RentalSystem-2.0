import sqlite3
import pickle

class Request:
    def __init__(self, status, sport, timestamp, user, boots, helmet, ski_board, associatedName ):
        self.status = status
        self.sport = sport
        self.timestamp = timestamp
        self.user = user
        self.boots = boots
        self.din = '' #self.calculate_din()
        self.employee = ''
        self.helmet = helmet
        self.ski_board = ski_board
        self.associatedName = associatedName     
    
    '''def calculate_din(self):

        if self.ski_board == 'Not Requested' or self.ski_board.type == 'BOARD':
            return ''
        
        else:

            first_tier = [0.75, 1, 1.25, 1.5, 2, 2.5, 3, 3.5, 4.25, 5, 6, 7, 8.5, 10, 12]
            second_tier = [0, 0.75, 1, 1.5, 1.75, 2.25, 2.5, 3, 4, 4.75, 5.5, 6.75, 8, 9.5, 11.25]
            third_tier = [0, 0, 0, 0, 0, 1.75, 2.25, 2.5, 3.25, 4, 5, 6, 7, 8.5, 10.25]
            fourth_tier = [0, 0, 0, 0, 0, 1.75, 2, 2.5, 3.25, 4, 4.75, 5.75, 6.75, 8.25, 10]

            if self.user.shoe_size <= 34:
                tier = first_tier
            elif 34 < self.user.shoe_size <= 37:
                tier = second_tier
            elif 37 < self.user.shoe_size <= 42:
                tier = third_tier
            else:
                tier = fourth_tier
            
            if self.user.height <= 148:
                din_h = 7
            elif 148 < self.user.height <= 157:
                din_h = 8
            elif 157 < self.user.height <= 166:
                din_h = 9
            elif 166 < self.user.height <= 178:
                din_h = 10
            elif 178 < self.user.height <= 194:
                din_h = 11
            else:
                din_h = 12
            
            if 9 < self.user.weight <= 13:
                din_w = 0
            elif 13 < self.user.weight <= 17:
                din_w = 1
            elif 17 < self.user.weight <= 21:
                din_w = 2
            elif 21 < self.user.weight <= 25:
                din_w = 3
            elif 25 < self.user.weight <= 230:
                din_w = 4
            elif 30 < self.user.weight <= 35:
                din_w = 5
            elif 35 < self.user.weight <= 41:
                din_w = 6
            elif 41 < self.user.weight <= 48:
                din_w = 7
            elif 48 < self.user.weight <= 57:
                din_w = 8
            elif 57 < self.user.weight <= 66:
                din_w = 9
            elif 66 < self.user.weight <= 78:
                din_w = 10
            elif 78 < self.user.weight <= 94:
                din_w = 11
            else:
                din_w = 12
            
            if din_h < din_w:
                index = din_h
            else:
                index = din_w
            
            if self.user.age < 10 or self.user.age > 59:
                index -= 1

            if tier[index] == 0:
                return 'Error'
            else:
                return tier[index]
                '''
            
    def create_request(self):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO requests (emailUser, userAssociatedName, request) VALUES (?, ?, ?)", (self.user.email, self.associatedName, pickle.dumps(self)))

        conn.commit()
        conn.close()
