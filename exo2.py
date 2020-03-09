a = int(input(" entrer un nombre compris entre 10 et 30 :"))

while a < 10 or a > 31 :
    a = int(input(" entrer un nombre compris entre 10 et 30 :"))
    a = a + 1
if a < 10:
    print("le nombre est  plus petit")
elif a > 20:
    print("le nombre est plus grand")
else:
    print(a)