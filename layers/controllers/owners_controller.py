from services import owners_service

def create_owner(body):
    if 'name' not in body:
        return {
            'status': 400,
            'mensagem': 'Nome é obrigatório'
            }
    if len(body['name']) < 3:
        return {
            'status': 400,
            'mensagem': 'Nome precisa de no mínimo 3 caracteres'
            }
    return owners_service.create_owner_service(body)

def get_all_owners():
    return owners_service.get_all_owners_service()

def delete_owner(id):
    if not id.isnumeric():
        return {
            'status': 400,
            'mensagem': 'somente numeros sao validos'
        }
    return owners_service.delete_owner_service(id)

def get_owners_opportunity():
    return owners_service.get_owners_opportunity_service()