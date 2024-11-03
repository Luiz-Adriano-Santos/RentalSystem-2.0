import sqlite3
import pickle

class User:
    def __init__(self, age, email, full_name, gender, height, is_employee, password_hash, shoe_size, weight):
        self.age = age
        self.email = email
        self.full_name = full_name
        self.gender = gender
        self.height = height
        self.is_employee = is_employee
        self.password_hash = password_hash
        self.shoe_size = shoe_size
        self.weight = weight

    def create_user(self):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO users (email, user) VALUES (?, ?)", (self.email, pickle.dumps(self)))

        conn.commit()
        conn.close()

    def update_user(self, full_name, age, gender, height, weight, shoe_size, password_hash, is_employee):

        self.age = age
        self.full_name = full_name
        self.gender = gender
        self.height = height
        self.is_employee = is_employee
        self.password_hash = password_hash
        self.shoe_size = shoe_size
        self.weight = weight

        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        user_data = [pickle.dumps(self), self.email]

        query = '''
            UPDATE Users 
            SET user = ?
            WHERE email = ?
            '''

        try:
            cursor.execute(query, user_data)
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

    def get_all_users(self):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT user FROM Users
        ''')

        all_users = cursor.fetchall()
        conn.close()

        users_list = []
        for user_data in all_users:
            user = pickle.loads(user_data[0])
            users_list.append(user)

        return users_list

    def delete_user(self):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        try:
            cursor.execute('''
                DELETE FROM Users WHERE email = ?
                ''', (self.email,))

            if cursor.rowcount == 0:
                print(f"No user found with email: {self.email}")
            else:
                print(f"User with email: {self.email} deleted successfully.")

            conn.commit()

        except sqlite3.Error as e:
            print(f"An error occurred while deleting the user: {e}")

        finally:
            conn.close()
    
    @classmethod
    def get_user(cls, email):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user FROM users WHERE email = ?", (email,))
        try:
            user = pickle.loads(cursor.fetchone()[0])
            conn.close()
            return user
        except:
            conn.close()
            return False