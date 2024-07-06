def menu():
    print("1.)Registrar cliente")
    print("2.)Listar clientes registrados")
    print("3.)Registrar compra")
    print("4.)Listar compras de un cliente")
    print("5.)Salir del programa")

def registrar_cliente(BD):
    nombre = input("Ingrese nombre del cliente: ")
    apellido = input("Ingrese apellido del clienete: ")
    correo = input("Ingrese el correo electronico del cliente: ")

    id_cliente = len(BD) + 1

    BD.append(
        {
            "nombre": nombre,
            "apellido": apellido,
            "ID": id_cliente,
            "correo": correo,
            "compra": []
        }
    )
    print("Se ha registrado exitosamente un nuevo cliente!")

def listar_clientes_registrados(BD):
    print("ID\t\tNombre\t\tApellido\t\tCorreo")

    for cliente in BD:
        print(f'{cliente["ID"]}\t\t{cliente["nombre"]}\t\t{cliente["apellido"]}\t\t{cliente["correo"]}')




def registar_compra(BD):
    id = int(input("Ingrese el ID del cliente: "))

    for cliente in BD:
        if cliente ["ID"] == id:
            fecha = input("Ingrese la fecha de compra (AAAA-MM-DD): ")
            compra = int(input("Ingrese el precio de la compra del cliente: "))
            puntos_acumulados = round(0.01*compra)
            cliente["compra"].append(
                {
                    "fecha": fecha,
                    "compra": compra,
                    "puntos": puntos_acumulados
                }   
            )    
        print("Se ha registrado la compra.")



        
def listar_compra(BD):
    id = int(input("Ingrese el ID del cliente: "))
    
    for cliente in BD:
        if cliente["ID"] == id:
            resumen = f'ID Socio : {id}\n'
            resumen += f'Nombre cliente: {cliente["nombre"]} {cliente["apellido"]}\n'
            resumen += f'Fecha de compra: {cliente["fecha"]} {cliente["puntos"]}\n'
            
            with open(f"RESUMEN_CLIENTE_ID{id}.txt", "w", encoding='utf-8') as archivo:
                archivo.write(resumen)
                
                print("ARCHIVO CREADO")

            break
    
