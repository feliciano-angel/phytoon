#programa8
#feliciano
des=[""]*10
can=[0]*10
pre=[0.0]*10
for n in range(10):
    des[n]=(input("ingrese descripcion"))
    can[n]=int(input("ingrese la cantidad"))
    pre[n]=float(input("ingrese la precio"))


for n in range(10):
    print(can[n], des[n], "$",pre[n])
