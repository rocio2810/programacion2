import tkinter
from PIL import ImageTk, Image
from bd_utils import traer_url_foto_por_id, traer_carta_random
from urllib.request import Request, urlopen

jugador1 = input("Ingrese nombre del jugador 1: ")
jugador2 = input("Ingrese nombre del jugador 2: ")

ventana = tkinter.Tk() #Crea la ventana
ventana.title("Juego")
def preparar_carta():
    datos = traer_carta_random()
    url_final = datos[0]
    vida = datos[1]
    danio = datos[2]
    req = Request(url_final, headers={'User-Agent': 'Mozilla/5.0'})
    raw_data = urlopen(req).read()
    photo = ImageTk.PhotoImage(data=raw_data)
    return (photo, vida, danio)


f1 = tkinter.Frame(ventana)
f1.grid(column=0, row=0)
f2 = tkinter.Frame(ventana)
f2.grid(column=1, row=0)
f3 = tkinter.Frame(ventana)
f3.grid(column=2, row=0)
carta1 = preparar_carta()
carta2 = preparar_carta()
ph1 = carta1[0]
ph2 = carta2[0]
l1 = tkinter.Label(f1, image=ph1)
l1.grid(column=0, row=0)
l2 = tkinter.Label(f3, image=ph2)
l2.grid(column=0, row=0)
boton1 = tkinter.Button(f2, text = "Golpear", command = lambda: print('{} golpeó a {}'.format(jugador1, jugador2)))
boton1.pack()

boton2 = tkinter.Button(f2, text = "Rendirse", command = lambda: print (f"{jugador1} se rindió"))
boton2.pack()

ventana.mainloop() #cierra registro de todo el programa