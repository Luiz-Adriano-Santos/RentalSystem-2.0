import customtkinter as ctk
from tkinter import messagebox
from views.common.DefaultLayout import create_default_background, create_default_header

class EquipmentsHomeView:
    def __init__(self, controller, equipments, logged_employee):
        self.controller = controller
        self.equipments = equipments 
        self.root = self.initialize_window()
        self.logged_employee = logged_employee
        self.setup_ui()

    def setup_ui(self):
        background_frame = create_default_background(self.root)
        create_default_header(background_frame, self.home_button_action )
        self.create_form_title(background_frame)
        self.create_equipment_columns(background_frame)

    def initialize_window(self):
        root = ctk.CTk()
        root.title("RENTAL SYSTEM - Equipments")
        root.geometry("1200x700")
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        return root

    def create_header(self, parent):
        header_frame = ctk.CTkFrame(parent, height=50, fg_color='#81c9d8', corner_radius=0)
        header_frame.pack(fill='x')

        header_label = ctk.CTkLabel(
            header_frame,
            text="RENTAL SYSTEM",
            font=('Poppins Medium', 18, 'bold'),
            text_color="#535353"
        )
        header_label.pack(side='left', padx=10)

    def create_form_title(self, parent):
        title_frame = ctk.CTkFrame(parent, corner_radius=0, fg_color="white")
        title_frame.pack(pady=20)

        title_inner_frame = ctk.CTkFrame(title_frame, fg_color="white")
        title_inner_frame.pack()

        edit_label = ctk.CTkLabel(
            title_inner_frame,
            text="Equipments",
            font=('Poppins Medium', 36, 'bold'),
            text_color='#8f8e8e'
        )
        edit_label.pack(side='left', pady=10, padx=10)

        add_button = ctk.CTkButton(
            title_inner_frame,
            text="+",
            width=40,
            height=40,
            font=('Poppins Medium', 20, 'bold'),
            text_color='white',
            fg_color='#81c9d8',
            command=self.add_equipment_action
        )
        add_button.pack(side='left', padx=10)

    def create_equipment_columns(self, parent):
        columns_frame = ctk.CTkFrame(parent, fg_color="white")
        columns_frame.pack(padx=50, pady=10, fill='both', expand=True)

        inner_columns_frame = ctk.CTkFrame(columns_frame, fg_color="white")
        inner_columns_frame.pack(anchor='center')

        categories = ["Ski", "Snowboard", "Boot", "Helmet"]
        for category in categories:
            column_frame = ctk.CTkFrame(inner_columns_frame, fg_color="white")
            column_frame.pack(side='left', padx=40, pady=10, fill='y')  

            category_label = ctk.CTkLabel(
                column_frame,
                text=category,
                font=('Poppins Medium', 20, 'bold'),
                text_color="#535353"
            )
            category_label.pack(pady=10)

            for equipment in self.equipments:
                if equipment.equipment_type == category:
                    self.create_equipment_card(column_frame, equipment)

    def create_equipment_card(self, parent, equipment):
        card_frame = ctk.CTkFrame(parent, fg_color='#D3D3D3', corner_radius=8, width=400, height=250)
        card_frame.pack(pady=10, padx=10, fill="both")

        id_frame = ctk.CTkFrame(card_frame, fg_color='#81C9D8', corner_radius=8)
        id_frame.pack(anchor='w', fill='x', pady=5)

        id_label = ctk.CTkLabel(id_frame, text=f"{equipment.equipment_id}", font=('Poppins', 18, 'bold'), text_color='black')
        id_label.pack(pady=4)

        size_label = ctk.CTkLabel(card_frame, text=f"{equipment.size}", font=('Poppins', 18), text_color='black')
        size_label.pack(anchor='w', padx=20, pady=4)

        date_label = ctk.CTkLabel(card_frame, text=f"{equipment.registration_date}", font=('Poppins', 18), text_color='black')
        date_label.pack(anchor='w', padx=20, pady=4)

        availability_label = ctk.CTkLabel(card_frame, text=f"{equipment.availability}", font=('Poppins', 18), text_color='black')
        availability_label.pack(anchor='w', padx=20, pady=4)

        card_frame.bind("<Button-1>", lambda e: self.on_card_click(equipment))


    def on_card_click(self, equipment):
        self.close()
        self.controller.edit_equipment_page(equipment, self.logged_employee)
        
    def home_button_action(self):
        self.root.withdraw()
        self.controller.return_to_employee_home(self.logged_employee)

    def add_equipment_action(self):
        self.close()
        self.controller.register_equipment_page(self.logged_employee)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def mainloop(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()
