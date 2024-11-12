import customtkinter as ctk
from tkinter import messagebox
from views.common.DefaultLayout import create_default_background, initialize_window

class GuestHomeView:
    def __init__(self, controller, user):
        self.user = user
        self.controller = controller
        self.root = initialize_window()
        self.setup_ui()

    def setup_ui(self):
        background_frame = create_default_background(self.root)
        self.create_user_home_header(background_frame)
        self.create_user_home_form(background_frame)
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
            text_color="white",
            width=60,
            height=30,
            command=self.log_out_button_action
        )
        log_out_button.place(relx=0.5, rely=0.5, anchor='center')

    def create_user_home_form(self, parent):
        form_frame = ctk.CTkFrame(parent, corner_radius=10, fg_color="white")
        form_frame.place(relx=0.25, rely=0.5, anchor='center')

        title_label = ctk.CTkLabel(
            form_frame,
            text="NEW RENTAL REQUEST",
            font=('Bold', 20),
            text_color="#535353"
        )
        title_label.grid(row=0, column=0, pady=(10, 2), padx=20, sticky='w')

        subtitle_label = ctk.CTkLabel(
            form_frame,
            text="Make sure your information is updated!",
            font=('Poppins', 14),
            text_color="#8f8e8e"
        )
        subtitle_label.grid(row=1, column=0, pady=(0, 10), padx=20, sticky='w')

        self.label_for_who = ctk.CTkLabel(
            form_frame,
            text="FOR WHO?",
            font=('DM Sans', 10),
            text_color='#8f8e8e',
            anchor="w"
        )
        self.label_for_who.grid(row=2, column=0, sticky='w', pady=(5, 2), padx=20)

        self.combo_for_who = ctk.CTkComboBox(
            form_frame,
            width=200,
            fg_color='lightgray',
            border_width=0,
            text_color='#4a4a4a',
            values=[self.user.full_name] + self.controller.get_usersAssociated(self.user),
        )
        self.combo_for_who.set("")
        self.combo_for_who.grid(row=3, column=0, pady=(0, 10), padx=20, sticky='w')

        self.label_sport = ctk.CTkLabel(
            form_frame,
            text="SPORT",
            font=('DM Sans', 10),
            text_color='#8f8e8e',
            anchor="w"
        )
        self.label_sport.grid(row=4, column=0, sticky='w', pady=(5, 2), padx=20)

        self.combo_sport = ctk.CTkComboBox(
            form_frame,
            width=200,
            fg_color='lightgray',
            border_width=0,
            text_color='#4a4a4a',
            values=["SKI", "SNOWBOARD"]
        )
        self.combo_sport.set("")
        self.combo_sport.grid(row=5, column=0, pady=(0, 10), padx=20, sticky='w')

        includes_label = ctk.CTkLabel(
            form_frame,
            text="INCLUDES",
            font=('DM Sans', 10),
            text_color='#8f8e8e'
        )
        includes_label.grid(row=6, column=0, sticky='w', pady=(5, 2), padx=20)

        self.skis_checkbox = ctk.CTkCheckBox(
            form_frame,
            text="SKIS/BOARD",
            fg_color='#8f8e8e',
            border_color='#8f8e8e',
            height=20,
            width=20
        )
        self.skis_checkbox.grid(row=7, column=0, sticky='w', padx=20, pady=(0, 5))

        self.boots_checkbox = ctk.CTkCheckBox(
            form_frame,
            text="BOOTS",
            fg_color='#8f8e8e',
            border_color='#8f8e8e',
            height=20,
            width=20
        )
        self.boots_checkbox.grid(row=8, column=0, sticky='w', padx=20, pady=(0, 5))

        self.helmet_checkbox = ctk.CTkCheckBox(
            form_frame,
            text="HELMET",
            fg_color='#8f8e8e',
            border_color='#8f8e8e',
            height=20,
            width=20
        )
        self.helmet_checkbox.grid(row=9, column=0, sticky='w', padx=20, pady=(0, 10))

        submit_button = ctk.CTkButton(
            form_frame,
            text="Submit",
            fg_color='#4094a5',
            width=200,
            height=30,
            command=self.submit_rental_request
        )
        submit_button.grid(row=10, column=0, pady=(20, 0), padx=20)

    def create_user_home_buttons(self, parent):
        button_frame = ctk.CTkFrame(parent, corner_radius=10, fg_color="white")
        button_frame.place(relx=0.75, rely=0.5, anchor='center')
        rental_requests_button = ctk.CTkButton(
            button_frame,
            text="RENTAL HISTORIC",
            font=('Poppins Bold', 16, 'bold'),
            fg_color='#4094a5',
            height=80,
            width=300,
            corner_radius=20,
            command=self.open_rental_requests
        )
        rental_requests_button.grid(row=0, column=0, padx=10, pady=15)
        account_info_button = ctk.CTkButton(
            button_frame,
            text="ACCOUNT INFORMATION",
            font=('Poppins Bold', 16, 'bold'),
            fg_color='#4094a5',
            height=80,
            width=300,
            corner_radius=20,
            command=self.open_account_information
        )
        account_info_button.grid(row=1, column=0, padx=10, pady=15)
        associated_users_button = ctk.CTkButton(
            button_frame,
            text="ASSOCIATED USERS",
            font=('Poppins Bold', 16, 'bold'),
            fg_color='#4094a5',
            height=80,
            width=300,
            corner_radius=20,
            command=self.open_associated_users
        )
        associated_users_button.grid(row=2, column=0, padx=10, pady=15)

    def submit_rental_request(self):
        for_who = self.combo_for_who.get()   
        sport = self.combo_sport.get() 
        includes_skis = self.skis_checkbox.get()
        includes_boots = self.boots_checkbox.get() 
        includes_helmet = self.helmet_checkbox.get()   

        self.controller.register_request(for_who, sport, includes_skis, includes_boots, includes_helmet, self.user)

    def message_box(self, title, message):
        messagebox.showinfo(title, message)

    def log_out_button_action(self):
        self.controller.logout()

    def open_account_information(self):
        self.close()
        self.controller.open_guest_edit_page(self.user)

    def open_rental_requests(self):
        self.close()
        self.controller.open_rental_requests_page()

    def open_associated_users(self):
        self.close()
        self.controller.open_associated_users_page(self.user)

    def close(self):
        self.root.destroy()

    def mainloop(self):
        self.root.mainloop()