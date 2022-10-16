from services import connection

def create_owner_service(body):
    try:
        connection.mycursor.execute(f"INSERT INTO owners (name) VALUES (%s)", [body['name']])
        connection.mydb.commit()
        return {
            'status': 201,
            'mensagem': 'criado'
        }
    except:
        return {
            'status': 500
        }


def get_all_owners_service():
    try:
        connection.mycursor.execute(f"SELECT * FROM owners")
        myresult = connection.mycursor.fetchall()
        myowners = []
        for o in myresult:
            myowners.append({
                'id': o[0],
                'name': o[1],
                'cars_quantity': o[2]
            })
        return {
            'status': 200,
            'mensagem': 'OK',
            'owners': myowners
        }
    except:
        return {
            'status': 500
        }

def delete_owner_service(id):
    connection.mycursor.execute(
        f"""DELETE FROM owners
        WHERE id = '{id}'"""
    )
    connection.mydb.commit()
    try:
        connection.mycursor.execute(
            f"""DELETE FROM owners
            WHERE id = '{id}'"""
        )
        connection.mydb.commit()
        return {
            'status': 200,
            'mensagem': 'OK',
            'owners': 'deletado'
        }
    except:
        return {
            'status': 500
        }

def get_owners_opportunity_service():
    try:
        connection.mycursor.execute(f"SELECT * FROM owners WHERE qtycars = 0")
        myresult = connection.mycursor.fetchall()
        myowners = []
        for o in myresult:
            myowners.append({
                'id': o[0],
                'name': o[1],
                'cars_quantity': o[2]
            })
        return {
            'status': 200,
            'mensagem': 'OK',
            'owners_opportunity': myowners
        }
    except:
        return {
            'status': 500
        }