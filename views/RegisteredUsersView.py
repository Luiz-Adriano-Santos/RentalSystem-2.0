from tkinter import messagebox

import customtkinter as ctk

from views.common.BaseLayout import initialize_window, create_background, create_title


class RegisteredUsersView:
    def __init__(self, controller, users):
        self.controller = controller
        self.root = initialize_window()
        self.users = users

        self.setup_ui()

    def setup_ui(self):
        background_frame = create_background(self.root)
        self.create_header(background_frame)
        create_title(background_frame, 'Registered Users')
        self.create_users_cards(background_frame)

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

        spacer_label = ctk.CTkLabel(
            header_frame,
            text="RENTAL SYSTEM",
            font=('Poppins Medium', 18, 'bold'),
            text_color="#81c9d8"
        )
        spacer_label.pack(side='right', padx=10)

        buttons_frame = ctk.CTkFrame(header_frame, fg_color='#81c9d8')
        buttons_frame.pack(side='top', pady=5)

        home_button = ctk.CTkButton(
            buttons_frame,
            text='Home',
            fg_color='#535353',
            command=self.home_button_action,
            width=30,
            height=30
        )
        home_button.grid(row=0, column=0, padx=10)

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
        self.controller.return_employee_home()

    def on_card_click(self, user):
        self.controller.open_employee_user_edit_page(user)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def mainloop(self):
        self.root.mainloop()
