from flask import Blueprint, jsonify, request, abort, Response, send_file
from app.models import Basket, User, Waste, Vehicle, Employee, commit, Area, SoftwareVersion, BasketType
from app.validate import validate
import json
from datetime import datetime
from io import BytesIO

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def index():
    return jsonify({"message": "the api is working"})


@api.route('baskets')
def get_baskets():
    baskets = Basket.query.all()
    baskets_list = [basket.format() for basket in baskets]
    return jsonify({
        "baskets": baskets_list,
        "total_baskets": len(baskets_list)
    })


@api.route('baskets/<int:basket_id>')
def get_basket(basket_id):
    basket = Basket.query.get(basket_id)
    return jsonify({
        "basket": basket.format()
    })


@api.route('baskets/<int:basket_id>/wastes')
def get_wastes_of_basket(basket_id):
    basket = Basket.query.get(basket_id)
    wastes = [waste.format() for waste in basket.wastes]
    total_size = 0.0
    for waste in wastes:
        total_size = total_size + waste['size']
        print(type(waste['size']), waste['size'])
        print(total_size)
    print(total_size)
    return jsonify({
        "basket_id": basket.id,
        "total_size": total_size,
        "wastes": wastes
    })


@api.route('baskets', methods=['POST'])
def add_new_basket():
    data = request.json
    roles = ['longitude', 'latitude', 'area_code']
    abort(400) if not validate(roles, data) else None
    longitude = data['longitude']
    latitude = data['latitude']
    area_code = data['area_code']
    type_id = data['type']
    area = Area.query.get(area_code)
    if not area:
        abort(422)
    basket_type = BasketType.query.get(type_id)
    if not basket_type:
        abort(422)
    basket = Basket(longitude=longitude, latitude=latitude, area=area, basketType=basket_type).save()

    return jsonify({
        "success": True,
        "basket": basket.format()
    })


@api.route('baskets/<int:basket_id>', methods=['DELETE'])
def delete_baskets(basket_id):
    basket = Basket.query.get(basket_id)
    basket = basket.delete() if basket else basket
    return jsonify({
        'success': bool(basket)
    })


@api.route('baskets', methods=['PATCH'])
def update_all_baskets():
    data = request.json
    software_version = data['software_version']
    baskets = Basket.query.update({Basket.software_version: software_version})
    commit()
    return jsonify({
        "baskets_update": baskets
    })


@api.route('baskets/<int:basket_id>', methods=['PATCH'])
def update_the_basket(basket_id):
    data = request.json
    basket_level = data['level']
    if basket_level is None:
        abort(400)
    try:
        basket = Basket.query.get(basket_id)
        basket.wastes_height = basket_level
        basket.save()
    except:
        abort(422)

    return jsonify({
        "success": True,
    })


@api.route('areas')
def get_areas():
    areas = Area.query.all()
    areas_list = [area.format() for area in areas]

    return jsonify({
        "total_areas": len(areas_list),
        "areas": areas_list
    })


@api.route('areas/<int:area_code>')
def get_area(area_code):
    area = Area.query.get(area_code)
    return jsonify({
        "area": area.format()
    })


@api.route('areas/<int:area_code>/baskets')
def get_basket_belong_to_area(area_code):
    baskets = Area.query.get(area_code).baskets
    baskets_list = [basket.format() for basket in baskets]
    return jsonify({
        "total_baskets": len(baskets_list),
        "baskets": baskets_list
    })


@api.route('areas/<int:area_code>/users')
def get_user_belong_to_area(area_code):
    users = Area.query.get(area_code).users
    users_list = [user.format() for user in users]
    return jsonify({
        "total_users": len(users_list),
        "users": users_list
    })


