import customtkinter as ctk
from tkinter import messagebox

class RegistrationView:
    def __init__(self, controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("RENTAL SYSTEM - Create Account")
        self.root.geometry("1000x700")

        background_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='white')
        background_frame.place(relwidth=1, relheight=1)

        header_frame = ctk.CTkFrame(background_frame, height=50, fg_color='#81c9d8', corner_radius=0)
        header_frame.pack(fill='x')

        header_label = ctk.CTkLabel(header_frame, text="RENTAL SYSTEM", font=('Poppins Medium', 18, 'bold'), text_color="#535353")
        header_label.pack(side='left', padx=10)

        form_frame = ctk.CTkScrollableFrame(background_frame, corner_radius=0, fg_color="white", width=600, height=500)
        form_frame.place(relx=0.5, rely=0.5, anchor='center')

        registration_label = ctk.CTkLabel(form_frame, text="Registration", font=('Poppins Medium', 30, 'bold'), text_color='#8f8e8e')
        registration_label.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

        label_email = ctk.CTkLabel(form_frame, text="EMAIL", font=('DM Sans', 10), text_color='#8f8e8e')
        label_email.grid(row=1, column=0, sticky='w', pady=(5, 2), padx=20)
        self.entry_email = ctk.CTkEntry(form_frame, width=400, fg_color='lightgray', border_width=0, text_color='#4a4a4a')
        self.entry_email.grid(row=2, column=0, pady=(0, 10), padx=20)

        label_name = ctk.CTkLabel(form_frame, text="FULL NAME", font=('DM Sans', 10), text_color='#8f8e8e')
        label_name.grid(row=3, column=0, sticky='w', pady=(5, 2), padx=20)
        self.entry_name = ctk.CTkEntry(form_frame, width=400, fg_color='lightgray', border_width=0, text_color='#4a4a4a')
        self.entry_name.grid(row=4, column=0, pady=(0, 10), padx=20)

        label_age = ctk.CTkLabel(form_frame, text="AGE", font=('DM Sans', 10), text_color='#8f8e8e')
        label_age.grid(row=5, column=0, sticky='w', pady=(5, 2), padx=20)
        self.entry_age = ctk.CTkEntry(form_frame, width=400, fg_color='lightgray', border_width=0, text_color='#4a4a4a')
        self.entry_age.grid(row=6, column=0, pady=(0, 10), padx=20)

        label_gender = ctk.CTkLabel(form_frame, text="GENDER", font=('DM Sans', 10), text_color='#8f8e8e')
        label_gender.grid(row=7, column=0, sticky='w', pady=(5, 2), padx=20)

        self.gender_var = ctk.StringVar(value="MALE")
        self.entry_gender = ctk.CTkOptionMenu(form_frame, variable=self.gender_var, values=["MALE", "FEMALE"], fg_color='lightgray', button_color='lightgray', button_hover_color='gray', dropdown_fg_color='lightgray', dropdown_text_color='#4a4a4a', dropdown_hover_color='gray', text_color='#4a4a4a', corner_radius=10, width=400)
        self.entry_gender.grid(row=8, column=0, pady=(0, 10), padx=20)

        label_height = ctk.CTkLabel(form_frame, text="HEIGHT (cm)", font=('DM Sans', 10), text_color='#8f8e8e')
        label_height.grid(row=9, column=0, sticky='w', pady=(5, 2), padx=20)
        self.entry_height = ctk.CTkEntry(form_frame, width=400, fg_color='lightgray', border_width=0, text_color='#4a4a4a')
        self.entry_height.grid(row=10, column=0, pady=(0, 10), padx=20)

        label_weight = ctk.CTkLabel(form_frame, text="WEIGHT (kg)", font=('DM Sans', 10), text_color='#8f8e8e')
        label_weight.grid(row=11, column=0, sticky='w', pady=(5, 2), padx=20)
        self.entry_weight = ctk.CTkEntry(form_frame, width=400, fg_color='lightgray', border_width=0, text_color='#4a4a4a')
        self.entry_weight.grid(row=12, column=0, pady=(0, 10), padx=20)

        label_shoe_size = ctk.CTkLabel(form_frame, text="SHOE SIZE", font=('DM Sans', 10), text_color='#8f8e8e')
        label_shoe_size.grid(row=13, column=0, sticky='w', pady=(5, 2), padx=20)
        self.entry_shoe_size = ctk.CTkEntry(form_frame, width=400, fg_color='lightgray', border_width=0, text_color='#4a4a4a')
        self.entry_shoe_size.grid(row=14, column=0, pady=(0, 10), padx=20)

        label_password = ctk.CTkLabel(form_frame, text="PASSWORD", font=('DM Sans', 10), text_color='#8f8e8e')
        label_password.grid(row=15, column=0, sticky='w', pady=(5, 2), padx=20)
        self.entry_password = ctk.CTkEntry(form_frame, show='*', width=400, fg_color='lightgray', border_width=0, text_color='#4a4a4a')
        self.entry_password.grid(row=16, column=0, pady=(0, 10), padx=20)

        label_confirm_password = ctk.CTkLabel(form_frame, text="CONFIRM PASSWORD", font=('DM Sans', 10), text_color='#8f8e8e')
        label_confirm_password.grid(row=17, column=0, sticky='w', pady=(5, 2), padx=20)
        self.entry_confirm_password = ctk.CTkEntry(form_frame, show='*', width=400, fg_color='lightgray', border_width=0, text_color='#4a4a4a')
        self.entry_confirm_password.grid(row=18, column=0, pady=(0, 10), padx=20)

        button_register = ctk.CTkButton(form_frame, text="Create Account", font=('Poppins Bold', 13, 'bold'), fg_color='#4094a5', width=400, command=self.register_user)
        button_register.grid(row=19, column=0, pady=10, padx=20)

        button_back_to_login = ctk.CTkButton(form_frame, text="Back to Login", font=('Poppins Bold', 13, 'bold'), fg_color='#4094a5', width=400, command=self.back_to_login)
        button_back_to_login.grid(row=20, column=0, pady=10, padx=20)

    def register_user(self):
        email = self.entry_email.get()
        full_name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.gender_var.get().upper()
        height = self.entry_height.get()
        weight = self.entry_weight.get()
        shoe_size = self.entry_shoe_size.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()
        
        self.controller.add_user(email, full_name, age, gender, height, weight, shoe_size, password, confirm_password)

    def message_box(self, title, message):
        messagebox.showinfo(title, message)

    def back_to_login(self):
        self.controller.back_to_login()

    def close(self):
        self.root.destroy()