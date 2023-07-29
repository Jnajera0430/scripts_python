import pyautogui
import keyboard
def es_color_rojo(coordenadaX,coordenadaY):
    rojo = (187, 0, 0)  # Color rojo en formato (R, G, B)
    color = pyautogui.pixel(coordenadaX,coordenadaY)  # Obtiene el color del píxel en las coordenadas dadas
    print(f"COLOR: {color}")
    return color == rojo
start= False
contador=0
try:    
    while True:       
        if keyboard.is_pressed('f4') or keyboard.is_pressed('F4'):
            print(f"los item con saldo negativo son: {contador}")
            start = False
        elif keyboard.is_pressed('F1') or keyboard.is_pressed('F1'):
            start = True
        if start: 
            pyautogui.press('f5')
            pyautogui.press('s')
            # Coordenadas del píxel donde se encuentra el posible indicador de error (ajusta según tu pantalla)
            x,y = pyautogui.position()
            print("paso")
            if es_color_rojo(x,y):
               # Ha ocurrido un error (el color en las coordenadas indicadas es rojo)
               # Manejar el error aquí, por ejemplo, presionando Enter y Flecha hacia abajo
               pyautogui.press('enter')
               pyautogui.press('down')
               contador=contador+1
            else:
               # No se ha detectado ningún error, continuar con el ciclo
               pass
        
except KeyboardInterrupt:
    print("El script ha sido detenido manualmente.")