@api.route('areas', methods=['POST'])
def insert_new_area():
    data = request.json
    roles = ['area_code', 'area_name', 'area_size', 'longitude', 'latitude', 'city']
    if not validate(roles, data):
        abort(422)
    code = data['area_code']
    name = data['area_name']
    size = data['area_size']
    longitude = data['longitude']
    latitude = data['latitude']
    city = data['city']
    area = Area(code=code, name=name, size=size, longitude=longitude, latitude=latitude, city=city)
    area.save(True)
    return jsonify({
        "success": True,
        "area": area.format()
    })


@api.route('vehicles')
def get_vehicles():
    vehicles = Vehicle.query.all()
    vehicles_list = [vehicle.format() for vehicle in vehicles]
    return jsonify({
        "vehicles": vehicles_list
    })


@api.route('vehicles/<int:vehicle_plate_no>')
def get_vehicle(vehicle_plate_no):
    vehicle = Vehicle.query.get(vehicle_plate_no)
    return jsonify({
        "vehicle": vehicle.format()
    })


@api.route('vehicles', methods=['POST'])
def create_vehicle():
    data = request.json
    roles = ['plate_number', 'container_size', 'tank_size', 'employee_ssn']
    if not validate(roles, data):
        abort(400)
    plate_number = data['plate_number']
    container_size = data['container_size']
    tank_size = data['tank_size']
    employee_ssn = data['employee_ssn']
    driver = Employee.query.get(employee_ssn)
    if not driver:
        abort(404)
    # try:
    vehicle = Vehicle(plate_number=plate_number, container_size=container_size, tank_size=tank_size, driver=driver)
    vehicle.save(True)
    return jsonify({
        "success": True,
        "vehicle": [vehicle.format()]
    })
    # except:
    #     abort(422)


@api.route('employees')
def get_employees():
    employees = Employee.query.all()
    employees_list = [employee.format() for employee in employees]
    return jsonify({
        "total_employees": len(employees_list),
        "employees": employees_list
    })


@api.route('employees/<int:employee_ssn>')
def get_employee(employee_ssn):
    employee = Employee.query.get(employee_ssn)
    return jsonify({
        "employee": employee.format()
    })


@api.route("employees", methods=['POST'])
def create_new_employee():
    data = request.json
    ssn = data['ssn']
    full_name = data['full_name']
    user_name = data['user_name']
    password = data['password']
    date_of_birth = data['data_of_birth']
    phone = data['phone']
    print(ssn)
    if not ssn or not full_name or not user_name or not password or not date_of_birth or not phone:
        abort(400)
    employee = Employee(SSN=ssn, full_name=full_name, user_name=user_name, password=password, DOB=date_of_birth,
                        phone=phone).save(True)
    return jsonify({
        "success": True,
        # "employee": [employee.format()]
    })


@api.route("employees", methods=['PATCH'])
def update_supervisor():
    # TODO update the supervisor for all employee
    return ''


@api.route('employees/<int:employee_ssn>', methods=['DELETE'])
def delete_employee(employee_ssn):
    employee = Employee.query.get(employee_ssn)
    if employee is None:
        abort(404)
    employee.update()
    return jsonify({
        "success": True
    })


@api.route('users')
def get_all_users():
    users = User.query.all()
    users_list = [user.format() for user in users]
    return jsonify({"user": users_list})


@api.route('users', methods=['POST'])
def create_new_user():
    data = request.json
    user_name = data['user_name']
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    password = data['password']
    gender = data['gender']
    area = data['area_code']
    area = Area.query.get(area)
    if not area:
        abort(404)
    roles = ['user_name', 'first_name', 'last_name', 'email', 'password', 'gender']
    abort(400) if not validate(roles, data) else None
    try:
        user = User(user_name=user_name, first_name=first_name, last_name=last_name, email=email, password=password,
                    gender=gender, area=area).save(True)
        return jsonify({
            "success": True,
            'user': user.format()
        })
    except:
        abort(422)


