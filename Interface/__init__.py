from customtkinter import *
from time import sleep as pause





class App(CTk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", lambda: print())
        self.logo()
        self.mainloop()

    

    def logo(self):
        janela_A = 400
        janela_L = 500
        tela_A = (self.winfo_screenheight() // 2) - (janela_A // 2)
        tele_L = (self.winfo_screenwidth() // 2) - (janela_L // 2)

        self.geometry(f"{janela_L}x{janela_A}+{tele_L}+{tela_A}")
        self.after(3000, self.configuração)



    def configuração(self):
        self.title("Pack de Programas")
        janela_A = 1200
        janela_L = 1500
        tela_A = (self.winfo_screenheight() // 2) - (janela_A // 2)
        tele_L = (self.winfo_screenwidth() // 2) - (janela_L // 2)
        self.geometry(f"{janela_L}x{janela_A}+{tele_L}+{tela_A}")
        self.attributes("-fullscreen", True)
    


    def layout(self):
        pass
    


    


app = App()