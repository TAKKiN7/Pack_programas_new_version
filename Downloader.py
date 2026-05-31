from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep as pause
from programas import lista
import urllib.request
from pathlib import Path
import subprocess

class Downloader:

    @staticmethod
    def download_chrome():
        caminho_exe : Path = Path.cwd() / "Instaladores/Chrome.exe"
        url = lista.get("chrome")
        for c in range(3):
            try:
                urllib.request.urlretrieve(url, caminho_exe)
            except:
                pass
            else:
                print("Download concluído")
                break
        subprocess.Popen([
            caminho_exe
        ])

    
    def get_driver(self) -> webdriver:
        options : Options = Options()
        options.add_argument("--user-data-dir=C:/SELENIUM")
        options.add_argument("--headless")
        driver : webdriver = webdriver.Chrome(options=options)
        return driver


    def download_programa(self, nome_arq : str, categoria):
        url_programa = lista.get(categoria).get(nome_arq)
        for c in range(3):
            driver = self.get_driver()
            driver.get(url_programa)

            try:
                bt_download = driver.find_element(By.TAG_NAME, "input")
            except:
                pass
            else:
                bt_download.click()
            # print("CLIQUEI")
            pause(3.5)
            self.waiting_download()
            validacao = self.validar(nome_arq)

            if validacao:
                break
        driver.quit()

    def waiting_download(self):
        caminho : Path = Path.home() / "Downloads"
        while True:
            cont = 0
            for item in caminho.iterdir():
                if item.is_file():
                    if item.suffix in (".crdownload", ".tmp"):
                        cont += 1

            if cont == 0:
                break
        # print("Download concluído")
    

    def validar(self, nome_arq : str) -> bool:
        caminho_downloads : Path = Path.home() / "Downloads"
        for arq in caminho_downloads.iterdir():
            if arq.is_file() and arq.stem == nome_arq:
                return True
    

downloader : Downloader = Downloader()