import datetime

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Alta de chofer")
        print("2. Modificar chofer")
        print("3. Eliminar chofer")
        print("4. Listar choferes")
        print("5. Cambio masivo de zona por año de ingreso")
        print("6. Depuración por antigüedad")
        print("7. Cola por zona de trabajo")
        print("0. Salir")
        op = input("Seleccione opción: ")
        if op == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            legajo = input("Legajo: ")
            fecha_ingreso = 
            nro_camion = input("Número de camión: ")
            zona = input("Zona de trabajo: ")
            chofer = #llamada a funcion que guarda chofer y le paso por paramteros los datos ingresados.
            #llamada a funcion que da alta a chofer, le paso por paramteros los datos ingresados.
        elif op == "2":
            legajo = input("Legajo del chofer a modificar: ")
            print("Dejar en blanco los campos que no desea modificar.")
            nombre = input("Nuevo nombre: ")
            apellido = input("Nuevo apellido: ")
            nro_camion = input("Nuevo número de camión: ")
            zona = input("Nueva zona de trabajo: ")
            cambios = {} #Diccionario para almacenar los cambios. Si el usuario ingresa un campo, se agrega al diccionario. Si deja en blanco, no se agrega.
            if nombre: cambios['nombre'] = nombre               #Si el usuario ingresa un valor, entonces el if es True y en cambios se agrega el campo.
            if apellido: cambios['apellido'] = apellido         #A ese campo se le asigna el valor ingresado por el usuario.
            if nro_camion: cambios['nro_camion'] = nro_camion   #Si el usuario deja en blanco, el if es False y no se agrega nada al diccionario.
            if zona: cambios['zona'] = zona
            #Aca va una llamada a la funcion para modificar chofer, le paso el legajo y el diccionario de cambios.
        elif op == "3":
            legajo = input("Legajo del chofer a eliminar: ")
            #Aca va una llamada a la funcion para eliminar chofer, le paso el legajo.
        elif op == "4":
            #Aca va una llamada a la funcion para listar choferes.
        elif op == "5":
            anio = int(input("Año de ingreso: "))
            nueva_zona = input("Nueva zona de trabajo: ")
            #Aca va una llamada a la funcion para cambiar masivamente la zona, le paso el año y la nueva zona.
        elif op == "6":
            #Aca va una llamada a la funcion para depurar antigüedad, le paso los años (30 por defecto).
        elif op == "7":
            zona = input("Zona de trabajo: ")
            #Aca va una llamada a la funcion para generar la cola de choferes por zona, le paso la zona.
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()