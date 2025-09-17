#programa5
#feliciano
respuesta="x"
n=0
cd=["zapotiltic","huescalapa","las canoas","el rincon","tamazula","tecalitalan"]
while (respuesta!="N") or (respuesta!="n"):
    print(cd[n])
    n=n+1
    respuesta=input("deseas continuar")
    if (respuesta=="N") or (respuesta=="n"):
        break
print("fin del programa")
