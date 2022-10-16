import pytest
from layers.controllers.owners_controller import (
    create_owner,
    delete_owner,
)

def test_create_owner_without_name():
    'Para um body sem name deve ser retornado um erro'
    fake_body = {'age': 10}
    assert create_owner(fake_body)['mensagem'] == 'Nome é obrigatório'

def test_create_owner_with_short_name():
    'Para um name abaixo de 3 letras deve ser retornado um erro'
    fake_body = {'name': 'le'}
    assert create_owner(fake_body)['mensagem'] == 'Nome precisa de no mínimo 3 caracteres'

def test_delete_owner_with_id_not_numerical():
    'Para um id nao numerico e retornado um erro'
    fake_id = 'one'
    assert delete_owner(fake_id)['mensagem'] == 'somente numeros sao validos'