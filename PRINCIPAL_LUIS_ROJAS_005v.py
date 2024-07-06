from FUNCIONES_LUIS_ROJAS_005v import *


print("¡Bienvenido a la cadena de supermercados TODOAHORRO!")

BD = [
    {
        "nombre": "Juanito",
        "apellido": "Perez",
        "ID": 1,
        "correo": "juanperez@ejemplo",
        "compras": [{'fecha': '06-09-2024', 'puntos': 10}]
        
    }
]

while True:

    menu()

    opcion = input("Ingrese una opcion: ")
    
    if opcion == "1":
        registrar_cliente(BD)

    elif opcion == "2":
        listar_clientes_registrados(BD)

    elif opcion == "3":
        registar_compra(BD)

    elif opcion == "4":
        listar_compra(BD)

    elif opcion == "5":
        print("Saliendo del rpograma.....")
        break