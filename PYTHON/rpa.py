import pyautogui
import time

# Abra o navegador (por exemplo, Edge)
pyautogui.hotkey('win', 's')  # Abre o menu Iniciar
pyautogui.write('edge\n', interval=0.1)  # Abre o Edge
time.sleep(2)  # Espera o Edge abrir

# Navegue até o site
pyautogui.write('https://archive.ics.uci.edu/', interval=0.3)
pyautogui.press('enter')  # Pressiona a tecla "Enter" após digitar o site
time.sleep(5)  # Espera o site carregar

pyautogui.click(x=1312, y=447)  # Coordenadas do botão de download
time.sleep(5)  # Espera o download iniciar


pyautogui.click(x=1410, y=223)  # Coordenadas do botão de download
time.sleep(10)  # Espera o download iniciar


# Feche o navegador
pyautogui.hotkey('ctrl', 'w')  # Fecha a aba atual


print("executado")

