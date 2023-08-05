import pyautogui
import time
import keyboard


def search_valor_unitario(item:int = 0):
    for _ in range(0,4):
        time.sleep(0.1)
        keyboard.press("esc")
    for digito in str(item):
        keyboard.press(digito)
    keyboard.press("enter")
    time.sleep(0.1)
    keyboard.press("enter")
    time.sleep(0.1)
    keyboard.press("f3")
    time.sleep(0.1)
    keyboard.press("enter")
    time.sleep(0.1)     
    for _ in range(0,36):
        time.sleep(0.1)
        keyboard.press("right")

item = int(input("Ingresa el item: "))
time.sleep(2)
search_valor_unitario(item)






# Obtener el ancho de la pantalla en píxeles
# ancho_pantalla = pyautogui.size().width

# # Obtener la posición actual del cursor en píxeles
# time.sleep(2)
# pyautogui.click(814,543)
# posicion_cursor = pyautogui.position()

# # Imprimir los resultados
# print(f"Ancho de la pantalla: {ancho_pantalla} píxeles")
# print(f"Posición del cursor: X={posicion_cursor.x}, Y={posicion_cursor.y} píxeles")

# x,y = pyautogui.position()
# color = pyautogui.pixel(x,y)  # Obtiene el color del píxel en las coordenadas dadas
# print(color)
# keyboard.press('alt')
# keyboard.press_and_release('tab')
# time.sleep(0.5)
# keyboard.release('tab')
# keyboard.press('tab')
# keyboard.release('alt')

# def es_color_rojo_proceso_recosteo():
#     #x,y = pyautogui.position()
#     rojo = (187, 0, 0)  # Color rojo en formato (R, G, B)
#     color = pyautogui.pixel(1150,888)  # Obtiene el color del píxel en las coordenadas dadas
#     return color == rojo

# def es_color_negro_proceso_recosteo():
#     #x,y = pyautogui.position()
#     negro = (0, 0, 0)  # Color rojo en formato (R, G, B)
#     color = pyautogui.pixel(1188,809)  # Obtiene el color del píxel en las coordenadas dadas
#     return color == negro
# def es_color_verde_proceso_recosteo_final():
#     #x,y = pyautogui.position()
#     verde = (0, 255, 0)  # Color rojo en formato (R, G, B)
#     color = pyautogui.pixel(1028,885) # Obtiene el color del píxel en las coordenadas dadas
#     return color == verde

# def press_alt_tab_twice():
#     keyboard.press('alt')
#     keyboard.press_and_release('tab')
#     time.sleep(0.5)
#     keyboard.release('tab')
#     keyboard.press('tab')
#     keyboard.release('alt')
        
# def press_alt_tab_once():
#     keyboard.press_and_release('alt+tab')
#     time.sleep(0.5) 
        
# def realizar_recosteo(fecha: int, item: int):
#     for i in range(1,3):
#         for digito in str(fecha):
#             time.sleep(0.5)
#             keyboard.press(digito)
#         print()
#         time.sleep(1)    
#         keyboard.press(str(i))
#         for digito in str(item):
#             time.sleep(0.5)
#             keyboard.press(digito)
#         time.sleep(1)
#         keyboard.press("enter")
#         time.sleep(1)
#         keyboard.press("enter")
#         time.sleep(1)
#         keyboard.press("enter")
#         time.sleep(1)
#         keyboard.press("s")
#         while es_color_rojo_proceso_recosteo():
#             time.sleep(1)
#             keyboard.press("enter")
#             time.sleep(1)
#             keyboard.press("s")
#         while es_color_negro_proceso_recosteo():
#             print("esta por terminar")
#             if es_color_verde_proceso_recosteo_final():
#                 time.sleep(1)
#                 keyboard.press("enter")
#                 time.sleep(1)
#                 keyboard.press("enter")
#                 return  
        
# def recostear_valor(primer_proceso:bool = False):
#     global item 
#     global fecha 
#     if primer_proceso:
#         press_alt_tab_once()           
#         #press_alt_tab_twice()
#         realizar_recosteo(fecha,item)
#         primer_proceso = False
#     else:
#         press_alt_tab_once()
#         realizar_recosteo(fecha,item)          
#     press_alt_tab_once()

# primer_proceso = True  
# fecha = int(input("Ingresa la fecha: "))
# item = int(input("Ingresa el item: "))   
# recostear_valor(primer_proceso)
