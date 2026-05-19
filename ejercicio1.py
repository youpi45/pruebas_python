nombre = input("como te llamas?   ")
edad = int (input("cuantos años tienes?   "))
altura = float (input("cuanto mides  "))
ciudad = input("donde vives  ")
print ("hola", nombre)
print ("tienes",edad, "años")
print ("el año que viene tendras   ",edad+1,"haha")
print ("y vives en   ",ciudad,)

if edad >= 18:
   print ("eres mayor de edad")
else:
    print ("eres menor de edad")
