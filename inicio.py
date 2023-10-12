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
    place_free_moto = [x['place'] for x in name_camp_moto if x['available'] == True]
    place_free_car = [x['place'] for x in name_camp_cars if x['available'] == True]
    
    print('Lugares disponibles:', place_free_car, place_free_moto)

    print("¿QUÉ OPCIÓN DESEAS REALIZAR?")
    print("1. Registrar vehiculo nuevo.")
    print("2. Registrar salida de vehiculo.")
    options = input("Seleccione una opción:")
    
    # Validar que el dato no sean letras
    if options.isdigit() and options not in ['1', '2']:
        print("NO SE ADMITEN LETRAS, SOLO LAS OPCIONES 1 o 2")
    
    # Opción para registrar Moto
    elif options == '1':
        if len(place_free_moto) > 0 or len(place_free_car) > 0:
            type_vehicle = input('¿QUÉ TIPO DE VEHÍCULO DESEAS REGISTRAR?\n1. Moto\n2. Carro\nOpción >:')
            
            if type_vehicle.isdigit() and type_vehicle in ['1', '2']:
                if type_vehicle == '1' and len(place_free_moto) > 0:
                    # Código para registrar una moto
                    placa = str(input('POR FAVOR INGRESA LA PLACA DEL VEHÍCULO >:'))
                    hour_inside = datetime.now().strftime('%Y-%m-%d %H:%M')
                    place_random = random.choice(place_free_moto)
                    register_motorcycle.append({'place': place_random, 'placa': placa, 'hour_inside': hour_inside, 'Action': 'Entro'})

                    for x in name_camp_moto:
                        if x['place'] == place_random:
                            x['available'] = False
                    print('El registro de vehículos es el siguiente: ', register_motorcycle)

                elif type_vehicle == '2' and len(place_free_car) > 0:
                    # Código para registrar un carro
                    placa = str(input('POR FAVOR INGRESA LA PLACA DEL VEHÍCULO >:'))
                    hour_inside = datetime.now().strftime('%Y-%m-%d %H:%M')
                    place_random = random.choice(place_free_car)
                    register_car.append({'place': place_random, 'placa': placa, 'hour_inside': hour_inside, 'Action': 'Entro'})

                    for x in name_camp_cars:
                        if x['place'] == place_random:
                            x['available'] = False
                    print('El registro de vehículos es el siguiente: ', register_car)

                else:
                    print('PARQUEADERO DE MOTOS LLENO' if type_vehicle == '1' else 'PARQUEADERO DE CARROS LLENO')
            else:
                print('POR FAVOR INTRODUZCA UNA SELECCIÓN VÁLIDA')
        else:
            print('PARQUEADERO LLENO, ESPERE QUE SALGA UN VEHÍCULO')
            
    # Opción de retirar un vehículo, aquí se calculará el costo
    elif options == '2':
        # Juntar las dos listas para buscar el registro en una sola lista
        option_cash = input('POR FAVOR DIGITE EL TIPO DE VEHÍCULO A COBRAR\n1. Moto\n2. Carro\nOpción: ')

        if option_cash.isdigit() and option_cash not in ['1', '2']:
            print('NO SE ADMITEN LETRAS, SOLO LAS OPCIONES 1 o 2')

        # Registrar salida de una moto
        if option_cash == '1':
            placa_pay = str(input('POR FAVOR DIGITE LA PLACA A COBRAR: '))

            # Se valida que se encuentre la placa consultada
            if not any(x for x in register_motorcycle if x['placa'] == placa_pay and x['Action'] == 'Entro'):
                print('LA PLACA CONSULTADA NO FUE ENCONTRADA')
            else:
                hour_inside = [x['hour_inside'] for x in register_motorcycle if x['placa'] == placa_pay and x['Action'] == 'Entro']
                place_out = [x['place'] for x in register_motorcycle if x['placa'] == placa_pay and x['Action'] == 'Entro']

                # Calcular tiempo de cobro
                hour_now = datetime.now()
                entry_time = datetime.strptime(hour_inside[0], '%Y-%m-%d %H:%M')
                time_difference = hour_now - entry_time
                hours_parked = time_difference.total_seconds() / 3600
                
                if option_cash == '1':
                    total = hours_parked * cost_frac_moto
                elif option_cash == '2':
                    total = hours_parked * cost_frac_car    
                                
                # Calcular tiempo de cobro

                print('Tu valor a pagar de parqueo es => ', total)

                # Convertir el tiempo de parqueo a un entero para poderlo multiplicar por el costo
                total = math.ceil(total)
                total = total * cost_frac_moto
                print('Tu valor a pagar de parqueo es => ', total)

                # Liberar parqueadero
                for x in name_camp_moto:
                    if x['place'] == str(place_out[0]):
                        x['available'] = True
                print('for', name_camp_moto, place_out)

                # Actualizar volante de salida con hora de salida y pago total para
                for x in register_car:
                    if x['placa'] == placa_pay:
                        x['hour_out'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                        x['pay_all'] = total
                        x['Action'] = 'salio'
                        

                        print('los vehiculos registrados son los siguientes: ', register_car)
                        

                    else:
                        print("POR FAVOR INTRODUZCA UNA SELECCION VALIDA")
                            



           






