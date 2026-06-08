from customtkinter import CTkFrame, CTkImage, CTkLabel
from Menu_s.area_trabalho import criar_menu
from tkinter import Menu
from PIL import Image

class Area_Trabalho(CTkFrame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master, fg_color="#27558F", corner_radius=0)
        self.papel_parede()
        self.config()
    


    def papel_parede(self):
        largura_T = self.master.winfo_screenwidth()
        altura_T = self.master.winfo_screenheight() - (self.master.winfo_screenheight() * 0.05)
        image = Image.open("C:/Users/eustaquio.filho/Documents/pack_programas/Pack_programas_new_version/Imagens/02.png")
        papel_parede_I : CTkImage = CTkImage(light_image=image, dark_image=image, size=(largura_T, largura_T))

        image_L : CTkLabel = CTkLabel(self, text="", image=papel_parede_I, bg_color="BLACK")
        image_L.bind("<Button-3>", lambda e: self.abrir_menu(e))
        image_L.place(relx=0, rely=0, relwidth=1, relheight=1)


    def config(self):
        
        self.place(relx=0, rely=0, relwidth=1, relheight=.95)

    
    def abrir_menu(self, e):
        menu_area_trabalho : Menu = criar_menu(self, self.master)
        menu_area_trabalho.post(e.x_root, e.y_root)






