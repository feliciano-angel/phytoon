#programa26
#feliciano
precio=float(input("ingresa precio"))
edad=int(input("ingresa edad"))
if (edad>=1) and (edad<=12):
    total=(precio/100)*50
if (edad>=13) and (edad<=17):
    total=(precio/100)*30
if (edad>=18) and (edad<=59):
    total=(precio/100)*100
totaldes=total-precio
print("El total de precio es de=",totaldes)
