print("Programa vacacional Rappi")
print()
print("¿Cual es tu nombre?")
nombre = input(">>>: ")
print()
print("Escribe una contraseña mayor de 4 digitos")
key = input(">>>: ")
print("Porfavor, confirma tu contraseña")
clave = input(">>>: ")
print()

while key == clave:
    print("!Confirmaste tu contraseña correctamente¡")
    print()
    print("¿Cuantos años tienes trabajando?")
    tiempo = int(input(">>>: "))
    print()
    if tiempo <= 5:
        print("Hola " + nombre + "!, tienes derecho a 10 dias de vacaciones.")

    elif tiempo <= 10:
        print("Hola " + nombre + "!, tienes derecho a 15 dias de vacaciones.")

    elif tiempo <= 20:
        print("Hola " + nombre + "!, tienes derecho a un mes de vacaciones.")

    else:
        print("No tienes derecho a vacaciones")
    print()
    print("Programa finalizado")
    break

if key != clave:
    print("Contraseña incorrecta")
    print()
    print("!Programa finalizado¡")