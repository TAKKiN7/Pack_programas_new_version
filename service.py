from subprocess import Popen as abrir
from pathlib import Path
from Manager import manager
from Downloader import downloader, Downloader
from programas import lista



def validar_chrome():
    caminho_default_chrome : Path = Path("C:/Program Files/Google/Chrome/Application/chrome.exe")
    existe = caminho_default_chrome.is_file()    
    return existe


def login_chrome():
    abrir([
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "--user-data-dir=C:/SELENIUM",
        "google.com"
    ])


def executar(nome_arq : str, categoria):
    if not validar_chrome():
        Downloader.download_chrome()
    
    caminho_destino = Path.cwd() / f"Instaladores/{nome_arq}.exe"
    if not caminho_destino.is_file():
        downloader.download_programa(nome_arq, categoria)
        manager.move(nome_arq)
    else:
        print("JA EXISTE O EXECUTÁVEL.")
    manager.executar_programa(caminho_destino)



# METODO PRA USO DIRETO DO CMD SEM INTERFACE
def listar_categorias():
    programas : list[str] = [arq for arq in lista]
    for index, programa in enumerate(programas):
        print(f"{index + 1}_ {programa}")
    
    while True:
        try:
            opc = int(input("Digite o número da categoria: "))
        except:
            print("Digite um valor numérico!")
        else:
            if opc == 0:
                print("programa finalizado!")
                return None
            elif opc > len(programas) or opc < 0:
                print("Valor inválido")
                continue
            else:
                break
    return programas[opc - 1]


def listar_programas(categoria : str):
    if categoria:
        programas : list[str] = [arq for arq in lista.get(categoria) if arq != "chrome"]
        for index, programa in enumerate(programas):
            print(f"{index + 1}_ {programa}")

    while True:
        try:
            opc = int(input("Digite o número do programa: "))
        except:
            print("Digite um valor numérico!")
        else:
            if opc == 0:
                print("programa finalizado!")
                return None
            elif opc > len(programas) or opc < 0:
                print("Valor inválido")
                continue
            else:
                break
    return programas[opc - 1]