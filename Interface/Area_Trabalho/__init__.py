from customtkinter import CTkFrame, CTkImage, CTkLabel, CTkButton
from Interface.Menu_s.area_trabalho import criar_menu
from tkinter import Menu
from PIL import Image
from pathlib import Path
from programas import (
        loja_de_jogos, navegadores, comunicacao, Diagnosticos
    )

class Area_Trabalho(CTkFrame):

    def __init__(self, master):
        self.master = master
        super().__init__(self.master, fg_color="#27558F", corner_radius=0)
        self.papel_parede()
        self.icones_lojas()
        self.icones_comunicacao()
        self.icones_diagnosticos()
        self.icones_navegadores()
        self.config()
        
    


    def papel_parede(self):
        largura_T = self.master.winfo_screenwidth()
        altura_T = (self.master.winfo_screenheight() - (self.master.winfo_screenheight() * 0.05))

        image_path : Path  = Path.cwd() / "Imagens/03.png"

        image = Image.open(image_path)
        papel_parede_I : CTkImage = CTkImage(light_image=image, dark_image=image, size=(largura_T, altura_T))

        image_L : CTkLabel = CTkLabel(self, text="", image=papel_parede_I, bg_color="BLACK")
        image_L.bind("<Button-3>", lambda e: self.abrir_menu(e))
        image_L.place(relx=0, rely=0, relwidth=1, relheight=1)


    def config(self):
        
        self.place(relx=0, rely=0, relwidth=1, relheight=.95)

    
    def abrir_menu(self, e):
        menu_area_trabalho : Menu = criar_menu(self, self.master)
        menu_area_trabalho.post(e.x_root, e.y_root)



    def icones_lojas(self):
        for loja in loja_de_jogos:
            

            image_path : Path = Path.cwd() / f"Imagens/icones/{loja}.png"
            icon_image = Image.open(image_path)

            if loja in ("Riot"):
                image : CTkImage = CTkImage(light_image=icon_image, dark_image=icon_image, size=(39, 30))
            else:
                image : CTkImage = CTkImage(light_image=icon_image, dark_image=icon_image, size=(29, 29))


            icon : CTkButton = CTkButton(self, image=image, corner_radius=0,
                                         text="",
                                         fg_color="WHITE", text_color="WHITE",)
            
            icon.bind("<Double-Button-1>", lambda e: self.double_click(e, loja))
            icon.place(relx=loja_de_jogos.get(loja).get("pos_x"), rely=loja_de_jogos.get(loja).get("pos_y"),
                        relwidth=loja_de_jogos.get(loja).get("width"))
        


    def icones_navegadores(self):
        for nav in navegadores:
            
            if nav == "Chrome":
                continue

            image_path : Path = Path.cwd() / f"Imagens/icones/{nav}.png"
            icon_image = Image.open(image_path)

            image : CTkImage = CTkImage(light_image=icon_image, dark_image=icon_image, size=(29, 29))


            icon : CTkButton = CTkButton(self, image=image, corner_radius=0,
                                         text="",
                                         fg_color="BLACK", text_color="WHITE",)
            
            icon.bind("<Double-Button-1>", lambda e: self.double_click(e, nav))
            icon.place(relx=navegadores.get(nav).get("pos_x"), rely=navegadores.get(nav).get("pos_y"),
                        relwidth=navegadores.get(nav).get("width"))
            
    

    def icones_comunicacao(self):
        for app in comunicacao:
            


            image_path : Path = Path.cwd() / f"Imagens/icones/{app}.png"
            icon_image = Image.open(image_path)

            if app in ("Discord", "Teams"):
                image : CTkImage = CTkImage(light_image=icon_image, dark_image=icon_image, size=(39, 30))
            else:
                image : CTkImage = CTkImage(light_image=icon_image, dark_image=icon_image, size=(29, 29))


            icon : CTkButton = CTkButton(self, image=image, corner_radius=0,
                                         text="",
                                         fg_color="BLACK", text_color="WHITE",)
            
            icon.bind("<Double-Button-1>", lambda e: self.double_click(e, app))
            icon.place(relx=comunicacao.get(app).get("pos_x"), rely=comunicacao.get(app).get("pos_y"),
                        relwidth=comunicacao.get(app).get("width"))
            
        

    def icones_diagnosticos(self):
        for app in Diagnosticos:
            

            image_path : Path = Path.cwd() / f"Imagens/icones/{app}.png"
            icon_image = Image.open(image_path)

            if app in ("Riot"):
                image : CTkImage = CTkImage(light_image=icon_image, dark_image=icon_image, size=(39, 30))
            else:
                image : CTkImage = CTkImage(light_image=icon_image, dark_image=icon_image, size=(29, 29))


            icon : CTkButton = CTkButton(self, image=image, corner_radius=0,
                                         text="",
                                         fg_color="WHITE", text_color="WHITE",)
            
            icon.bind("<Double-Button-1>", lambda e: self.double_click(e, app))
            icon.place(relx=Diagnosticos.get(app).get("pos_x"), rely=Diagnosticos.get(app).get("pos_y"),
                        relwidth=Diagnosticos.get(app).get("width"))


    def double_click(self, e, nome_programa : str):
        print(f"abrindo {nome_programa}...")