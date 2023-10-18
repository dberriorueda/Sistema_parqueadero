from datetime import datetime
import random
import math

print('////BIENVENIDO AL SISTEMA DE PARQUEADEROS GALVIS////')
print('----------------------------------------------------')

camp_cars = int(input('Ingresa la cantidad de parqueaderos para carros: '))
camp_motorcycles = int(input('Ingresa la cantidad de parqueaderos para motos: '))

name_camp_cars = []
name_camp_moto = []

while len(name_camp_cars) < camp_cars:
    name_camp_cars.append({'place': str(input('Ingresa el nombre del campo del parqueadero de carro: ')), 'available': True})

while len(name_camp_moto) < camp_motorcycles:
    name_camp_moto.append({'place': str(input('Ingresa el nombre del campo del parqueadero de moto: ')), 'available': True})

cost_frac_car = 2000
cost_frac_moto = 1000

register_car = []
register_motorcycle = []

while True:
    place_free_moto = [x['place'] for x in name_camp_moto if x['available']]
    place_free_car = [x['place'] for x in name_camp_cars if x['available']]
    
    print('Lugares disponibles:', place_free_car, place_free_moto)

    print("¿QUÉ OPCIÓN DESEAS REALIZAR?")
    print("1. Registrar vehiculo nuevo.")
    print("2. Registrar salida de vehiculo.")
    print("3. Salir.")
    options = input("Seleccione una opción:")
    
    # Validar que el dato no sean letras
    if options.isdigit() and options not in ['1', '2', '3']:
        print("Opcion no valida. por favor opcion 1, 2 o 3")
    
    # Opción para registrar Moto
    if options == '1':
        if len(place_free_moto) > 0 or len(place_free_car) > 0:
            type_vehicle= input('¿QUÉ TIPO DE VEHÍCULO DESEAS REGISTRAR?\n1. Moto\n2. Carro\nOpción >:')
            
            if type_vehicle == '1' and place_free_moto:
                 vehicle_type = 'Moto'
                 register_list = register_motorcycle
            elif type_vehicle == '2' and place_free_car:
                 vehicle_type = 'Carro'
                 register_list = register_car
            if vehicle_type and register_list:
                placa = input('POR FAVOR INGRESA LA PLACA DEL VEHÍCULO >:')
                hour_inside = datetime.now()
                place_random = random.choice(place_free_moto if vehicle_type == 'Moto' else place_free_car)
                register_list.append({'place': place_random, 'placa': placa, 'hour_inside': hour_inside, 'Action': 'Entro'})
                for x in (name_camp_moto if vehicle_type == 'Moto' else name_camp_cars):
                    if x['place'] == place_random:
                        x['available'] = False
                print(f'El registro de {vehicle_type} es el siguiente: ', register_list)
            else:
                print(f"No hay lugares disponibles para este tipo de vehículo: {vehicle_type}")

        elif options == '2':
            placa_pay = input("Digite la placa a cobrar: ")
            vehicle_type = input("Que tipo de vehiculo es ? (1. Moto, 2. Carro): ")
            if vehicle_type == '1':
                #buscar la moto en el registro
                for entry in register_motorcycle:
                    if entry['placa'] == placa_pay and entry['Action'] == 'Entro':
                        hour_inside = entry['hour_inside']
                        place_out = entry['place']
                        #Calcular el tiempo del parqueo
                        delta = datetime.now()- hour_inside
                        hour_parqueo = delta.total_seconds() / 3600
                        #Calcular el costo
                        total_costo = math.ceil(hour_parqueo) * cost_frac_moto
                        print("Tu valor a pagar de parqueo es: ", total_costo)
                        #Liberar el parqueadero
                        for x in name_camp_moto:
                            if x['place'] == place_out:
                                x['available'] = True
                        #Marcar la moto como salida
                        entry['Action'] = 'Salio'
                        entry['total_costo'] = total_costo
                        print("Registro de salida con exito.")
                        break
            else:
                print("La placa consultada no fue encontrada.")
        elif vehicle_type== '2':
            for entry in register_motorcycle:
                    if entry['placa'] == placa_pay and entry['Action'] == 'Entro':
                        hour_inside = entry['hour_inside']
                        place_out = entry['place']
                        #Calcular el tiempo del parqueo
                        delta = datetime.now()- hour_inside
                        hour_parqueo = delta.total_seconds() / 3600
                        #Calcular el costo
                        total_costo = math.ceil(hour_parqueo) * cost_frac_car
                        print("Tu valor a pagar de parqueo es: ", total_costo)
                        #Liberar el parqueadero
                        for x in name_camp_cars:
                            if x['place'] == place_out:
                                x['available'] = True
                        #Marcar la moto como salida
                        entry['Action'] = 'Salio'
                        entry['total_costo'] = total_costo
                        print("Registro de salida con exito.")
                        pass
        elif options == '3':
            break
        else:
            print("Opcion no valida. por favor seleccione una opcion valida. ")      

                        
                            



           






