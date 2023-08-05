import pyautogui
import keyboard
import time

def es_color_rojo(coordenadaX,coordenadaY):
    rojo = (187, 0, 0)  # Color rojo en formato (R, G, B)
    color = pyautogui.pixel(coordenadaX,coordenadaY)  # Obtiene el color del píxel en las coordenadas dadas
    print(f"COLOR: {color}")
    return color == rojo

def es_color_rojo_proceso(red_err_list):
    #x,y = pyautogui.position()
    rojo = (187, 0, 0)  # Color rojo en formato (R, G, B)
    color = pyautogui.pixel(red_err_list.x,red_err_list.y)  # Obtiene el color del píxel en las coordenadas dadas
    return color == rojo
def es_color_rojo_proceso_recosteo(red_err_reco):
    #x,y = pyautogui.position()
    rojo = (187, 0, 0)  # Color rojo en formato (R, G, B)
    color = pyautogui.pixel(red_err_reco.x,red_err_reco.y)  # Obtiene el color del píxel en las coordenadas dadas
    return color == rojo

def es_color_negro_proceso_recosteo(black_process_reco):
    #x,y = pyautogui.position()
    negro = (0, 0, 0)  # Color rojo en formato (R, G, B)
    color = pyautogui.pixel(black_process_reco.x,black_process_reco.y)  # Obtiene el color del píxel en las coordenadas dadas
    return color == negro
def es_color_verde_proceso_recosteo_final(green_end_process_reco):
    #x,y = pyautogui.position()
    verde = (0, 255, 0)  # Color rojo en formato (R, G, B)
    color = pyautogui.pixel(green_end_process_reco.x,green_end_process_reco.y) # Obtiene el color del píxel en las coordenadas dadas
    return color == verde

def config_var_global():
    global red_err_list, red_err_reco, black_process_reco, green_end_process_reco,point_list_page,point_save_page,point_search_page,point_console    
    print("Registrar coordenadas de la pantalla de error en recosteo: ")
    time.sleep(4)
    red_err_reco = pyautogui.position()
    print("Registrar coordenadas de la pantalla de proceso en recosteo: ")
    time.sleep(4)
    black_process_reco = pyautogui.position()
    print("Registrar coordenadas del fin del proceso en recosteo: ")
    time.sleep(4)
    green_end_process_reco = pyautogui.position()
    print("Registrar coordenadas de la consola de recosteo: ")
    time.sleep(4)
    point_save_page = pyautogui.position()
    print("Registrar coordenadas de la consola del proceso: ")
    time.sleep(4)
    point_console = pyautogui.position()
    print("Configuracion terminada terminada")
    
def click_change_page_save(point_save_page):
    pyautogui.click(point_save_page)
def click_change_page_list(point_list_page):
    pyautogui.click(point_list_page)
def click_change_page_search(point_search_page):
    pyautogui.click(point_search_page)
def click_change_page_console(point_console_page):
    pyautogui.click(point_console_page)
    
def recostear_valor():
    time.sleep(2)
    for i in range(1,2):
        for digito in str(fecha):
            time.sleep(0.1)
            keyboard.press(digito)
        time.sleep(0.1)    
        keyboard.press(str(i))
        for digito in str(item):
            time.sleep(0.1)
            keyboard.press(digito)
        time.sleep(0.1)
        keyboard.press("enter")
        time.sleep(0.1)
        keyboard.press("enter")
        time.sleep(0.1)
        keyboard.press("enter")
        time.sleep(0.1)
        keyboard.press("s")
        while es_color_rojo_proceso_recosteo(red_err_reco):
            time.sleep(0.1)
            keyboard.press("enter")
            time.sleep(0.1)
            keyboard.press("s")
        while es_color_negro_proceso_recosteo(black_process_reco):            
            if es_color_verde_proceso_recosteo_final(green_end_process_reco):
                print("esta por terminar")
                time.sleep(0.1)
                keyboard.press("enter")
                time.sleep(0.1)
                keyboard.press("enter")
                if i == 2:
                    return
                else:
                    pass
def generar_valor():
    global valor_final,proceso_abierto
    click_change_page_list(point_list_page)
    time.sleep(2)
    keyboard.press("enter")                
    time.sleep(0.1)
    keyboard.press("enter")
    time.sleep(0.1)           
    for digito in str(valor_final):
        keyboard.press(digito)    
    keyboard.press("enter")
    time.sleep(1)
    if es_color_rojo_proceso(red_err_list):
        keyboard.press("enter")
        time.sleep(0.1)
        keyboard.press("enter")
        time.sleep(0.1)            
    keyboard.press("enter")
    time.sleep(0.1)
    keyboard.press("enter")
    time.sleep(0.1)
    keyboard.press("enter")
    time.sleep(0.1)
    
def search_valor_unitario():
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
start= False
global red_err_list, red_err_reco, black_process_reco, green_end_process_reco,point_list_page,point_save_page,point_search_page,point_console    
global valor_final
global proceso_abierto
global primer_proceso
global item 
global fecha 
try: 
    valor_final = 0   
    while True:       
        if keyboard.is_pressed('f4') or keyboard.is_pressed('F4'):
            start = False
        elif keyboard.is_pressed('F1') or keyboard.is_pressed('F1'):
            start = True
        elif keyboard.is_pressed('F2') or keyboard.is_pressed('F2'):
            config_var_global()
            fecha = int(input("Ingresa la fecha: "))
        if start:
            while True:
                try:
                    item = int(input("Ingresa el item: "))                   
                    # valor_inicial = int(input("Ingresa el valor inicial: "))
                    # valor_final = int(input("Ingresa el precio unitario: "))
                    proceso_abierto = True
                    click_change_page_save(point_save_page)
                    recostear_valor()
                    click_change_page_console(point_console)
                except ValueError:
                    print("Ingresa un valor válido (debe ser un número entero).")
                
except KeyboardInterrupt:
    print("El script ha sido detenido manualmente.")
    
