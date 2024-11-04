import customtkinter as ctk
from views.common.BaseLayout import create_background, initialize_window, create_title

# IMPORTAÇÕES UTILIZADAS PARA TESTES:
from models.Request import Request
from datetime import datetime

class EmployeeHomeView:
    def __init__(self, controller, user):
        self.controller = controller
        self.root = initialize_window()
        self.user = user

        self.setup_ui()

    # INÍCIO DO TRECHO UTILIZADO PARA TESTES

        self.requests = self.get_requests()

    def get_requests(self):
        requests = []
        for i in range(5):
            requests.append(Request('Sent', 'Ski', datetime.now().strftime("%d/%m/%Y %H:%M:%S"), self.user))
        for i in range(5):
            requests.append(Request('In Progress', 'Ski', datetime.now().strftime("%d/%m/%Y %H:%M:%S"), self.user))
        for i in range(5):
            requests.append(Request('Returned', 'Snowboard', datetime.now().strftime("%d/%m/%Y %H:%M:%S"), self.user))
        for i in range(5):
            requests.append(Request('Canceled', 'Ski', datetime.now().strftime("%d/%m/%Y %H:%M:%S"), self.user))
        return requests

    # FIM DO TRECHO UTILIZADO PARA TESTES

    def setup_ui(self):
        background_frame = create_background(self.root)
        self.create_employee_home_header(background_frame)
        create_title(background_frame, 'Rental Requests')
        self.create_status_columns(background_frame)

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

    def create_status_columns(self, parent):
        status_frame = ctk.CTkScrollableFrame(parent, fg_color='white')
        status_frame.pack(pady=20, padx=20, fill='both', expand=True)

        statuses = ["Sent", "In Progress", "Returned", "Canceled"]

        columns_container = ctk.CTkFrame(status_frame, fg_color='white')
        columns_container.pack(pady=10, padx=50) 

        for col, status in enumerate(statuses):
            col_frame = ctk.CTkFrame(columns_container, fg_color='#f0f0f0', width=200, corner_radius=10)
            col_frame.grid(row=0, column=col, padx=10, pady=10, sticky="n") 

            status_label = ctk.CTkLabel(
                col_frame,
                text=status,
                font=('Poppins Medium', 18, 'bold'),
                text_color="#535353"
            )
            status_label.pack(pady=10)

            for request in self.requests:
                if request.status == status:
                    self.create_request_card(col_frame, request)

    def create_request_card(self, parent, request):
        card_frame = ctk.CTkFrame(parent, corner_radius=10, fg_color="lightgray", width=200, height=150)
        card_frame.pack(pady=10, padx=10, fill='x')

        card_frame.bind("<Button-1>", lambda event, r=request: self.on_card_click(r))

        card_frame.grid_columnconfigure(0, weight=1)

        name_label = ctk.CTkLabel(
            card_frame,
            text=request.timestamp,
            bg_color='#81c9d8',
            font=('Poppins Medium', 17, 'bold'),
            text_color='#8f8e8e'
        )
        name_label.grid(row=0, column=0, sticky="nsew")

        gender_label = ctk.CTkLabel(
            card_frame,
            text=request.user.full_name,
            font=('Poppins Medium', 15),
            text_color='#8f8e8e'
        )
        gender_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        age_label = ctk.CTkLabel(
            card_frame,
            text=request.sport,
            font=('Poppins Medium', 15),
            text_color='#8f8e8e'
        )
        age_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    def equipments_button_action(self):
        self.close()
        self.controller.open_equipments_page()

    def logout_button_action(self):
        self.controller.logout()

    def registered_users_button_action(self):
        self.close()
        self.controller.open_registered_users_page(self.user)
        

    def mainloop(self):
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()
    
    def on_card_click(self, request):
        self.controller.open_request_details_page(request)