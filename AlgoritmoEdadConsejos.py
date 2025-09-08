#Realizar una encuesta a sus compañeros que contenda estas funciones
#Si la persona es mayor de 18 años, proporcione un consejo de economia
#Si la persona es mayor de 20 años, proporcione un consejo de amor
print("En este codigo, vas a ingresar tu nombre y edad,con respecto a eso te dare un consejo")
print(" ")
Nombre= input("Ingresa tu primer nombre y tu primer apellido: ")
print (f"Tu nombre es {nombre} verdad?")
s= int(input("Si quieres corregir tu nombre ingresa 0 ="))
while (s==0):
    nombre= input("Digita nuevamente tu nombre: ")
    s+1