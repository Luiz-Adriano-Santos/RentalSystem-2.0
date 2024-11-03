import customtkinter as ctk
from views.common.BaseLayout import create_background, initialize_window, create_title


class EmployeeHomeView:
    def __init__(self, controller, user):
        self.controller = controller
        self.root = initialize_window()
        self.user = user

        self.setup_ui()

    def setup_ui(self):
        background_frame = create_background(self.root)
        self.create_employee_home_header(background_frame)
        create_title(background_frame, 'Rental Requests')


    def create_employee_home_header(self, parent):
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

        equipments_button = ctk.CTkButton(
            buttons_frame,
            text='Equipments',
            fg_color='#535353',
            command=self.equipments_button_action,
            width=30,
            height=30
        )
        equipments_button.grid(row=0, column=0, padx=10)

        logout_button = ctk.CTkButton(
            buttons_frame,
            text='Logout',
            command=self.logout_button_action,
            fg_color='#535353',
            width=30,
            height=30
        )
        logout_button.grid(row=0, column=1, padx=10)

        registered_users_button = ctk.CTkButton(
            buttons_frame,
            text='Users',
            fg_color='#535353',
            command=self.registered_users_button_action,
            width=30,
            height=30
        )
        registered_users_button.grid(row=0, column=2, padx=10)

    def equipments_button_action(self):
        self.controller.open_equipments_page()

    def logout_button_action(self):
        self.controller.logout()

    def registered_users_button_action(self):
        self.controller.open_registered_users_page(self.user)

    def mainloop(self):
        self.root.mainloop()
