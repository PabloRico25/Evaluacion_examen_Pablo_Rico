productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}
stock = {
    '8475HD': {'precio': 387990, 'unidades': 10},
    '2175HD': {'precio': 327990, 'unidades': 4},
    'JjfFHD': {'precio': 424990, 'unidades': 1},
    'fgdxFHD': {'precio': 664990, 'unidades': 21},
    '123FHD': {'precio': 290890, 'unidades': 32},
    '342FHD': {'precio': 444990, 'unidades': 7},
    'GF75HD': {'precio': 749990, 'unidades': 2},
    'UWU131HD': {'precio': 349990, 'unidades': 1},
    'FS1230HD': {'precio': 249990, 'unidades': 0}
}
def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total += stock.get(modelo, {}).get("unidades", 0)
    print(f"El stock es: {total}")

def busqueda_precio(p_min, p_max):
    resultado = []
    for modelo, info in stock.items():
        if p_min <= info["precio"] <= p_max and info["unidades"] > 0:
            marca = productos[modelo][0]
            resultado.append(f"{marca}--{modelo}")
    if resultado:
        print("Los notebooks entre los precios de busqueda son:", sorted(resultado))
    else:
        print("No existen notebooks en ese rango de precios.")
def busqueda_RAM(Rmin,Rmax):
    Resultado = []
    for precio, inf in productos.items():
        if  Rmin<= inf[0]<=Rmax and inf[4]>0:
            marca=stock[precio][0]
        Resultado.append(f"{marca}--{precio}")
    if Resultado:
        print("Los notebooks entre las cantidades de RAM de busqueda son:", sorted(Resultado))
    else:
        print("No existen notebooks en ese rango de precios.")
def eliminar_producto(modelo):
    if modelo in productos and modelo in stock:
        del productos[modelo]
        del stock[modelo]
        return True
    return False
def menu():
    while True:
        print("Bienvenido al portal de Pybooks")
        print("")
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por RAM y precio.")
        print("3. Eliminar producto.")
        print("4. Salir.")
        try:
            op = int(input("Ingrese opcion: "))
        except ValueError:
            print("Debe seleccionar una opcion invalida")
            continue

        if op == 1:
            marca = input("Ingrese marca a consultar(Asus,Acer,Dell,Hp): ")
            stock_marca(marca)
        elif op == 2:
            while True:
                try:
                    print("seleccione busqueda:")
                    print("1.-RAM")
                    print("2.-precio")
                    opc2=int(input(""))
                except ValueError:
                    print("ingrese una  opcion dentro de los parametros entregados ")
                if opc2==1:
                    while True:
                        try:  
                            Rmin = int(input("Ingrese una cantidad minima de RAM (4/8/12/16): "))
                            if Rmin!=4 and Rmin!=8 and Rmin!=12 and Rmin!=16:
                                Rmin=input("Ingrese la cantidad de RAM minima disponible (4/8/12/16):") 
                            else:
                                print(f"Su RAM minima de busqueda es: {Rmin}")
                            Rmax = int(input("Ingrese una cantidad maxima de RAM (4/8/12/16): "))
                            if Rmax==Rmin:
                                Rmax=int(input("La RAM maxima debe ser distinta a la RAM minima entregada"))
                            elif Rmax!=4 and Rmax!=8 and Rmax!=12 and Rmax!=16:
                                Rmax=input("Ingrese la cantidad de RAM minima disponible (4/8/12/16):")
                            else:
                                print(f"Su RAM minima de busqueda es: {Rmax}")  
                            break    
                        except ValueError:
                            print("Debe ingresar valores enteros solicitados")
                    busqueda_RAM(Rmin, Rmax)
                else:
                    opc2==2
                    while True:
                        try:
                            pmin = int(input("Ingrese precio mínimo: "))
                            pmax = int(input("Ingrese precio máximo: "))
                            break
                        except ValueError:
                            print("Debe ingresar valores enteros")
                    busqueda_precio(pmin, pmax)
        elif op == 3:
            while True:
                modelo = input("Ingrese modelo a eliminar: ")
                if eliminar_producto(modelo):
                    print("Producto eliminado con exito!!")
                else:
                    print("El modelo no existe!!")
                continuar = input("Desea eliminar otro producto (s/n)?: ").lower()
                if continuar != "s":
                    break
        elif op == 4:
            print("Programa finalizado....")
            break
        else:
            print("Debe seleccionar una opcion valida!!")
menu()
