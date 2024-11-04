import customtkinter as ctk
from tkinter import messagebox

from views.common.BaseLayout import create_background, initialize_window
class EquipmentRegistrationView:
    def __init__(self, controller):
        self.controller = controller
        self.root = initialize_window()
        self.setup_ui()

    def setup_ui(self):
        background_frame = create_background(self.root)
        self.create_header(background_frame)
        self.create_form_title(background_frame)
    
    def initialize_window(self):
        root = ctk.CTk()
        root.title("RENTAL SYSTEM - Equipments")
        root.geometry("1000x700")
        return root

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
        title_frame = ctk.CTkFrame(parent, corner_radius=0, fg_color="white")
        title_frame.pack(pady=20)

        edit_label = ctk.CTkLabel(
            title_frame,
            text="Editar Perfil",
            font=('Poppins Medium', 36, 'bold'),
            text_color='#8f8e8e'
        )
        edit_label.grid(row=0, column=0, pady=10)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)
    
    def mainloop(self):
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()
       