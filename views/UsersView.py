from tkinter import messagebox

import customtkinter as ctk

from views.common.DefaultLayout import initialize_window, create_default_background, create_default_title, \
    create_default_header


class RegisteredUsersView:
    def __init__(self, controller, users, is_associated_users=False, logged_user=None):
        self.logged_user = logged_user
        self.controller = controller
        self.root = initialize_window()
        self.users = users
        self.is_associated_users = is_associated_users

        self.setup_ui()

    def setup_ui(self):
        background_frame = create_default_background(self.root)
        create_default_header(background_frame, self.home_button_action)
        if self.is_associated_users:
            title = 'Associated Users'
            self.create_associated_users_title(background_frame, title)
        else:
            title = 'Registered Users'
            create_default_title(background_frame, title)
        self.create_users_cards(background_frame)

    def create_associated_users_title(self, parent, title):
        title_frame = ctk.CTkFrame(parent, corner_radius=0, fg_color="white", width=400)
        title_frame.pack(pady=20)

        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_columnconfigure(1, weight=0)
        title_frame.grid_columnconfigure(2, weight=1)

        create_associated_user_button = ctk.CTkButton(
            title_frame,
            command=self.create_associated_user_action,
            text='Create User',
            fg_color='#535353',
            width=20,
            height=20
        )
        create_associated_user_button.grid(row=0, column=0, padx=(0, 10))

        edit_label = ctk.CTkLabel(
            title_frame,
            text=title,
            font=('Poppins Medium', 50, 'bold'),
            text_color='#8f8e8e'
        )
        edit_label.grid(row=0, column=1, pady=10)

    def create_users_cards(self, parent):
        users_frame = ctk.CTkScrollableFrame(parent, corner_radius=0, fg_color="white", width=1000)
        users_frame.pack(fill='y', expand=True)

        num_columns = 3

        users_frame.grid_columnconfigure(tuple(range(num_columns)), weight=1)

        for index, user in enumerate(self.users):
            row = index // num_columns
            col = index % num_columns
            self.create_card(users_frame, user, row, col)

    def create_card(self, parent, user, row, col):
        card_frame = ctk.CTkFrame(parent, corner_radius=10, fg_color="lightgray", width=200, height=150)
        card_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        card_frame.bind("<Button-1>", lambda event, u=user: self.on_card_click(u))

        card_frame.grid_columnconfigure(0, weight=1)

        name_label = ctk.CTkLabel(
            card_frame,
            text=user.full_name,
            bg_color='#81c9d8',
            font=('Poppins Medium', 20, 'bold'),
            text_color='#8f8e8e'
        )
        name_label.grid(row=0, column=0, sticky="nsew")

        gender_label = ctk.CTkLabel(
            card_frame,
            text=f"Gender: {user.gender}",
            font=('Poppins Medium', 15),
            text_color='#8f8e8e'
        )
        gender_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        age_label = ctk.CTkLabel(
            card_frame,
            text=f"Age: {user.age}",
            font=('Poppins Medium', 15),
            text_color='#8f8e8e'
        )
        age_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    def home_button_action(self):
        if self.is_associated_users:
            self.controller.return_guest_home(self.logged_user)
        else:
            self.controller.return_employee_home()

    def create_associated_user_action(self):
        self.controller.create_associated_user_view(self.logged_user)

    def on_card_click(self, user):
        if self.is_associated_users:
            self.controller.open_associated_user_edit_page(user)
        else:
            self.controller.open_employee_user_edit_page(user)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def mainloop(self):
        self.root.mainloop()
