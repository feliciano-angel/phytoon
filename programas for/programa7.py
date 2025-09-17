#programa7
#feliciano
posi=0
nega=0
for n in range(1,21):
    num=int(input("ingrese el numero"))
    if num>=0:
        posi=posi+1
    if num < 0:
        nega=nega+1
print("de los 20 numeros", posi ,"son positivos")
print("de los 20 numeros", nega ,"son negativos")