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
    
            else:
                print(f"No hay lugares disponibles para este tipo de vehículo: {vehicle_type}")
                continue

            placa = input('Por favor ingresa la placa del vehiculo >:')
            hour_inside = datetime.now()
            place_random = random.choice(place_free_moto if vehicle_type == 'Moto' else place_free_car)
            register_list.append({'place': place_random, 'placa': placa, 'hour_inside': hour_inside, 'Action': 'Entro'})
            for x in (name_camp_moto if vehicle_type == 'Moto' else name_camp_cars):
                if x['place'] == place_random:
                     x['available'] = False
            print(f'El registro de {vehicle_type} es el siguiente: ', register_list) 

    elif options == '2':
            vehicle_type = input("Que tipo de vehiculo es ? (1. Moto, 2. Carro): ")
            placa_pay = input("Digite la placa a cobrar: ")

            if vehicle_type == '1':
                register_list = register_motorcycle
                cont_frac = cost_frac_moto
            elif vehicle_type == '2':
                register_list = register_car
                cont_frac = cost_frac_car
                
            else:
                print('Opcion de vehiculo no valida. por favor selecione 1 o 2.')
                continue        
                #buscar la moto en el registro
            placa_encontrada = False
                
            for entry in register_list:
                if entry['placa'] == placa_pay and entry['Action'] == 'Entro':
                    hour_inside = entry['hour_inside']
                    place_out = entry['place']
                    
                    #Calcular el tiempo del parqueo
                    current_time = datetime.now()
                    delta = current_time - hour_inside
                    hour_parqueo = delta.total_seconds() / 3600
                    #Calcular el costo
                    total_costo = math.ceil(hour_parqueo) * cont_frac
                    
                    #Calcular hora y minutos de permanencia
                    hours = int(hour_parqueo)
                    minutes = (hour_parqueo - hours) * 60
                    
                    print(f'Tiempo de permanencia : {hours} horas {int(minutes)} minutos ')
                    print(f'consto total es : {total_costo} pesos')
                        
                    placa_encontrada = True
                    break
                        #Liberar el parqueadero
                if not placa_encontrada:
                    print('La placa consultada no fue encontrada.')
                else:
                    for X in (name_camp_moto if vehicle_type == '1' else name_camp_cars):
                        if x['place'] == place_out:
                            x['available'] = True
                            
                    entry['Action'] = 'Salio'
                    entry['total_costo'] = total_costo 
                    print('Registro de salida con exito.')          
                

                        
                            



           






