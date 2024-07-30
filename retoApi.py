import requests
import os 

while True:  
    API_KEY = '329609649b9a685bcda0311a'
    BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        rates = data['conversion_rates']
        
        moneda = input("tu moneda: ").upper()
        if moneda == "S":
            os.system("clear")
            print("!Adios")
            break
        cantidad = float(input("cantidad: "))
        monedaNew = input("moneda que quieres: ").upper()
        tasa_moneda = rates[moneda]
        tasa_monedaNew = rates[monedaNew]
        #paso la moneda a dolares 
        cant_usd = cantidad / tasa_moneda

        #convertir dolares a la monedaNew
        cant_monedaNew = cant_usd * tasa_monedaNew
        os.system("clear")
        print(f"{"\033[92m"} {cantidad} {moneda} son aproximadamente {cant_monedaNew:.2f} {monedaNew} {"\033[0m"}")
    else:
        print(f"Error: {response.status_code}")
        print(f"{"\033[91m"} algo salio mal {"\033[0m"}")