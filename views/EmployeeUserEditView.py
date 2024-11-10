import customtkinter as ctk
from tkinter import messagebox

from models.enums import GenderEnum
from views.common.DefaultLayout import create_default_background, initialize_window, create_default_header, \
    create_form_field, create_gender_select


class EmployeeUserEditView:
    def __init__(self, controller, user):
        self.controller = controller
        self.root = initialize_window()

        self.user = user
        self.full_name_entry = user.full_name
        self.email_entry = user.email
        self.password_entry = ''
        self.password_confirmation_entry = ''
        self.gender_entry = user.gender
        self.us_shoe_size_entry = user.shoe_size
        self.age_entry = user.age
        self.is_employee_entry = user.is_employee
        self.weight_entry = user.weight
        self.height_entry = user.height

        self.setup_ui()

    def setup_ui(self):
        background_frame = create_default_background(self.root)
        create_default_header(background_frame, self.home_button_action)
        self.create_form_title(background_frame)
        self.create_edit_user_form(background_frame)

    def create_form_title(self, parent):
        title_frame = ctk.CTkFrame(parent, corner_radius=0, fg_color="white", width=400)
        title_frame.pack(pady=20)

        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_columnconfigure(1, weight=0)
        title_frame.grid_columnconfigure(2, weight=1)

        delete_user_button = ctk.CTkButton(
            title_frame,
            command=self.delete_user_action,
            text='Delete User',
            fg_color='#535353',
            width=20,
            height=20
        )
        delete_user_button.grid(row=0, column=0, padx=(0, 10))

        edit_label = ctk.CTkLabel(
            title_frame,
            text="Edit User Information",
            font=('Poppins Medium', 50, 'bold'),
            text_color='#8f8e8e'
        )
        edit_label.grid(row=0, column=1, pady=10)

        return_button = ctk.CTkButton(
            title_frame,
            command=self.return_button_action,
            text='Return',
            fg_color='#535353',
            width=20,
            height=20
        )
        return_button.grid(row=0, column=2, padx=(10, 0))

    def create_edit_user_form(self, parent):
        form_frame = ctk.CTkScrollableFrame(parent, corner_radius=0, fg_color="white", width=400)
        form_frame.pack(fill='y', expand=True)

        self.full_name_entry = create_form_field(form_frame, "FULL NAME", 2, self.full_name_entry)
        self.email_entry = create_form_field(form_frame, "EMAIL", 4, self.email_entry)
        self.email_entry.configure(state="readonly")
        self.password_entry = create_form_field(form_frame, "NEW PASSWORD", 6, self.password_entry,
                                                     entry_options={"show": '*'})
        self.password_confirmation_entry = create_form_field(form_frame, "PASSWORD CONFIRMATION", 8,
                                                                  self.password_confirmation_entry,
                                                                  entry_options={"show": '*'})
        self.gender_entry = create_gender_select(form_frame, "GENDER", 10, self.gender_entry)
        self.us_shoe_size_entry = create_form_field(form_frame, "US SHOE SIZE", 12, self.us_shoe_size_entry)
        self.age_entry = create_form_field(form_frame, "AGE", 14, self.age_entry)
        self.is_employee_entry = self.create_radio_buttons(form_frame, "EMPLOYEE", 16, self.is_employee_entry)
        self.weight_entry = create_form_field(form_frame, "WEIGHT (KG)", 18, self.weight_entry)
        self.height_entry = create_form_field(form_frame, "HEIGHT (CM)", 20, self.height_entry)

        self.create_buttons(form_frame)

    def create_radio_buttons(self, parent, label_text, row, default_value):
        parent.grid_columnconfigure(0, minsize=120)
        parent.grid_columnconfigure(1, weight=1)

        employee_label = ctk.CTkLabel(parent, text=label_text, text_color='#8f8e8e')
        employee_label.grid(row=row, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='w')

        radio_value = ctk.StringVar(value='1' if default_value else '0')

        ctk.CTkRadioButton(parent, text='Yes', variable=radio_value, value='1', text_color='#8f8e8e').grid(
            row=row + 1, column=0, padx=(10, 0), pady=(0, 5), sticky='w'
        )
        ctk.CTkRadioButton(parent, text='No', variable=radio_value, value='0', text_color='#8f8e8e').grid(
            row=row + 1, column=1, padx=(0, 10), pady=(0, 5), sticky='w'
        )

        return radio_value

    def delete_user_action(self):
        confirm = messagebox.askyesno("Confirm Delete",
                                      "Are you sure you want to delete this user?")
        if confirm:
            self.controller.delete_user(self.user)
        else:
            self.show_message('Error', "User deletion canceled.")

    def return_button_action(self):
        self.root.withdraw()
        self.controller.registered_users_page()

    def home_button_action(self):
        self.root.withdraw()
        self.controller.return_employee_home()

    def create_buttons(self, parent):
        buttons = [
            ("Rental History", self.rental_historic),
            ("Save", self.save),
            ("Working History", self.working_historic)
        ]
        for i, (text, command) in enumerate(buttons):
            ctk.CTkButton(
                parent,
                text=text,
                font=('Poppins Bold', 13, 'bold'),
                fg_color='#81c9d8',
                command=command
            ).grid(row=23 + i, column=0, columnspan=2, pady=10)

    def rental_historic(self):
        messagebox.showinfo("Info", "Rental History clicked")

    def save(self):
        full_name = self.full_name_entry.get()
        new_password = self.password_entry.get()
        password_confirmation = self.password_confirmation_entry.get()
        gender = self.gender_entry.get()
        us_shoe_size = self.us_shoe_size_entry.get()
        age = self.age_entry.get()
        is_employee = self.is_employee_entry.get()
        weight = self.weight_entry.get()
        height = self.height_entry.get()

        self.controller.update_user_as_employee(self.user, full_name, new_password, password_confirmation, gender, us_shoe_size, age, is_employee, weight, height)

    def working_historic(self):
        messagebox.showinfo("Info", "Working History clicked")

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def mainloop(self):
        self.root.mainloop()
