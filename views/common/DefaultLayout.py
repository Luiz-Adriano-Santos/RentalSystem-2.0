import customtkinter as ctk

from models.enums import GenderEnum


def initialize_window():
    root = ctk.CTk()
    root.title("RENTAL SYSTEM")
    root.geometry("1000x700")
    return root

def create_default_background(root):
    background_frame = ctk.CTkFrame(root, corner_radius=0, fg_color='white')
    background_frame.place(relwidth=1, relheight=1)
    return background_frame

def create_default_title(parent, text):
    title_frame = ctk.CTkFrame(parent, corner_radius=0, fg_color="white", width=400)
    title_frame.pack(pady=20)

    title_label = ctk.CTkLabel(
        title_frame,
        text=text,
        font=('Poppins Medium', 50, 'bold'),
        text_color='#8f8e8e'
    )
    title_label.grid(row=0, column=0, pady=10)

def create_default_header(parent, home_button_action):
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
        command=home_button_action,
        width=30,
        height=30
    )
    home_button.grid(row=0, column=0, padx=10)

def create_gender_select(parent, label_text, row, default_value=GenderEnum.MALE.value):
        gender_options = [GenderEnum.MALE.value, GenderEnum.FEMALE.value]
        entry = ctk.StringVar(value=default_value)

        ctk.CTkLabel(parent, text=label_text, text_color='#8f8e8e').grid(
            row=row, column=0, columnspan=2, padx=10, pady=(5, 2), sticky='w'
        )

        gender_select = ctk.CTkOptionMenu(
            parent,
            variable=entry,
            fg_color='lightgray',
            button_color='lightgray',
            button_hover_color='gray',
            dropdown_fg_color='lightgray',
            dropdown_text_color='#4a4a4a',
            dropdown_hover_color='gray',
            text_color='#4a4a4a',
            values=gender_options
        )
        gender_select.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='nsew')

        return entry

def create_form_field(parent, label_text, row, user_value, entry_options=None):
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