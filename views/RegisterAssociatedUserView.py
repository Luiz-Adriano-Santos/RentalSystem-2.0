import customtkinter as ctk
from tkinter import messagebox

from views.common.DefaultLayout import create_default_background, initialize_window, create_default_header, \
    create_gender_select, create_form_field


class RegisterAssociatedUserView:
    def __init__(self, controller, user):
        self.controller = controller
        self.root = initialize_window()

        self.user = user
        self.full_name_entry = ""
        self.gender_entry = ""
        self.us_shoe_size_entry = ""
        self.age_entry = ""
        self.weight_entry = ""
        self.height_entry = ""

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

        edit_label = ctk.CTkLabel(
            title_frame,
            text="Create new user",
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
        self.gender_entry = create_gender_select(form_frame, "GENDER", 10, self.gender_entry)
        self.us_shoe_size_entry = create_form_field(form_frame, "US SHOE SIZE", 12, self.us_shoe_size_entry)
        self.age_entry = create_form_field(form_frame, "AGE", 14, self.age_entry)
        self.weight_entry = create_form_field(form_frame, "WEIGHT (KG)", 18, self.weight_entry)
        self.height_entry = create_form_field(form_frame, "HEIGHT (CM)", 20, self.height_entry)

        self.create_buttons(form_frame)

    def return_button_action(self):
        self.root.withdraw()
        self.controller.associated_users_page(self.user)

    def home_button_action(self):
        self.root.withdraw()
        self.controller.return_guest_home(self.user)

    def create_buttons(self, parent):
        buttons = [
            ("Create", self.create)
        ]
        for i, (text, command) in enumerate(buttons):
            ctk.CTkButton(
                parent,
                text=text,
                font=('Poppins Bold', 13, 'bold'),
                fg_color='#81c9d8',
                command=command
            ).grid(row=23 + i, column=0, columnspan=2, pady=10)

    def create(self):
        # TODO Andreszinho: implement this method
        # full_name = self.full_name_entry.get()
        # gender = self.gender_entry.get()
        # us_shoe_size = self.us_shoe_size_entry.get()
        # age = self.age_entry.get()
        # weight = self.weight_entry.get()
        # height = self.height_entry.get()
        #
        # self.controller.create_associated_user()
        pass

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def mainloop(self):
        self.root.mainloop()
