import funciones
funciones.registrar_pedido
funciones.hojaderutA
funciones.listar_pedido

opcionmenu=None
while True:
    print ("ClaeanWasser")
    print("-----------------")
    print("1.Registrar pedido")
    print("2.Listar todos los pedidos")
    print("3.Imprimit hoja de ruta")
    print("4.Buscar pedido por ID")
    print("5.Salir")

    if opcionmenu == "1":
        print ("Registrando pedido")
        registrar_pedido
        ubicacion= input ("Ingrese su Comuna")
        
       
    

    elif opcionmenu=="2":
        print("Listando Pedidos")
        print (listar_pedido)
        print(idPedido)
        

    elif opcionmenu =="3":

        print("Imprimiendo Hoja de ruta", hojaderutA)
        



    elif opcionmenu =="4":
        pedidoid=input("Ingrese el ID de su pedido")
        


else:
        opcionmenu == "5"
        print("Saliendo del programa")
        break





       

