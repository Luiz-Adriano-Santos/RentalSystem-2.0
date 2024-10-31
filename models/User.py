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

    @classmethod
    def update_user(cls, email, new_email, full_name, age, gender, height, weight, shoe_size, password_hash=None,
                    is_employee=None):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        # Lista de parâmetros a serem atualizados
        user_data = [full_name, age, gender, height, weight, shoe_size, new_email]

        # Base da query SQL
        query = '''
            UPDATE Users 
            SET full_name = ?, age = ?, gender = ?, height = ?, weight = ?, shoe_size = ?, email = ?
            '''

        # Se a senha foi fornecida, adiciona à query e aos dados
        if password_hash:
            query += ', password_hash = ?'
            user_data.append(password_hash)  # Adiciona o hash da senha ao final da lista

        # Se is_employee foi fornecido, adiciona à query e aos dados
        if is_employee is not None:
            query += ', is_employee = ?'
            user_data.append(is_employee)  # Adiciona o valor de is_employee ao final da lista

        query += ' WHERE email = ?'
        user_data.append(email)  # Adiciona o email como último parâmetro

        try:
            # Executa a query com os dados
            cursor.execute(query, user_data)
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()

    @classmethod
    def get_all_user_data(cls, email):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM Users WHERE email = ?
        ''', (email,))

        user_data = cursor.fetchone()
        conn.close()
        print(user_data)
        if user_data:
            user_dict = {
                'email': user_data[0],
                'full_name': user_data[1],
                'age': user_data[2],
                'gender': user_data[3],
                'height': user_data[4],
                'weight': user_data[5],
                'shoe_size': user_data[6],
                'is_active': user_data[7],  
                'is_employee': user_data[8],  
                'password_hash': user_data[9]  
            }
            return user_dict
        else:
            return None

    @classmethod
    def get_all_users(cls):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        cursor.execute('''
        SELECT * FROM Users
        ''')

        all_users = cursor.fetchall()
        conn.close()

        users_list = []
        for user_data in all_users:
            user_dict = {
                'email': user_data[0],
                'full_name': user_data[1],
                'age': user_data[2],
                'gender': user_data[3],
                'height': user_data[4],
                'weight': user_data[5],
                'shoe_size': user_data[6],
                'is_active': user_data[7],
                'is_employee': user_data[8],
                'password_hash': user_data[9]
            }
            users_list.append(user_dict)

        return users_list

    @classmethod
    def delete_user(cls, email):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        try:
            cursor.execute('''
                DELETE FROM Users WHERE email = ?
                ''', (email,))

            if cursor.rowcount == 0:
                print(f"No user found with email: {email}")
            else:
                print(f"User with email: {email} deleted successfully.")

            conn.commit()

        except sqlite3.Error as e:
            print(f"An error occurred while deleting the user: {e}")

        finally:
            conn.close()