import customtkinter as ctk
from tkinter import messagebox

from views.common.BaseLayout import create_background, initialize_window

class EquipmentEditView:
    def __init__(self, controller, equipment):
        self.controller = controller
        self.root = initialize_window()

        self.equipment = equipment

        self.setup_ui()

    def setup_ui(self):
        background_frame = create_background(self.root)
        self.create_header(background_frame)
        self.create_form_title(background_frame)
        self.create_view_equipment_form(background_frame)

    def initialize_window(self):
        root = ctk.CTk()
        root.title("RENTAL SYSTEM - View Equipment")
        root.geometry("1000x700")
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
        title_frame.pack(pady=10)

        title_frame.grid_columnconfigure(0, weight=0)
        title_frame.grid_columnconfigure(1, weight=0)
        title_frame.grid_columnconfigure(2, weight=0)

        delete_button = ctk.CTkButton(
            title_frame,
            text="Delete",
            width=80,  
            height=40,
            font=('Poppins Medium', 14),  
            text_color='white',
            fg_color='#81c9d8',
            command=self.delete_equipment
        )
        delete_button.grid(row=0, column=0, padx=5)

        view_label = ctk.CTkLabel(
            title_frame,
            text="View Equipment",
            font=('Poppins Medium', 24, 'bold'),  
            text_color='#8f8e8e'
        )
        view_label.grid(row=0, column=1, padx=5)

        return_button = ctk.CTkButton(
            title_frame,
            text="Return",
            width=80,  
            height=40,
            font=('Poppins Medium', 14),  
            text_color='white',
            fg_color='#81c9d8',
            command=self.return_to_equipments_home
        )
        return_button.grid(row=0, column=2, padx=5)


    def create_view_equipment_form(self, parent):
        form_frame = ctk.CTkScrollableFrame(parent, corner_radius=0, fg_color="white", width=400)
        form_frame.pack(fill='y', expand=True)

        self.equipment_id_entry = self.create_form_field(
            form_frame, "EQUIPMENT ID", 2, self.equipment.equipment_id, readonly=True
        )
        self.equipment_type_entry = self.create_form_field(
            form_frame, "EQUIPMENT TYPE", 4, self.equipment.equipment_type, readonly=True
        )
        self.size_entry = self.create_form_field(
            form_frame, "SIZE", 6, self.equipment.size, readonly=True
        )
        self.registration_date_entry = self.create_form_field(
            form_frame, "REGISTRATION DATE", 8, self.equipment.registration_date, readonly=True
        )
        self.create_availability_label(
            form_frame, "AVAILABILITY", 10, self.equipment.availability
        )

        self.create_buttons(form_frame)

    def create_form_field(self, parent, label_text, row, value, readonly=True):
        ctk.CTkLabel(parent, text=label_text, font=('DM Sans', 10), text_color='#8f8e8e').grid(
            row=row, column=0, sticky='w', pady=(5, 2), padx=(20, 0)
        )

        entry = ctk.CTkEntry(
            parent,
            width=220,
            fg_color='lightgray',
            border_width=0,
            text_color='#4a4a4a'
        )
        entry.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='nsew')
        entry.insert(0, value)
        if readonly:
            entry.configure(state="readonly")

        return entry

    def create_availability_label(self, parent, label_text, row, value):
        ctk.CTkLabel(parent, text=label_text, text_color='#8f8e8e').grid(
            row=row, column=0, columnspan=2, padx=10, pady=(5, 2), sticky='w'
        )

        availability_label = ctk.CTkLabel(
            parent,
            text=value,
            font=('DM Sans', 10),
            text_color='#4a4a4a',
            fg_color='lightgray',
            corner_radius=5,
            anchor='w'
        )
        availability_label.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='nsew')

    def create_buttons(self, parent):
        buttons = [
            ("Rental Historic", self.button_rental_historic),
        ]
        for i, (text, command) in enumerate(buttons):
            ctk.CTkButton(
                parent,
                text=text,
                font=('Poppins Bold', 13, 'bold'),
                fg_color='#81c9d8',
                command=lambda: command(self.equipment)
            ).grid(row=23 + i, column=0, columnspan=2, pady=10)

    def button_rental_historic(self, equipment):
        self.show_message(
            "Redirecionando",
            f"Redirecionando para a página de Histórico de Aluguéis com o equipamento de ID: {equipment.equipment_id}"
        )

    def return_to_equipments_home(self):
        self.close()
        self.controller.equipments_page()

    def delete_equipment(self):
        self.controller.delete_equipment(self.equipment)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def mainloop(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()
