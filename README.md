PROJETO CARFORD

Projeto desenvolvido por Vitor Campos


DEPOIS DE CLONAR O PROJETO ->

Crie um ambiente virtual: source carford_venv/bin/activate

Instale as dependências: pip install -r requirements.txt

Inicie o banco de dados com docker-compose: docker-compose up -d

Inicie o app e use as rotas: python3 layers/server.py

Para rodar os testes: python3 -m pytest tests/

Para sair do ambiente virtual: deactivate


ENDPOINTS DA APLICAÇÃO

GET /owner - retorna todos os proprietários registrados

GET /car - retorna todos os carros registrados

GET /owner_opportunity - retorna os propritários que ainda não tem carros, para opotunidade de venda

POST /owner - cria novo proprietário
    body {
        'name': 'fulano'
    }

POST /car - cria novo carro
    body {
        'owner_name': 'fulano',
        'color': 'yellow',
        'type': 'convertible'
    }

PUT /car - atualiza o registro de um carro
    body {
        'id': '1',
        'color': 'yellow',
        'type': 'hatch'
    }

DELETE /owner/'id_owner' - deleta o proprietário com 'id_owner'