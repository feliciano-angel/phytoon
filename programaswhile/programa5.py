#programa5
#feliciano
respuesta="x"
n=0
mes=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
while (respuesta!="N") or (respuesta!="n"):
    print(mes[n])
    n=n+1
    respuesta=input("deseas continuar")
    if (respuesta=="N") or (respuesta=="n"):
        break
print("fin del programa")
