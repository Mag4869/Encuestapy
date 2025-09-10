#Realizar una encuesta a sus compañeros que contenda estas funciones
#Si la persona es mayor de 18 años, proporcione un consejo de economia
#Si la persona es mayor de 20 años, proporcione un consejo de amor
print("En este codigo, vas a ingresar tu nombre y edad, clscon respecto a eso te dare un consejo")
print(" ")
Nombre= input("Ingresa tu primer nombre y tu primer apellido: ")
print (f"Tu nombre es {Nombre} verdad?")
s= int(input("Si quieres corregir tu nombre ingresa 0 = "))
if (s==0):
    Nombre= input("Puedes volver a ingresar tu primer nombre y tu primer apellido: ")
else:
    print(" ")
edad= int(input(f"Bueno {Nombre} ahora ingresa tu edad: "))
if (edad<20):
    if(edad>=18):
        print(f"{Nombre}, ya que aun eres joven, pero no lo suficiente, el consejo que te voy a dar es:")
        print("Empieza a ahorrar e invertir lo antes posible, aunque sea poco, el tiempo es tu mayor aliado. Gracias al interés compuesto, pequeñas cantidades de dinero ahorradas o invertidas regularmente pueden convertirse en sumas importantes con el tiempo.")
    else:
        print("Aun eres joven, disfruta tu vida hasta que cumplas 18 o tengas responsabilidades")
elif (edad>=20):
    print("Ya que eres un adulto, te voy a dar un consejo de amor, este es:")
    print("Es importante construir relaciones basadas en respeto, comunicación y crecimiento mutuo. Pero nunca olvides cuidar tu individualidad")
print(" ")
print(f"Espero te sirva este consejo {Nombre}")