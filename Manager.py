from pathlib import Path
import os
from subprocess import Popen



class Manager:
    def move(self, nome_arq):
        caminho_arq : Path = Path.home() / f"Downloads/{nome_arq}.exe"
        pasta_destino : Path = Path.cwd() / "Instaladores"
        pasta_destino.mkdir(exist_ok=True)
        caminho_destino = f"{pasta_destino}/{nome_arq}.exe"
        os.rename(caminho_arq, caminho_destino)
    
    def executar_programa(self, caminho_arq):
        Popen([caminho_arq])



manager : Manager = Manager()