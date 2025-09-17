#programa4
#feliciano
respuesta="x"
dob=0

while (respuesta!="N") or (respuesta!="n"):
    num=float(input("ingresa un numero"))
    dob=num*2
    print("el doble es",dob)
    respuesta=input("deseas continuar")
    if (respuesta=="N") or (respuesta=="n"):
        break
print("fin del programa")
