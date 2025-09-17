#programa8
#feliciano
dilab=int(input("cuantos dias trabajaste"))
pagd=float(input("cuanto de pagan por dia"))
diaex=int(input("si trbajaste dia extra escribe el numero 1 si no el numero 2"))
total=dilab*pagd
if (diaex==1):
    labex=int(input("cuantos dias extra trabajaste"))
    pagex=float(input("cuanto te pagan por dia extra"))
    totalex=pagex*labex
    masd=total+totalex
    print("tu paga con dias extra es de",masd)
else:
    print("tu paga es de",total)
