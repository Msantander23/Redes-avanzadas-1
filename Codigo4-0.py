#Creado por Matias Santander
#Fecha 04'10'2024

import os
import ipaddress

def cargar_campus(nombre_archivo="campus.txt"):
    """Carga la lista de campus desde un archivo."""
    if not os.path.exists(nombre_archivo):
        campus_inicial = ["Zona Core", "Campus Uno", "Campus Matriz", "Sector Outsourcing"]
        with open(nombre_archivo, "w") as file:
            for c in campus_inicial:
                file.write(c + "\n")
        return campus_inicial
    else:
        with open(nombre_archivo, "r") as file:
            return [line.strip() for line in file if line.strip()]

def guardar_campus(campus_lista, nombre_archivo="campus.txt"):
    """Guarda la lista de campus en un archivo."""
    with open(nombre_archivo, "w") as file:
        for c in campus_lista:
            file.write(c + "\n")

campus = cargar_campus()

def mostrar_menu():
    print("¿Qué quiere hacer? \n")
    print("1. Ver los dispositivos.")
    print("2. Ver los campus.")
    print("3. Añadir dispositivo.")
    print("4. Añadir campus.")
    print("5. Borrar dispositivo.")
    print("6. Borrar campus.")
    print("7. Salir.")

while True:
    os.system("clear")
    mostrar_menu()
    selector = input("Elija una opción: ")

    # Menú opción 1: Ver los dispositivos
    if selector == "1":
        os.system("clear")
        y = 1
        print("Elegir un campus \n")
        for item in campus:
            print(f"{y}. {item}")
            y += 1
        selector = input("\nElija una opción: ")
        try:
            x = int(selector) - 1
        except ValueError:
            x = -1
        if 0 <= x < len(campus):
            os.system("clear")
            try:
                with open(campus[x] + ".txt", "r") as file:
                    for item in file:
                        print(item.strip())
            except FileNotFoundError:
                print("Archivo no encontrado.")
        else:
            print("Opción no válida.")

    elif selector == "2":
        os.system("clear")
        y = 1
        print("Campus disponibles: \n")
        for item in campus:
            print(f"{y}. {item}")
            y += 1

    elif selector == "3":
        os.system("clear")
        y = 1
        servicios = []
        print("¿Dónde agregar nuevo dispositivo? \n")
        for item in campus:
            print(f"{y}. {item}")
            y += 1
        selector = input("\nElija una opción: ")
        try:
            x = int(selector) - 1
        except ValueError:
            x = -1
        if 0 <= x < len(campus):
            os.system("clear")
            with open(campus[x] + ".txt", "a") as file:
                print("Elija un dispositivo: \n1. Router. \n2. Switch. \n3. Switch multicapa. \n4. PC. \n5. Servidor. \n6. Impresora.")
                variable1 = input("Elija su opción: ")
                os.system("clear")
                print("Agregue el nombre de su dispositivo")
                variable2 = input("Agregue su nombre: ")
                while True:
                    print("¿Confirma este nombre? \n1. Sí \n2. No")
                    variable3 = input("Introduzca su respuesta: ")
                    if variable3 == "1":
                        print("Nombre confirmado.")
                        break
                    elif variable3 == "2":
                        print("Nombre no confirmado. Intente nuevamente.")
                        variable2 = input("Agregue su nombre: ")
                    else:
                        print("Opción no válida.")
                
                if variable1 == "1": 
                    while True:
                        ip_address = input("Introduzca la dirección IP del router: ")
                        try:
                            ipaddress.ip_address(ip_address)  
                            break
                        except ValueError:
                            print("Dirección IP no válida. Inténtelo de nuevo.")
                    
                    file.write(f"\n---------------------------------\nRouter: {variable2}\nIP: {ip_address}")
                    print("Router agregado con éxito.")
                    
                elif variable1 == "2": 
                    file.write(f"\n---------------------------------\nSwitch: {variable2}")
                    while True:
                        vlan = input("Añada una VLAN (o escriba 'salir' para terminar): ")
                        if vlan.lower() == 'salir':
                            break
                        servicios.append(f"VLAN: {vlan}")
                    file.write("\n" + "\n".join(servicios))
                    print("Switch agregado con éxito.")
                    
                elif variable1 == "3": 
                    file.write(f"\n---------------------------------\nSwitch multicapa: {variable2}")
                    while True:
                        vlan = input("Añada una VLAN (o escriba 'salir' para terminar): ")
                        if vlan.lower() == 'salir':
                            break
                        servicios.append(f"VLAN: {vlan}")
                    file.write("\n" + "\n".join(servicios))
                    print("Switch multicapa agregado con éxito.")
                    
                elif variable1 == "4": 
                    while True:
                        ip_address = input("Introduzca la dirección IP de la PC: ")
                        try:
                            ipaddress.ip_address(ip_address)
                            break
                        except ValueError:
                            print("Dirección IP no válida. Inténtelo de nuevo.")
                    file.write(f"\n---------------------------------\nPC: {variable2}\nIP: {ip_address}")
                    print("PC agregada con éxito.")
                    
                elif variable1 == "5":  
                    while True:
                        ip_address = input("Introduzca la dirección IP del servidor: ")
                        try:
                            ipaddress.ip_address(ip_address)
                            break
                        except ValueError:
                            print("Dirección IP no válida. Inténtelo de nuevo.")
                    file.write(f"\n---------------------------------\nServidor: {variable2}\nIP: {ip_address}")
                    print("Servidor agregado con éxito.")
                    
                elif variable1 == "6": 
                    while True:
                        ip_address = input("Introduzca la dirección IP de la impresora: ")
                        try:
                            ipaddress.ip_address(ip_address)
                            break
                        except ValueError:
                            print("Dirección IP no válida. Inténtelo de nuevo.")
                    file.write(f"\n---------------------------------\nImpresora: {variable2}\nIP: {ip_address}")
                    print("Impresora agregada con éxito.")
                else:
                    print("Opción de dispositivo no válida.")
        else:
            print("Opción no válida.")

    elif selector == "4":
        os.system("clear")
        nuevo_campus = input("Introduzca el nombre del nuevo campus: ").strip()
        if nuevo_campus:
            if nuevo_campus not in campus:
                campus.append(nuevo_campus)
                guardar_campus(campus)
                print(f"Nuevo campus '{nuevo_campus}' añadido.")
            else:
                print("El campus ya existe.")
        else:
            print("El nombre del campus no puede estar vacío.")

    elif selector == "5":
        os.system("clear")
        print("Seleccionar campus para borrar un dispositivo: \n")
        y = 1
        for item in campus:
            print(f"{y}. {item}")
            y += 1
        selector = input("\nElija una opción: ")
        try:
            x = int(selector) - 1
        except ValueError:
            x = -1
        
        if 0 <= x < len(campus):
            os.system("clear")
            try:
                with open(campus[x] + ".txt", "r") as file:
                    dispositivos = file.readlines()
                    if not dispositivos:
                        print("No hay dispositivos para mostrar.")
                    else:
                        print("Dispositivos disponibles:\n")
                        for i, dispositivo in enumerate(dispositivos):
                            print(f"{i + 1}. {dispositivo.strip()}")
                        
                        selector = input("\nElija el dispositivo a borrar: ")
                        try:
                            dispositivo_a_borrar = int(selector) - 1
                        except ValueError:
                            dispositivo_a_borrar = -1
                        
                        if 0 <= dispositivo_a_borrar < len(dispositivos):
                            
                            print(f"¿Está seguro de que desea borrar: {dispositivos[dispositivo_a_borrar].strip()}? (s/n)")
                            confirmacion = input("Respuesta: ")
                            
                            if confirmacion.lower() == 's':
                               
                                dispositivos.pop(dispositivo_a_borrar)
                               
                                with open(campus[x] + ".txt", "w") as file_write:
                                    file_write.writelines(dispositivos)
                                print("Dispositivo eliminado con éxito.")
                            else:
                                print("Eliminación cancelada.")
                        else:
                            print("Opción no válida.")
            except FileNotFoundError:
                print("Archivo no encontrado.")
        else:
            print("Opción no válida.")
    elif selector == "6":
        os.system("clear")
        y = 1
        print("Seleccionar campus a borrar: \n")
        for i, item in enumerate(campus):
            print(f"{i + 1}. {item}")
        selector = input("Elija una opción: ")
        try:
            x = int(selector) - 1
        except ValueError:
            x = -1

        if 0 <= x < len(campus):
            campus_a_borrar = campus[x]
            print(f"¿Está seguro de que desea borrar el campus '{campus_a_borrar}'? (s/n)")
            confirmacion = input("Respuesta: ")
            if confirmacion.lower() == 's':
                campus.pop(x)
                guardar_campus(campus)
                archivo_dispositivos = campus_a_borrar + ".txt"
                if os.path.exists(archivo_dispositivos):
                    os.remove(archivo_dispositivos)
                print("Campus eliminado.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Opción no válida.")
    elif selector == "7":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida")

    input("Presione Enter para continuar ")
    
