from customtkinter import CTkFrame, CTkImage, CTkLabel, CTkButton
from Interface.Menu_s.area_trabalho import criar_menu
from tkinter import Menu
from PIL import Image
from pathlib import Path
from programas import loja_de_jogos

class Area_Trabalho(CTkFrame):

    def __init__(self, master):
        self.master = master
        super().__init__(self.master, fg_color="#27558F", corner_radius=0)
        self.papel_parede()
        self.icones()
        self.config()
        
    


    def papel_parede(self):
        largura_T = self.master.winfo_screenwidth()
        altura_T = self.master.winfo_screenheight() - (self.master.winfo_screenheight() * 0.05)

        image_path : Path  = Path.cwd() / "Imagens/02.png"

        image = Image.open(image_path)
        papel_parede_I : CTkImage = CTkImage(light_image=image, dark_image=image, size=(largura_T, largura_T))

        image_L : CTkLabel = CTkLabel(self, text="", image=papel_parede_I, bg_color="BLACK")
        image_L.bind("<Button-3>", lambda e: self.abrir_menu(e))
        image_L.place(relx=0, rely=0, relwidth=1, relheight=1)


    def config(self):
        
        self.place(relx=0, rely=0, relwidth=1, relheight=.95)

    
    def abrir_menu(self, e):
        menu_area_trabalho : Menu = criar_menu(self, self.master)
        menu_area_trabalho.post(e.x_root, e.y_root)



    def icones(self):
        for loja in loja_de_jogos:
            

            image_path : Path = Path.cwd() / f"Imagens/icones/{loja}.png"
            icon_image = Image.open(image_path)

            image : CTkImage = CTkImage(light_image=icon_image, dark_image=icon_image, size=(24, 24))


            icon : CTkButton = CTkButton(self, image=image, corner_radius=0,
                                         text="",
                                         fg_color="BLACK", text_color="WHITE",)
            
            icon.bind("<Double-Button-1>", lambda e: self.double_click(e, loja))
            icon.place(relx=loja_de_jogos.get(loja).get("pos_x"), rely=loja_de_jogos.get(loja).get("pos_y"),
                        relwidth=loja_de_jogos.get(loja).get("width"))
        


    def double_click(self, e, nome_programa : str):
        print(f"abrindo {nome_programa}...")