from flask import Flask, request
from controllers import owners_controller, cars_controller

app = Flask('carford')


@app.route('/owner', methods=["POST"])
def create_owner_route():
    body = request.get_json()
    return owners_controller.create_owner(body)


@app.route('/car', methods=["POST"])
def create_car_route():
    body = request.get_json()
    return cars_controller.create_car(body)


@app.route('/owner', methods=["GET"])
def get_all_owners_route():
    return owners_controller.get_all_owners()


@app.route('/car', methods=["GET"])
def get_all_cars_route():
    return cars_controller.get_all_cars()


@app.route('/car', methods=["PUT"])
def update_cars_route():
    body = request.get_json()
    return cars_controller.update_cars(body)


@app.route('/owner/<id_owner>', methods=["DELETE"])
def delete_owner_route(id_owner):
    return owners_controller.delete_owner(id_owner)


@app.route('/owner_opportunity', methods=["GET"])
def get_owners_opportunity_route():
    return owners_controller.get_owners_opportunity()


app.run()
