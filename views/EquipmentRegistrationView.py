import customtkinter as ctk
from tkinter import messagebox

from views.common.DefaultLayout import create_default_background, initialize_window


class EquipmentRegistrationView:
    def __init__(self, controller, logged_employee):
        self.controller = controller
        self.root = initialize_window()

        self.logged_employee = logged_employee
        self.type_entry = ""
        self.id_entry = ""
        self.size_entry = ""
        self.size_dropdown = None

        self.setup_ui()

    def setup_ui(self):
        background_frame = create_default_background(self.root)
        self.create_header(background_frame)
        self.create_form_title(background_frame)
        self.create_add_equipment_form(background_frame)

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
        title_frame = ctk.CTkFrame(parent, corner_radius=0, fg_color="white", width=400)
        title_frame.pack(pady=20)

        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_columnconfigure(1, weight=0)
        title_frame.grid_columnconfigure(2, weight=1)

        return_button = ctk.CTkButton(
            title_frame,
            command=self.return_to_equipments_home,
            text='Return',
            fg_color='#535353',
            width=20,
            height=20
        )
        return_button.grid(row=0, column=0, padx=(10, 0))

        add_label = ctk.CTkLabel(
            title_frame,
            text="Add New Equipment",
            font=('Poppins Medium', 50, 'bold'),
            text_color='#8f8e8e'
        )
        add_label.grid(row=0, column=1, pady=10)

    def create_add_equipment_form(self, parent):
        form_frame = ctk.CTkFrame(parent, corner_radius=0, fg_color="white", width=400)
        form_frame.pack(fill='y', expand=True)

        self.type_entry, type_dropdown = self.create_dropdown_field(form_frame, "TYPE", 2, ["Ski", "Snowboard", "Helmet", "Boot"])
        
        self.size_entry, self.size_dropdown = self.create_dropdown_field(form_frame, "SIZE", 6, ["128", "136", "144", "152", "160", "168", "176"])
        
        self.type_entry.trace("w", self.update_size_options)

        self.id_entry = self.create_form_field(form_frame, "ID", 4, self.id_entry)

        self.create_buttons(form_frame)

    def create_form_field(self, parent, label_text, row, initial_value, entry_options=None):
        parent.grid_columnconfigure(0, minsize=120)
        parent.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(parent, text=label_text, text_color='#8f8e8e').grid(
            row=row, column=0, columnspan=2, sticky='w', padx=10, pady=(5, 2)
        )

        entry_options = entry_options or {}
        entry = ctk.CTkEntry(
            parent,
            width=220,
            fg_color='lightgray',
            border_width=0,
            text_color='#4a4a4a',
            **entry_options
        )
        entry.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='nsew')
        entry.insert(0, initial_value)

        return entry

    def create_dropdown_field(self, parent, label_text, row, options):
        parent.grid_columnconfigure(0, minsize=120)
        parent.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(parent, text=label_text, text_color='#8f8e8e').grid(
            row=row, column=0, columnspan=2, sticky='w', padx=10, pady=(5, 2)
        )

        dropdown_value = ctk.StringVar(value=options[0] if options else "")
        dropdown = ctk.CTkOptionMenu(
            parent,
            variable=dropdown_value,
            values=options,
            fg_color='lightgray',
            button_color='lightgray',
            button_hover_color='gray',
            dropdown_fg_color='lightgray',
            dropdown_text_color='#4a4a4a',
            dropdown_hover_color='gray',
            text_color='#4a4a4a'
        )
        dropdown.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='nsew')

        return dropdown_value, dropdown

    def update_size_options(self, *args):
        type_selected = self.type_entry.get()
        if type_selected == "Ski":
            new_options = ["128", "136", "144", "152", "160", "168", "176"]
        elif type_selected == "Snowboard":
            new_options = ["110", "120", "130", "140", "150", "160"]
        elif type_selected == "Helmet":
            new_options = ["Unique"]
        elif type_selected == "Boot":
            new_options = ["32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45"]
        else:
            new_options = []

        self.size_dropdown.configure(values=new_options)
        self.size_entry.set(new_options[0]) 

    def create_buttons(self, parent):
        save_button = ctk.CTkButton(
            parent,
            text="Save",
            font=('Poppins Bold', 13, 'bold'),
            fg_color='#81c9d8',
            command=self.save
        )
        save_button.grid(row=10, column=0, columnspan=2, pady=10)

    def save(self):
        equipment_type = self.type_entry.get()
        equipment_id = self.id_entry.get()
        equipment_size = self.size_entry.get()

        self.controller.add_new_equipment(equipment_type, equipment_id, equipment_size)

    def return_to_equipments_home(self):
        self.root.withdraw()
        self.controller.equipments_page(self.logged_employee)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def mainloop(self):
        self.root.mainloop()
