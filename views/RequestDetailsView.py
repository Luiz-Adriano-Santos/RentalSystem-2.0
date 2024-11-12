import customtkinter as ctk
from tkinter import messagebox

from models.enums import GenderEnum
from views.common.DefaultLayout import create_default_background, initialize_window

class RequestDetailsView:
    def __init__(self, request_details_controller, request):
        self.request_details_controller = request_details_controller
        self.request = request
        self.root = initialize_window()

        self.user = self.request.associatedUser
        self.status_entry = request.status
        self.sport_entry = request.sport
        self.timestamp_entry = request.timestamp
        self.boots = request.boots
        self.helmet = request.helmet
        self.ski_board = request.ski_board
        self.employee = request.employee
        self.din_entry = request.din

        self.setup_ui()

    def setup_ui(self):
        background_frame = create_default_background(self.root)
        self.create_header(background_frame)
        self.create_form_title(background_frame)
        self.create_edit_user_form(background_frame)

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

        edit_label = ctk.CTkLabel(
            title_frame,
            text="Rental Request Details",
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

        self.full_name_entry = self.create_form_field(form_frame, "FULL NAME", 2, self.user.full_name)
        self.full_name_entry.configure(state="readonly")

        self.sport_entry = self.create_form_field(form_frame, "SPORT", 4, self.sport_entry)
        self.sport_entry.configure(state="readonly")

        self.timestamp_entry = self.create_form_field(form_frame, "TIMESTAMP", 6, self.timestamp_entry)
        self.timestamp_entry.configure(state="readonly")

        self.status_entry = self.create_form_field(form_frame, "STATUS", 8, self.status_entry)
        self.status_entry.configure(state="readonly")

        self.gender_entry = self.create_form_field(form_frame, "GENDER", 10, self.user.gender)
        self.gender_entry.configure(state="readonly")

        self.us_shoe_size_entry = self.create_form_field(form_frame, "US SHOE SIZE", 12, self.user.shoe_size)
        self.us_shoe_size_entry.configure(state="readonly")

        self.age_entry = self.create_form_field(form_frame, "AGE", 14, self.user.age)
        self.age_entry.configure(state="readonly")

        self.weight_entry = self.create_form_field(form_frame, "WEIGHT (KG)", 16, self.user.weight)
        self.weight_entry.configure(state="readonly")

        self.height_entry = self.create_form_field(form_frame, "HEIGHT (CM)", 18, self.user.height)
        self.height_entry.configure(state="readonly")
        
        row = 20

        if self.ski_board != "Not Requested":

            self.ski_board_length_entry = self.create_form_field(form_frame, "SKI/BOARD LENGTH", 20, self.ski_board)

            self.ski_board_id_entry = self.create_form_field(form_frame, "SKI/BOARD ID", 22, self.ski_board)

            row = 24 

        if self.din_entry:

            self.din_entry = self.create_form_field(form_frame, "DIN", row, self.din_entry)
            self.din_entry.configure(state="readonly")

            row += 2

        if self.boots == "Requested":
            
            self.label_boots = ctk.CTkLabel(
                form_frame,
                text="BOOTS ID",
                text_color='#8f8e8e',
                anchor="w"
            )
            self.label_boots.grid(row=row, column=0, sticky='w', pady=(5, 2), padx=10)

            self.combo_boots = ctk.CTkComboBox(
                form_frame,
                width=200,
                fg_color='lightgray',
                border_width=0,
                text_color='#4a4a4a',
                values=self.request_details_controller.get_boots(),
            )
            self.combo_boots.set("")
            self.combo_boots.grid(row=row+2, column=0, pady=(0, 10), padx=10, sticky='w')

            row += 4
        
        if self.helmet == "Requested":

            self.label_helmet = ctk.CTkLabel(
                form_frame,
                text="HELMET ID",
                text_color='#8f8e8e',
                anchor="w"
            )
            self.label_helmet.grid(row=row, column=0, sticky='w', pady=(5, 2), padx=10)

            self.combo_helmet = ctk.CTkComboBox(
                form_frame,
                width=200,
                fg_color='lightgray',
                border_width=0,
                text_color='#4a4a4a',
                values=self.request_details_controller.get_helmets(),
            )
            self.combo_helmet.set("")
            self.combo_helmet.grid(row=row+2, column=0, pady=(0, 10), padx=10, sticky='w')

            row += 4

        self.employee_entry = self.create_form_field(form_frame, "EMPLOYEE", row, self.employee)
        self.employee_entry.configure(state="readonly")

        row += 2

        self.create_buttons(form_frame, row)

    def create_form_field(self, parent, label_text, row, user_value, entry_options=None):
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
        entry.insert(0, user_value)

        return entry

    def return_button_action(self):
        self.root.withdraw()
        self.request_details_controller.employee_home_page()

    def create_buttons(self, parent, row):

        buttons = []

        if self.status_entry.get() == 'SENT':
            buttons = [
                ("Cancel", self.cancel),
                ("In Progress", self.in_progress)
            ]
        elif self.status_entry.get() == 'IN_PROGRESS':
            buttons = []
            if self.ski_board != 'Not Requested':
                buttons.append(("Return Skis/Board", self.return_ski_board))
            if self.boots != 'Not Requested':
                buttons.append(("Return Boots", self.return_boots))
            if self.helmet != 'Not Requested':
                buttons.append(("Return Helmet", self.return_helmet))

        for i, (text, command) in enumerate(buttons):
            ctk.CTkButton(
                parent,
                text=text,
                font=('Poppins Bold', 13, 'bold'),
                fg_color='#81c9d8',
                command=command
            ).grid(row=row + i, column=0, columnspan=2, pady=10)

    def cancel(self):
        confirm = messagebox.askyesno("Confirm",
                                      "Are you sure you want to change the status of this request to CANCELED?")
        if confirm:
            self.request_details_controller.cancel_request()
            self.return_button_action()
        else:
            self.show_message('Canceled', "Request status change canceled.")

    def in_progress(self):
        pass

    def return_ski_board(self):
        pass

    def return_boots(self):
        pass

    def return_helmet(self):
        pass

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def mainloop(self):
        self.root.mainloop()
