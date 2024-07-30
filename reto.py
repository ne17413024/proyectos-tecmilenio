import os
while True:
    diccionario = { 'mxn-usd': 0.054, 'mxn-eur': 0.050, 'usd-mxn': 18.43, 'usd-eur': 0.92, 'eur-mxn': 20.01, 'eur-usd': 1.09 }
    
    moneda = input("moneda que tienes: ").lower()
    if moneda == "s":
        print("adios")
        break 
    cantidad = float(input("cantidad que deseas cambiar: "))
    monedanew  = input("moneda que deseas cambiar: ").lower()
    clave = "de:" + moneda + " - " + "a:" + monedanew + " ="
    os.system("clear")
    print(f"{"\033[92m"} obtendrias:  {clave}  {cantidad * diccionario[moneda + "-" + monedanew]} {"\033[0m"}")
    #print(f"{"\033[92m"} {cantidad} {moneda} son aproximadamente {cant_monedaNew:.2f} {monedaNew} {"\033[0m"}")






