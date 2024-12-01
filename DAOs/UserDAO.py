import sqlite3
import pickle

class UserDAO:
    def __init__(self):
        self.conn = sqlite3.connect('RentalSystem.db')
        self.cursor = self.conn.cursor()

    def get_user(self, email):
        self.cursor.execute("SELECT user FROM users WHERE email = ?", (email,))
        try:
            user = pickle.loads(self.cursor.fetchone()[0])
            self.conn.close()
            return user
        except:
            self.conn.close()
            return False