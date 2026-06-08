from customtkinter import CTkFrame
from Menu_s.area_trabalho import criar_menu
from tkinter import Menu

class Area_Trabalho(CTkFrame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master, fg_color="#27558F", corner_radius=0)
        self.config()
    

    def config(self):
        self.bind("<Button-3>", lambda e: self.abrir_menu(e))
        self.place(relx=0, rely=0, relwidth=1, relheight=.95)

    
    def abrir_menu(self, e):
        menu_area_trabalho : Menu = criar_menu(self, self.master)
        menu_area_trabalho.post(e.x_root, e.y_root)



