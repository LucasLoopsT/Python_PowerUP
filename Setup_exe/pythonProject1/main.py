6.5  # Frameworks we'll use
import pyautogui
import pandas as pd
import time

# Some variables and presets:
email = "Lucas"
password = "python24"
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pd.read_csv("https://raw.githubusercontent.com/LucasLoopsT/Python_RPA/main/Python_PowerUP/produtos.csv")
pyautogui.PAUSE = 0.5


# Function to write text using the params, then press tab.
def writeTab(text):
    pyautogui.write(str(text))
    pyautogui.press("tab")


# First step: Open your browser.
pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("enter")

# Second step: Search for your website.
pyautogui.write(link)
pyautogui.press("enter")

# Third step: Log in with your account.
time.sleep(1)
pyautogui.press("tab")
writeTab(email)
writeTab(password)
pyautogui.press("enter")

# Fourth step: Set the data in the fields.
time.sleep(1)
pyautogui.press("tab")
for tupla in tabela.index:
    colunasID = {
        'codigo': tabela.loc[tupla, "codigo"],
        'marca': tabela.loc[tupla, "marca"],
        'tipo': tabela.loc[tupla, "tipo"],
        'categoria': tabela.loc[tupla, "categoria"],
        'preco_unitario': tabela.loc[tupla, "preco_unitario"],
        'custo': tabela.loc[tupla, "custo"],
        'obs': tabela.loc[tupla, "obs"]
    }
    for valor in colunasID.values():
        if not pd.isna(valor):
            writeTab(valor)
    pyautogui.press("enter")
    pyautogui.press("pageup")
    pyautogui.click(x=893, y=392)