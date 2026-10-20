import time

# lista de usuarios: [nombre, clave, tipo]
usuarios = []

# lista de perros: [nombre, raza, edad, tamano, adoptado_por]
perros = [
    ["Max", "Labrador", 3, "Grande", ""],
    ["Luna", "Border Collie", 2, "Mediano", ""],
    ["Rocky", "Bulldog", 4, "Mediano", ""],
    ["Canela", "Beagle", 1, "Pequeno", ""],
    ["Toby", "Quiltro", 5, "Mediano", ""],
    ["Kira", "Husky", 2, "Grande", ""],
    ["Simba", "Golden Retriever", 6, "Grande", ""],
    ["Pelusa", "Poodle", 3, "Pequeno", ""],
]

CODIGO_ADMIN = "ADMIN2026"


# validar que el nombre solo tenga letras
def nombre_valido(nombre):
    solo_letras = nombre.replace(" ", "")
    if len(solo_letras) < 3:
        print("Error: el nombre debe tener al menos 3 letras.")
        return False
    if not solo_letras.isalpha():
        print("Error: el nombre solo puede tener letras.")
        return False
    return True


# validar la contrasena
def clave_valida(clave):
    if len(clave) < 8:
        print("Error: la contrasena debe tener al menos 8 caracteres.")
        return False
    tiene_letra = False
    tiene_numero = False
    for caracter in clave:
        if caracter.isalpha():
            tiene_letra = True
        if caracter.isdigit():
            tiene_numero = True
    if tiene_letra == False or tiene_numero == False:
        print("Error: la contrasena debe tener letras y numeros.")
        return False
    return True


# pedir una opcion del menu
def pedir_opcion(minimo, maximo):
    while True:
        opcion = input("Elige una opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion >= minimo and opcion <= maximo:
                return opcion
        print("Error: opcion invalida.")


# registrar un usuario nuevo
def registrar():
    print("\n--- REGISTRO ---")

    # pedir el nombre
    while True:
        nombre = input("Nombre real: ").title()
        if nombre_valido(nombre) == False:
            continue
        existe = False
        for u in usuarios:
            if u[0] == nombre:
                existe = True
        if existe:
            print("Error: ese usuario ya existe.")
        else:
            break

    # elegir el tipo de usuario
    print("1) Adoptante")
    print("2) Administrador")
    tipo = "Adoptante"
    if pedir_opcion(1, 2) == 2:
        codigo = input("Codigo de administrador: ")
        if codigo == CODIGO_ADMIN:
            tipo = "Administrador"
        else:
            print("Codigo incorrecto, seras Adoptante.")

    # pedir la contrasena
    while True:
        clave = input("Contrasena (minimo 8, letras y numeros): ")
        if clave_valida(clave) == False:
            continue
        repetir = input("Repite la contrasena: ")
        if clave == repetir:
            break
        print("Error: las contrasenas no coinciden.")

    usuarios.append([nombre, clave, tipo])
    print("Usuario registrado como", tipo)


# iniciar sesion
def iniciar_sesion():
    print("\n--- INICIAR SESION ---")
    print("1) Adoptante")
    print("2) Administrador")
    if pedir_opcion(1, 2) == 1:
        tipo = "Adoptante"
    else:
        tipo = "Administrador"

    intentos = 0
    while intentos < 3:
        nombre = input("Usuario: ").title()
        if nombre_valido(nombre) == False:
            continue
        clave = input("Contrasena: ")

        # buscar el usuario en la lista
        for u in usuarios:
            if u[0] == nombre and u[1] == clave and u[2] == tipo:
                print("Bienvenido/a", nombre)
                return [nombre, tipo]

        intentos = intentos + 1
        print("Datos incorrectos. Intentos restantes:", 3 - intentos)

    # bloqueo despues de 3 intentos
    print("Demasiados intentos. Espera 10 segundos.")
    time.sleep(10)
    return None


# mostrar todos los perros
def ver_perros():
    print("\n--- LISTADO DE PERROS ---")
    numero = 1
    for p in perros:
        if p[4] == "":
            estado = "Disponible"
        else:
            estado = "Adoptado por " + p[4]
        print(numero, ")", p[0], "-", p[1], "-", p[2], "anos -", p[3], "-", estado)
        numero = numero + 1


# adoptar un perro
def adoptar(usuario):
    print("\n--- ADOPTAR UN PERRO ---")
    disponibles = []
    for p in perros:
        if p[4] == "":
            disponibles.append(p)

    if len(disponibles) == 0:
        print("No quedan perros disponibles.")
        return

    numero = 1
    for p in disponibles:
        print(numero, ")", p[0], "-", p[1], "-", p[2], "anos -", p[3])
        numero = numero + 1
    print("0 ) Volver")

    opcion = pedir_opcion(0, len(disponibles))
    if opcion == 0:
        return

    elegido = disponibles[opcion - 1]
    confirmar = input("Confirmas adoptar a " + elegido[0] + "? (s/n): ")
    if confirmar == "s":
        elegido[4] = usuario
        print("Listo,", elegido[0], "fue adoptado.")
    else:
        print("Adopcion cancelada.")


# mostrar los perros adoptados por el usuario
def mis_adopciones(usuario):
    print("\n--- MIS ADOPCIONES ---")
    cantidad = 0
    for p in perros:
        if p[4] == usuario:
            print(p[0], "-", p[1], "-", p[2], "anos")
            cantidad = cantidad + 1
    if cantidad == 0:
        print("Aun no has adoptado ningun perro.")


# agregar un perro nuevo (solo administrador)
def agregar_perro():
    print("\n--- AGREGAR PERRO ---")
    nombre = input("Nombre del perro: ").title()
    if nombre_valido(nombre) == False:
        return
    raza = input("Raza: ").title()
    edad = input("Edad (anos): ")
    if raza == "" or edad.isdigit() == False:
        print("Error: datos invalidos.")
        return
    print("1) Pequeno")
    print("2) Mediano")
    print("3) Grande")
    opcion = pedir_opcion(1, 3)
    if opcion == 1:
        tamano = "Pequeno"
    elif opcion == 2:
        tamano = "Mediano"
    else:
        tamano = "Grande"
    perros.append([nombre, raza, int(edad), tamano, ""])
    print(nombre, "fue agregado al listado.")


# menu del usuario que inicio sesion
def menu(usuario, tipo):
    while True:
        print("\n--- MENU:", usuario, "(" + tipo + ") ---")
        print("1. Ver todos los perros")
        print("2. Adoptar un perro")
        print("3. Mis adopciones")
        if tipo == "Administrador":
            print("4. Agregar perro")
        print("0. Cerrar sesion")

        if tipo == "Administrador":
            opcion = pedir_opcion(0, 4)
        else:
            opcion = pedir_opcion(0, 3)

        if opcion == 1:
            ver_perros()
        elif opcion == 2:
            adoptar(usuario)
        elif opcion == 3:
            mis_adopciones(usuario)
        elif opcion == 4:
            agregar_perro()
        else:
            print("Sesion cerrada.")
            break


# programa principal
while True:
    print("\n--- REFUGIO PATITAS FELICES ---")
    print("1. Iniciar sesion")
    print("2. Registrarse")
    print("0. Salir")
    opcion = pedir_opcion(0, 2)

    if opcion == 1:
        resultado = iniciar_sesion()
        if resultado != None:
            menu(resultado[0], resultado[1])
    elif opcion == 2:
        registrar()
    else:
        print("Hasta pronto")
        break
