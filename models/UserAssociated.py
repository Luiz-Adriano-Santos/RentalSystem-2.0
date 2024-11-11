import pickle
import sqlite3


class UserAssociated:
    def __init__(self, parent_user_email, full_name, gender, shoe_size, age, weight, height):
        self.parent_user_email = parent_user_email
        self.full_name = full_name
        self.gender = gender
        self.shoe_size = shoe_size
        self.age = age
        self.weight = weight
        self.height = height

    def create_associated_user(self):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO usersAssociated (parent_user, user, full_name) VALUES (?, ?, ?)", (self.parent_user_email, pickle.dumps(self), self.full_name))

        conn.commit()
        conn.close()

    def update_associated_user(self, user):
        self.full_name = user["full_name"]
        self.gender = user["gender"]
        self.shoe_size = user["shoe_size"]
        self.age = user["age"]
        self.weight = user["weight"]
        self.height = user["height"]

        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        user_data = [pickle.dumps(self), self.parent_user_email]

        query = '''
            UPDATE UsersAssociated 
            SET user = ?
            WHERE parent_user = ?
            '''

        try:
            cursor.execute(query, user_data)
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()


    def delete_associated_user(self):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        cursor.execute("DELETE FROM usersAssociated WHERE full_name = ?", self.full_name)

        conn.commit()
        conn.close()

    @classmethod
    def get_associated_users(cls, parent_user_email):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT user FROM UsersAssociated
        WHERE parent_user = ?
        ''', (parent_user_email,))

        users = []
        for row in cursor.fetchall():
            users.append(pickle.loads(row[0]))

        conn.close()

        return users

