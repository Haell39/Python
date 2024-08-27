import pyautogui

# Movendo o mouse para uma posição específica
pyautogui.moveTo(100, 100, duration=1)

# Clicando em um local específico
pyautogui.click(100, 100)

# Escrevendo um texto
pyautogui.write('Hello, World!', interval=0.1)

# Pressionando uma tecla
pyautogui.press('enter')

# Tirando uma captura de tela
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')
