import pyautogui
import keyboard
import time
"""
This is a reST style.

:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""
def es_color_rojo(coordenadaX,coordenadaY):
    rojo = (187, 0, 0)  # Color rojo en formato (R, G, B)
    color = pyautogui.pixel(coordenadaX,coordenadaY)  # Obtiene el color del píxel en las coordenadas dadas
    print(f"COLOR: {color}")
    return color == rojo

def es_color_rojo_proceso():
    #x,y = pyautogui.position()
    rojo = (187, 0, 0)  # Color rojo en formato (R, G, B)
    color = pyautogui.pixel(577,468)  # Obtiene el color del píxel en las coordenadas dadas
    return color == rojo
def es_color_rojo_proceso_recosteo():
    #x,y = pyautogui.position()
    rojo = (187, 0, 0)  # Color rojo en formato (R, G, B)
    color = pyautogui.pixel(1150,888)  # Obtiene el color del píxel en las coordenadas dadas
    return color == rojo

def es_color_negro_proceso_recosteo():
    #x,y = pyautogui.position()
    negro = (0, 0, 0)  # Color rojo en formato (R, G, B)
    color = pyautogui.pixel(1188,809)  # Obtiene el color del píxel en las coordenadas dadas
    return color == negro
def es_color_verde_proceso_recosteo_final():
    #x,y = pyautogui.position()
    verde = (0, 255, 0)  # Color rojo en formato (R, G, B)
    color = pyautogui.pixel(1031,890) # Obtiene el color del píxel en las coordenadas dadas
    return color == verde

def sustraendo(valor:int,num_error:int):
    valor_a_restar:int=0
    size:int = 0
    if num_error == 0:
       size = len(str(valor))
       valor_a_restar = 10 ** (size - 1)      
    elif num_error == 1:
       valor_a_restar = int(valor * 0.1)
    elif num_error == 2:
        valor_a_restar = int(valor * 0.05)
    elif num_error == 3:
        valor_a_restar = int(valor * 0.03)
    elif num_error == 4:
        valor_a_restar = int(valor * 0.01)
    return valor_a_restar

def costear_ultimo_valor(valor: int , valorFinal: int):
    global valor_inicial,valor_final,proceso_abierto   
    if valor < valorFinal:
        valor_inicial_final = valorFinal
        keyboard.press("enter")
        time.sleep(0.5)
        keyboard.press("enter")
        time.sleep(0.5)
        for digito in str(valor_inicial_final):
            keyboard.press(digito)    
        keyboard.press("enter")
        time.sleep(0.5)
        keyboard.press("enter")
        time.sleep(0.5)
        keyboard.press("enter")
        time.sleep(0.5)
        keyboard.press("enter")
        print("FINALIZÓ EL PROCESO")
        valor_inicial = 0
        valor_final = 0
        proceso_abierto = False
        return True
    return False
        

def generar_valor(valorInicial:int, valorFinal:int):
    global valor,valor_inicial,valor_final,proceso_abierto
    valor = valorInicial
    time.sleep(2)
    if valor == valorFinal:
        valor_inicial = 0
        valor_final = 0
        proceso_abierto = False
        return
    
    errores = 0
    while valor > valorFinal and errores < 5:
        valor_a_restar = sustraendo(valor,errores)
        valor_inicial_final = valor - valor_a_restar
        keyboard.press("enter")                
        time.sleep(0.1)
        keyboard.press("enter")
        time.sleep(0.1)           
        for digito in str(valor_inicial_final):
            keyboard.press(digito)    
        keyboard.press("enter")
        time.sleep(1)
        if es_color_rojo_proceso():
            errores += 1
            keyboard.press("enter")
            time.sleep(0.1)
            keyboard.press("enter")
            time.sleep(0.1)
        else:            
            valor = valor_inicial_final
            valor_inicial = valor
           
        keyboard.press("enter")
        time.sleep(0.1)
        keyboard.press("enter")
        time.sleep(0.1)
        keyboard.press("enter")
        time.sleep(0.1)
    print(f"VALOR FINAL: {valor}")        
    if costear_ultimo_valor(valor,valorFinal): return     

def press_alt_tab_twice():
    keyboard.press('alt')
    keyboard.press_and_release('tab')
    time.sleep(0.5)
    keyboard.release('tab')
    keyboard.press('tab')
    keyboard.release('alt')
        
def press_alt_tab_once():
    keyboard.press('alt')
    keyboard.press_and_release('tab')
    time.sleep(0.5)
    keyboard.release('alt')
    keyboard.release('tab')
        
def realizar_recosteo(fecha: int, item: int):
    for i in range(1,3):
        for digito in str(fecha):
            time.sleep(0.2)
            keyboard.press(digito)
        print()
        time.sleep(0.1)    
        keyboard.press(str(i))
        for digito in str(item):
            time.sleep(0.2)
            keyboard.press(digito)
        time.sleep(0.1)
        keyboard.press("enter")
        time.sleep(0.1)
        keyboard.press("enter")
        time.sleep(0.1)
        keyboard.press("enter")
        time.sleep(0.1)
        keyboard.press("s")
        while es_color_rojo_proceso_recosteo():
            time.sleep(0.1)
            keyboard.press("enter")
            time.sleep(0.1)
            keyboard.press("s")
        while es_color_negro_proceso_recosteo():
            print("esta por terminar")            
            if es_color_verde_proceso_recosteo_final():
                time.sleep(0.1)
                keyboard.press("enter")
                time.sleep(0.1)
                keyboard.press("enter")
                if i == 2:
                    return
                else:
                    pass  
        
def recostear_valor():
    global primer_proceso
    time.sleep(4)
    if primer_proceso:
        #press_alt_tab_once()                
        press_alt_tab_twice()
        realizar_recosteo(fecha,item)
        primer_proceso = False
    else:
        press_alt_tab_once()
        realizar_recosteo(fecha,item)
    press_alt_tab_once()
    
    
start= False
global valor_inicial
global valor_final
global proceso_abierto
global primer_proceso
global item 
global fecha 
try:    
    while True:       
        if keyboard.is_pressed('f4') or keyboard.is_pressed('F4'):
            start = False
        elif keyboard.is_pressed('F1') or keyboard.is_pressed('F1'):
            start = True
        if start:
            try:
                valor_inicial = int(input("Ingresa el valor inicial: "))
                valor_final = int(input("Ingresa el valor final: "))
                fecha = int(input("Ingresa la fecha: "))
                item = int(input("Ingresa el item: "))   
                proceso_abierto = True 
            except:
                Exception("Ingresa un valor valido")
            primer_proceso = True 
            while valor_final > 0 and valor_inicial > 0 and proceso_abierto:
                generar_valor(valor_inicial,valor_final)
                recostear_valor() 
                
except KeyboardInterrupt:
    print("El script ha sido detenido manualmente.")