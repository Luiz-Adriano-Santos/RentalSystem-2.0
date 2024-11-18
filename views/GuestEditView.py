import customtkinter as ctk
from tkinter import messagebox

from models.enums import GenderEnum
from views.common.DefaultLayout import create_default_background, initialize_window, create_default_header


class GuestEditView:
    def __init__(self, controller, user):
        self.controller = controller
        self.root = initialize_window()

        self.user = user
        self.full_name_entry = user.full_name
        self.email_entry = user.email
        self.age_entry = user.age
        self.gender_entry = user.gender
        self.height_entry = user.height
        self.weight_entry = user.weight
        self.us_shoe_size_entry = user.shoe_size
        self.password_entry = ''
        self.password_confirmation_entry = ''

        self.setup_ui()

    def setup_ui(self):
        background_frame = create_default_background(self.root)
        create_default_header(background_frame, self.home_button_action)
        self.create_form_title(background_frame)
        self.create_edit_user_form(background_frame)

    def initialize_window(self):
        root = ctk.CTk()
        root.title("RENTAL SYSTEM - Edit Account")
        root.geometry("1000x700")
        return root

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
            command=self.delete_button_action
        )
        delete_button.grid(row=0, column=0, padx=5)

        view_label = ctk.CTkLabel(
            title_frame,
            text="Edit Account",
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
            command=self.return_button_action
        )
        return_button.grid(row=0, column=2, padx=5)
    def create_edit_user_form(self, parent):
        form_frame = ctk.CTkScrollableFrame(parent, corner_radius=0, fg_color="white", width=400)
        form_frame.pack(fill='y', expand=True)

        self.full_name_entry = self.create_form_field(form_frame, "FULL NAME", 2, self.full_name_entry)
        self.email_entry = self.create_form_field(form_frame, "EMAIL", 4, self.email_entry)
        self.email_entry.configure(state="readonly")
        self.password_entry = self.create_form_field(form_frame, "NEW PASSWORD", 6, self.password_entry,
                                                     entry_options={"show": '*'})
        self.password_confirmation_entry = self.create_form_field(form_frame, "PASSWORD CONFIRMATION", 8,
                                                                  self.password_confirmation_entry,
                                                                  entry_options={"show": '*'})
        self.gender_entry = self.create_gender_select(form_frame, "GENDER", 10, self.gender_entry)
        self.us_shoe_size_entry = self.create_form_field(form_frame, "US SHOE SIZE", 12, self.us_shoe_size_entry)
        self.age_entry = self.create_form_field(form_frame, "AGE", 14, self.age_entry)
        self.weight_entry = self.create_form_field(form_frame, "WEIGHT (KG)", 18, self.weight_entry)
        self.height_entry = self.create_form_field(form_frame, "HEIGHT (CM)", 20, self.height_entry)

        self.create_buttons(form_frame)

    def create_form_field(self, parent, label_text, row, user_value, entry_options=None):
        ctk.CTkLabel(parent, text=label_text, font=('DM Sans', 10), text_color='#8f8e8e').grid(
            row=row, column=0, sticky='w', pady=(5, 2), padx=(20, 0) 
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
        entry.insert(0, user_value)

        return entry
    
    def create_gender_select(self, parent, label_text, row, default_value=GenderEnum.MALE.value):
        gender_options = [GenderEnum.MALE.value, GenderEnum.FEMALE.value]
        entry = ctk.StringVar(value=default_value)

        ctk.CTkLabel(parent, text=label_text, text_color='#8f8e8e').grid(
            row=row, column=0, columnspan=2, padx=10, pady=(5, 2), sticky='w'
        )

        gender_select = ctk.CTkOptionMenu(
            parent,
            variable=entry,
            fg_color='lightgray',
            button_color='lightgray',
            button_hover_color='gray',
            dropdown_fg_color='lightgray',
            dropdown_text_color='#4a4a4a',
            dropdown_hover_color='gray',
            text_color='#4a4a4a',
            values=gender_options
        )
        gender_select.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='nsew')

        return entry

    def return_button_action(self):
        self.root.withdraw()
        self.controller.return_guest_home(self.user)

    def home_button_action(self):
        self.root.withdraw()
        self.controller.return_guest_home(self.user)

    def create_buttons(self, parent):
        buttons = [
            ("Save", self.update_user),
        ]
        for i, (text, command) in enumerate(buttons):
            ctk.CTkButton(
                parent,
                text=text,
                font=('Poppins Bold', 13, 'bold'),
                fg_color='#81c9d8',
                command=command
            ).grid(row=23 + i, column=0, columnspan=2, pady=10)

    def update_user(self):
        full_name = self.full_name_entry.get()
        new_password = self.password_entry.get()
        password_confirmation = self.password_confirmation_entry.get()
        gender = self.gender_entry.get()
        us_shoe_size = self.us_shoe_size_entry.get()
        age = self.age_entry.get()
        weight = self.weight_entry.get()
        height = self.height_entry.get()

        self.controller.update_user_as_guest(self.user, full_name, new_password, password_confirmation, gender, us_shoe_size, age, weight, height)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
    
    def delete_button_action(self):
        self.controller.delete_user(self.user)

    def mainloop(self):
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()
