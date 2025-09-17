#programa7
#feliciano
cant=int(input("ingresa la cantidad de burritos"))
pre=float(input("ingresa el valor por proucto"))
total=cant*pre
if (total>=500):
    des=(total/100)*20
    condes=total-des
    print("tu total a pagar es de",condes)
else:
    des=(total/100)*10
    condes=total-des
    print("tu total a pagar es de",condes)
