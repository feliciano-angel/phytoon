#programa3
#feliciano
respuesta="x"
suma=0
cont=0
while (respuesta!="N") or (respuesta!="n"):
    cal=float(input("ingresa la calificaion"))
    suma=suma+cal
    cont=cont+1
    respuesta=input("deseas continuar")
    if (respuesta=="N") or (respuesta=="n"):
        prom=suma/cont
        print("el promedio es",prom)
        break
print("fin del programa")
