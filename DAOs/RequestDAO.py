import sqlite3
import pickle

from models.enums import StatusEnum

class RequestDAO:
    def __init__(self):
        self.conn = sqlite3.connect('RentalSystem.db')
        self.cursor = self.conn.cursor()

    def get_requests(self):

        self.cursor.execute("SELECT request FROM requests")

        all_requests = self.cursor.fetchall()
        self.conn.close()

        requests_list = []
        for request_data in all_requests:
            request = pickle.loads(request_data[0])
            requests_list.append(request)
        
        return requests_list
    
    def cancel(self, request):
        request.status = StatusEnum.CANCELED.value
        
        self.cursor.execute("UPDATE requests SET request = ? WHERE id = ?", (pickle.dumps(request), request.id))

        self.conn.commit()
        self.conn.close()
    
    def in_progress(self, ids, employee, request):
        request.status = StatusEnum.IN_PROGRESS.value
        request.employee = employee.full_name
        if request.ski_board != 'Not Requested':
            request.ski_board = [ids['ski_board'], True]
        if request.helmet == 'Requested':
            request.helmet = [ids['helmet'], True]
        if request.boots == 'Requested':
            request.boots = [ids['boots'], True]
        
        self.cursor.execute("UPDATE requests SET request = ? WHERE id = ?", (pickle.dumps(request), request.id))

        self.conn.commit()
        self.conn.close()
    
    def return_ski_board(self, request):
        request.ski_board[1] = False

        if (request.helmet == 'Not Requested' or (request.helmet != 'Not Requested' and not request.helmet[1])) and (request.boots == 'Not Requested' or (request.boots != 'Not Requested' and not request.boots[1])):
            request.status = StatusEnum.RETURNED.value
        
        self.cursor.execute("UPDATE requests SET request = ? WHERE id = ?", (pickle.dumps(request), request.id))

        self.conn.commit()
        self.conn.close()

    def return_boots(self, request):
        request.boots[1] = False

        if (request.helmet == 'Not Requested' or (request.helmet != 'Not Requested' and not request.helmet[1])) and (request.ski_board == 'Not Requested' or (request.ski_board != 'Not Requested' and not request.ski_board[1])):
            request.status = StatusEnum.RETURNED.value

        
        self.cursor.execute("UPDATE requests SET request = ? WHERE id = ?", (pickle.dumps(request), request.id))

        self.conn.commit()
        self.conn.close()
    
    def return_helmet(self, request):
        request.helmet[1] = False

        if (request.ski_board == 'Not Requested' or (request.ski_board != 'Not Requested' and not request.ski_board[1])) and (request.boots == 'Not Requested' or (request.boots != 'Not Requested' and not request.boots[1])):
            request.status = StatusEnum.RETURNED.value
        
        self.cursor.execute("UPDATE requests SET request = ? WHERE id = ?", (pickle.dumps(request), request.id))

        self.conn.commit()
        self.conn.close()