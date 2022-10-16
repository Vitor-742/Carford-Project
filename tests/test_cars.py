import pytest
from layers.controllers.cars_controller import (
    create_car,
    update_cars,
)

def test_create_car_without_owner_name():
    'Para um body sem nome do proprietario deve ser retornado um erro'
    fake_body = {
        'color': 'yellow',
        'type': 'sedan'
    }
    assert create_car(fake_body)['mensagem'] == 'Nome do proprietário é obrigatório'

def test_create_car_without_color():
    'Para um body sem color deve ser retornado um erro'
    fake_body = {
        'owner_name': 'vitor',
        'type': 'sedan'
    }
    assert create_car(fake_body)['mensagem'] == 'cor do carro é obrigatório'

def test_create_car_without_type():
    'Para um body sem tipo deve ser retornado um erro'
    fake_body = {
        'owner_name': 'vitor',
        'color': 'yellow'
    }
    assert create_car(fake_body)['mensagem'] == 'tipo do carro é obrigatório'

def test_create_car_with_color_wrong():
    'Para um body com cor fora do padrao deve ser retornado um erro'
    fake_body = {
        'owner_name': 'vitor',
        'color': 'red',
        'type': 'sedan'
    }
    assert create_car(fake_body)['mensagem'] == 'cor do carro precisa ser uma das especificadas'

def test_create_car_with_type_wrong():
    'Para um body com tipo fora do padrao deve ser retornado um erro'
    fake_body = {
        'owner_name': 'vitor',
        'color': 'yellow',
        'type': 'fusca'
    }
    assert create_car(fake_body)['mensagem'] == 'tipo do carro precisa ser um dos especificados'

def test_update_car_withou_id():
    'Para um body sem id deve ser retornado um erro'
    fake_body = {
        'color': 'yellow',
        'type': 'fusca'
    }
    assert update_cars(fake_body)['mensagem'] == 'id do carro é obrigatório'

def test_update_car_without_color():
    'Para um body sem color deve ser retornado um erro'
    fake_body = {
        'id': '2',
        'type': 'sedan'
    }
    assert update_cars(fake_body)['mensagem'] == 'cor do carro é obrigatório'

def test_update_car_without_type():
    'Para um body sem tipo deve ser retornado um erro'
    fake_body = {
        'id': '2',
        'color': 'yellow'
    }
    assert update_cars(fake_body)['mensagem'] == 'tipo do carro é obrigatório'

def test_update_car_with_color_wrong():
    'Para um body com cor fora do padrao deve ser retornado um erro'
    fake_body = {
        'id': '2',
        'color': 'red',
        'type': 'sedan'
    }
    assert update_cars(fake_body)['mensagem'] == 'cor do carro precisa ser uma das especificadas'

def test_update_car_with_type_wrong():
    'Para um body com tipo fora do padrao deve ser retornado um erro'
    fake_body = {
        'id': '2',
        'color': 'yellow',
        'type': 'fusca'
    }
    assert update_cars(fake_body)['mensagem'] == 'tipo do carro precisa ser um dos especificados'