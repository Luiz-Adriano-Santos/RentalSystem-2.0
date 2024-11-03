import customtkinter as ctk

class RoleSelectionView:
    def __init__(self, controller, user):
        self.controller = controller
        self.user = user
        self.root = ctk.CTk()
        self.root.title("RENTAL SYSTEM - Role Selection")
        self.root.geometry("1000x700")

        background_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='white')
        background_frame.place(relwidth=1, relheight=1)

        header_frame = ctk.CTkFrame(background_frame, height=50, fg_color='#81c9d8', corner_radius=0)
        header_frame.pack(fill='x')

        header_label = ctk.CTkLabel(header_frame, text="RENTAL SYSTEM", font=('Poppins Medium', 18, 'bold'), text_color="#535353")
        header_label.pack(side='left', padx=10)

        selection_frame = ctk.CTkFrame(background_frame, corner_radius=0, fg_color="white")
        selection_frame.place(relx=0.5, rely=0.5, anchor='center')

        employee_button = ctk.CTkButton(selection_frame, text="EMPLOYEE", font=('Poppins Medium', 30, 'bold'), fg_color='#4094a5', width=400, height=200, corner_radius=20, command=self.employee_page)
        employee_button.grid(row=0, column=0, padx=20, pady=20)

        guest_button = ctk.CTkButton(selection_frame, text="GUEST", font=('Poppins Medium', 30, 'bold'), fg_color='#4094a5', width=400, height=200, corner_radius=20, command=self.guest_page)
        guest_button.grid(row=0, column=1, padx=20, pady=20)

        back_button = ctk.CTkButton(selection_frame, text="Back", font=('Poppins Bold', 13, 'bold'), fg_color='#4094a5', command=self.back_to_login)
        back_button.grid(row=1, column=0, columnspan=2, pady=20)

    def back_to_login(self):
        self.root.destroy()
        self.controller.reset_login_fields()
        self.controller.view.root.deiconify()

    def mainloop(self):
        self.root.mainloop()
    
    def guest_page(self):
        self.root.destroy()
        self.controller.guest_page(self.user)

    def employee_page(self):
        self.root.destroy()
        self.controller.employee_page(self.user)