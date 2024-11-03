import customtkinter as ctk
from views.common.BaseLayout import create_background, initialize_window, create_title

class GuestHomeView:
    def __init__(self, controller, user):
        self.user = user
        self.controller = controller
        self.root = initialize_window()

        self.setup_ui()

    def setup_ui(self):
        background_frame = create_background(self.root)
        self.create_user_home_header(background_frame)
        create_title(background_frame, 'User Dashboard')
        self.create_user_home_buttons(background_frame)

    def create_user_home_header(self, parent):
        header_frame = ctk.CTkFrame(parent, height=50, fg_color='#81c9d8', corner_radius=0)
        header_frame.pack(fill='x')

        header_label = ctk.CTkLabel(
            header_frame,
            text="RENTAL SYSTEM",
            font=('Poppins Medium', 18, 'bold'),
            text_color="#535353"
        )
        header_label.pack(side='left', padx=10)

        log_out_button = ctk.CTkButton(
            header_frame,
            text='LogOut',
            fg_color='#535353',
            command=self.log_out_button_action,
            width=60,
            height=30
        )
        log_out_button.place(relx=0.5, rely=0.5, anchor='center')


    def create_user_home_buttons(self, parent):
        button_frame = ctk.CTkFrame(parent, corner_radius=10, fg_color="white")
        button_frame.pack(pady=20)
        button_frame.place(relx=0.5, rely=0.5, anchor='center')

        account_info_button = ctk.CTkButton(
            button_frame,
            text="ACCOUNT INFORMATION",
            font=('Poppins Bold', 16, 'bold'),
            fg_color='#4094a5',
            height=50,
            width=300,
            corner_radius=10,
            command=self.open_account_information
        )
        account_info_button.grid(row=0, column=0, padx=10, pady=20)

        rental_requests_button = ctk.CTkButton(
            button_frame,
            text="Rental Historic",
            font=('Poppins Bold', 16, 'bold'),
            fg_color='#4094a5',
            height=50,
            width=300,
            corner_radius=10,
            #command=self.open_rental_requests               Futura implementação
        )
        rental_requests_button.grid(row=1, column=0, padx=10, pady=20)

    def log_out_button_action(self):
        self.controller.logout()
        

    def open_account_information(self):
        self.close()
        self.controller.open_guest_edit_page(self.user)

    def open_rental_requests(self):
        self.close()
        self.controller.open_rental_requests_page()

    def close(self):
        self.root.destroy()

    def mainloop(self):
        self.root.mainloop()
