import speech_recognition as sr
import pyautogui as pg

def reconocerEscritura(text):
    if text == "espacio":
        pg.write(" ")
    elif text == "enter":
        pg.press("enter")
    elif text == "punto":
        pg.write(".")
    elif text == "p1":
        pg.write("(")
    elif text == "p2":
        pg.write(")")
    elif text == "comilla":
        pg.write("''")
    elif text == "borrar" :
        pg.press("delete")                 
    else:
        pg.write(text)
        
        
      
def redactar():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Di algo para escribir...")
            audio = r.listen(source)
            
        try:
            text = r.recognize_google(audio, language="es-ES")  # Utiliza el servicio de reconocimiento de voz de Google en español
            
            if text.lower() == "salir":
                break
          
            reconocerEscritura(text)
            print("Texto escrito: " + text)
            
        except sr.UnknownValueError:
            print("No se pudo reconocer el audio.")
            
        except sr.RequestError:
            print("No se pudo acceder al servicio de reconocimiento de voz.")
        
       

def mover(text):
    posicion_original = pg.position()
    if text == "arriba":
        pg.moveTo(posicion_original[0],posicion_original[1]-10)
        print("moviendo arriba")
    elif text == "abajo":
        print("moviendo abajo")
        pg.moveTo(posicion_original[0],posicion_original[1]+10)
    elif text == "izquierda":
        print("moviendo izquierda")
        pg.moveTo(posicion_original[0]-10,posicion_original[1])
    elif text == "derecha":
        pg.moveTo(posicion_original[0]-10,posicion_original[1])
        print("moviendo derecha")
    elif text == "click":
         pg.click()            
    elif text == "escribir":
        redactar()



while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio,language="es-ES")  # Utiliza el servicio de reconocimiento de voz de Google en español
        print("Texto reconocido: " + text)
        mover(text)
        
    except:
        print("error")    
        



