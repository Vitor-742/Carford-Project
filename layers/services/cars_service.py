from services import connection


def create_car_service(body):
    connection.mycursor.execute(
        f"SELECT * FROM owners WHERE name = '{body['owner_name']}'"
    )
    myresult = connection.mycursor.fetchone()
    if not myresult:
        return {
            'status': 400,
            'messagem': 'proprietário não encontrado'
        }
    if myresult[2] == 3:
        return {
            'status': 400,
            'mensagem': 'somente 3 carros são válidos por pessoa'
        }
    connection.mycursor.execute(
        f"""UPDATE owners SET qtycars = '{myresult[2]+1}'
        WHERE id = '{myresult[0]}'"""
    )
    connection.mydb.commit()
    connection.mycursor.execute(
        """INSERT INTO cars (owner, color, type)
        VALUES (%s, %s, %s)""",
        [myresult[0], body['color'], body['type']]
    )
    connection.mydb.commit()
    return {
        'status': 201,
        'mensagem': 'criado'
    }

def get_all_cars_service():
    try:
        connection.mycursor.execute(f"SELECT * FROM cars")
        myresult = connection.mycursor.fetchall()
        mycars = []
        for o in myresult:
            mycars.append({
                'id': o[0],
                'owner_id': o[1],
                'car_color': o[2],
                'car_type': o[3]
            })
        return {
            'status': 200,
            'mensagem': 'OK',
            'cars': mycars
        }
    except:
        return {
            'status': 500
        }

def update_cars_service(body):
    try:
        connection.mycursor.execute(
            f"""UPDATE cars
            SET color = '{body['color']}',
            type = '{body['type']}'
            WHERE id = '{body['id']}'"""
        )
        connection.mydb.commit()
        return {
            'status': 200,
            'mensagem': 'OK',
            'owners': 'atualizado'
        }
    except:
        return {
            'status': 500
        }