@api.route('wastes')
def get_waste():
    data = request.args
    basket_id = data.get('basket_id', 0, int)
    wastes = Waste.query.all() if not basket_id else Waste.query.filter_by(basket_id=basket_id).all()
    wastes_list = [waste.format() for waste in wastes]
    total_size = 0
    for waste in wastes_list:
        total_size += +waste['size']

    return jsonify({
        "total_wastes_size": total_size,
        "wastes": wastes_list,
    })


@api.route('wastes', methods=['POST'])
def insert_new_waste():
    data = request.json
    basket = Basket.query.get(data['basket_id'])
    is_full = basket.set_wastes_height(data['waste_height'])
    if is_full:
        abort(422)
    waste_size = basket.get_waste_volume(data['waste_height'])
    waste = Waste(size=waste_size, type='bio', DOC=datetime.utcnow(), basket=basket).save()
    return jsonify({
        "basket_level": basket.get_basket_level(),
        "waste": waste.format()
    })


@api.route('wastes', methods=['DELETE'])
def delete_waste():
    # waste = Waste.query.filter_by(type='bio').delete()
    # db.session.commit()
    waste = Waste.query.all()
    print(waste)

    return ''


@api.route('test', methods=['POST', "GET"])
def test():
    data = request.json
    return jsonify({
        "value": data['value']
    })


@api.route("/baskets_types")
def get_basket_type():
    types_of_baskets = BasketType.query.all()
    type_list = [type_of_basket.format() for type_of_basket in types_of_baskets]
    return jsonify({
        "types": type_list
    })


@api.route("/baskets_types", methods=["POST"])
def create_basket_type():
    data = request.json
    length = data["length"]
    height = data["height"]
    width = data["width"]
    micro_controller = data["micro_controller"]
    roles = ['length', 'height', 'width']
    abort(400) if not validate(roles, data) else None
    try:
        basket_type = BasketType(length=length, height=height, width=width, micro_controller=micro_controller).save()
        return jsonify({
            "success": True,
            'Type': basket_type.format()
        })
    except:
        abort(422)


@api.route('/baskets/<int:basket_id>/versions')
def get_basket_software_version(basket_id):
    basket = Basket.query.get(basket_id)
    software_versions = SoftwareVersion.query.filter_by(basket_id=basket_id).order_by(SoftwareVersion.date.desc()).all()
    list_software_version = []
    status = 'update'
    for software_version in software_versions:
        if software_version.version == basket.software_version:
            status = 'rollback'
            list_software_version.append(software_version.format('current'))
            continue
        list_software_version.append(software_version.format(status))
    return jsonify({
        "software_versions": list_software_version,
        "current_version": basket.software_version
    })


@api.route("/software_versions/<string:version>")
def get_file(version):
    software = SoftwareVersion.query.get(version)
    file_name = "{}.bin".format(software.version)
    return send_file(BytesIO(software.file), attachment_filename=file_name, as_attachment=True)


@api.route("/software_versions", methods=["POST"])
def post_file():
    file = request.files['file']
    update_type = request.form.get("update_type", None)
    basket_id = request.form.get("basket_id", None)
    basket = Basket.query.get(basket_id)
    last_version = SoftwareVersion.query.filter_by(basket_id=basket_id).order_by(SoftwareVersion.date.desc()).first()
    if last_version:
        major, minor, patch = last_version.version.split(".")
        if update_type == "patch":
            patch = int(patch) + 1
        elif update_type == "minor":
            minor = int(minor) + 1
            patch = 0
        elif update_type == "major":
            major = int(major) + 1
            patch = 0
            minor = 0
        else:
            abort(422)
        print(last_version.version.split())
        version = "{}.{}.{}".format(major, minor, patch)
    else:
        version = "0.1.0"
    print(version)
    print(last_version)
    software_version = SoftwareVersion(version=version, file=file.read(), basket=basket)
    software_version.save(True)
    return jsonify({
        "success": True,
        "version": software_version.version
    }), 201
