from tkinter import Menu



def criar_menu(master):
    menu_tarefas : Menu = Menu(master, tearoff=0)
        
    menu_tarefas.add_command(
        label="Fechar área de trabalho",
        command=lambda: master.destroy()
    )

    return menu_tarefas