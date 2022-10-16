from services import cars_service

car_colors = [
        'yellow',
        'blue',
        'gray'
    ]

car_types = [
        'sedan',
        'hatch',
        'convertible'
    ]

def create_car(body):
    if 'owner_name' not in body:
        return {
            'status': 400,
            'mensagem': 'Nome do proprietário é obrigatório'
            }
    if 'color' not in body:
        return {
            'status': 400,
            'mensagem': 'cor do carro é obrigatório'
            }
    if 'type' not in body:
        return {
            'status': 400,
            'mensagem': 'tipo do carro é obrigatório'
            }
    if body['color'] not in car_colors:
        return {
            'status': 400,
            'mensagem': 'cor do carro precisa ser uma das especificadas'
            }
    if body['type'] not in car_types:
        return {
            'status': 400,
            'mensagem': 'tipo do carro precisa ser um dos especificados'
            }
    return cars_service.create_car_service(body)

def get_all_cars():
    return cars_service.get_all_cars_service()

def update_cars(body):
    if 'id' not in body:
        return {
            'status': 400,
            'mensagem': 'id do carro é obrigatório'
            }
    if 'color' not in body:
        return {
            'status': 400,
            'mensagem': 'cor do carro é obrigatório'
            }
    if 'type' not in body:
        return {
            'status': 400,
            'mensagem': 'tipo do carro é obrigatório'
            }
    if body['color'] not in car_colors:
        return {
            'status': 400,
            'mensagem': 'cor do carro precisa ser uma das especificadas'
            }
    if body['type'] not in car_types:
        return {
            'status': 400,
            'mensagem': 'tipo do carro precisa ser um dos especificados'
            }
    return cars_service.update_cars_service(body)
