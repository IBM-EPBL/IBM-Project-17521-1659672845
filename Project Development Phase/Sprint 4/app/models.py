from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy()


def setup_db(app):
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)


def commit():
    db.session.commit()


collect = db.Table('collect',
                   db.Column('plate_number', db.Integer, db.ForeignKey('vehicles.plate_number'), primary_key=True),
                   db.Column('basket_id', db.Integer, db.ForeignKey('baskets.id'), primary_key=True),
                   db.Column('DOC', db.DateTime, primary_key=True)
                   )

complaint = db.Table('complaint',
                     db.Column('user_name', db.String, db.ForeignKey('users.user_name'), primary_key=True),
                     db.Column('basket_id', db.Integer, db.ForeignKey('baskets.id'), primary_key=True),
                     db.Column('date_of_compliant', db.DateTime, primary_key=True),
                     db.Column('compliant_message', db.String),
                     )


class Basket(db.Model):
    __tablename__ = 'baskets'
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    software_version = db.Column(db.String, nullable=False, default="0.0.0")
    wastes_height = db.Column(db.Integer, nullable=False, default=0)
    wastes = db.relationship('Waste', lazy=True, backref=db.backref('basket', lazy=True))
    software_versions = db.relationship('SoftwareVersion', lazy=True, backref=db.backref('basket', lazy=True))
    type = db.Column(db.Integer, db.ForeignKey('basketsTypes.id'), nullable=False)
    area_code = db.Column(db.Integer, db.ForeignKey('areas.code'), nullable=False)

    def save(self):
        if self.id is None:
            db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "software_version": self.software_version,
            "micro_controller": self.basketType.micro_controller,
            "level": "{}%".format(self.get_basket_level())
        }

    def set_wastes_height(self, waste_height):
        if waste_height <= (self.basketType.height - self.wastes_height):
            self.wastes_height += waste_height
            return False
        return True

    def get_waste_volume(self, height):
        return (self.length * self.width * float(height)) / 1000000

    def get_basket_level(self):
        return int((self.wastes_height / self.basketType.height) * 100)


class Area(db.Model):
    __tablename__ = "areas"
    code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    size = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.String, nullable=False)
    latitude = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    baskets = db.relationship('Basket', lazy=False, backref=db.backref('area'))
    users = db.relationship('User', backref=db.backref('area'))

    def save(self, has_key_by_default=False):
        if self.code is None or has_key_by_default:
            db.session.add(self)
        db.session.commit()

    def format(self):
        return {
            "area_code": self.code,
            "area_name": self.name,
            "area_size": self.size,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "city": self.city
        }


class User(db.Model):
    __tablename__ = 'users'
    user_name = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    DOB = db.Column(db.DateTime)
    phone = db.Column(db.String)
    area_code = db.Column(db.Integer, db.ForeignKey('areas.code'), nullable=False)
    baskets = db.relationship('Basket', secondary=complaint, lazy=True, backref=db.backref('complainants'))

    def save(self, has_key_by_default=False):
        if self.user_name is None or has_key_by_default:
            db.session.add(self)
        db.session.commit()
        return self

    def format(self):
        return {
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "gender": self.gender,
            "Date_of_birth": self.DOB
        }


class Employee(db.Model):
    __tablename__ = 'employees'
    SSN = db.Column(db.BigInteger, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String, nullable=False, unique=False)
    password = db.Column(db.String, nullable=False)
    DOB = db.Column(db.DateTime, nullable=False)
    phone = db.Column(db.String)
    vehicle = db.relationship('Vehicle', uselist=False, lazy="select", backref=db.backref('driver'))
    supervise = db.relationship("Employee")
    supervise_SSN = db.Column(db.BigInteger, db.ForeignKey('employees.SSN'), nullable=True)

    def save(self, has_key_by_default=False):
        if self.SSN is None or has_key_by_default:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "SSN": self.SSN,
            "full_name": self.full_name,
            "user_name": self.user_name,
            "date_of_birth": self.DOB,
            "phone": self.phone
        }


class Vehicle(db.Model):
    __tablename__ = "vehicles"
    plate_number = db.Column(db.Integer, primary_key=True)
    container_size = db.Column(db.Float)
    tank_level = db.Column(db.Float)
    tank_size = db.Column(db.Float)
    employee_SSN = db.Column(db.BigInteger, db.ForeignKey('employees.SSN'))
    baskets = db.relationship('Basket', secondary=collect, lazy=True, backref=db.backref('baskets'))

    def save(self, has_key_by_default=False):
        if self.plate_number is None or has_key_by_default:
            db.session.add(self)
        db.session.commit()

    def format(self):
        return {
            "plate_number": self.plate_number,
            "container_size": self.container_size,
            "tank_level": self.tank_level,
            "tank_size": self.tank_size,
            "driver": self.driver.format() if self.driver else {}
        }


class Waste(db.Model):
    __tablename__ = "wastes"
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Float)
    type = db.Column(db.String)
    DOC = db.Column(db.DateTime, nullable=False)
    basket_id = db.Column(db.Integer, db.ForeignKey('baskets.id'), nullable=True)

    def save(self, has_key_by_default=False):
        if self.id is None or has_key_by_default:
            db.session.add(self)
            db.session.add(self.basket)
        db.session.commit()
        return self

    def format(self):
        return {
            "basket_id": self.basket_id,
            "size": self.size,
            "type": self.type,
            "date_of_creation": self.DOC
        }

    def delete(self):
        db.session.commit()


class SoftwareVersion(db.Model):
    __tablename__ = "software_versions"
    version = db.Column(db.String(), primary_key=True)
    file = db.Column(db.LargeBinary())
    date = db.Column(db.DateTime, server_default=db.func.now())
    basket_id = db.Column(db.Integer, db.ForeignKey('baskets.id'), nullable=True, primary_key=True)

    def save(self, has_key_by_default=False):
        if self.version is None or has_key_by_default:
            db.session.add(self)
        db.session.commit()
        return self

    def format(self, status):
        return {
            "version": self.version,
            "date": self.date,
            "status": status
        }

    def delete(self):
        db.session.commit()


class BasketType(db.Model):
    __tablename__ = "basketsTypes"
    id = db.Column(db.Integer, primary_key=True)
    length = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    micro_controller = db.Column(db.String, nullable=False)
    basket = db.relationship('Basket', lazy=True, backref=db.backref('basketType', lazy=True))

    def save(self):
        if self.id is None:
            db.session.add(self)
        db.session.commit()
        return self

    def format(self):
        return {    
            "name": "{}*{}*{}/{}".format(self.length, self.width, self.height, self.micro_controller),
            "value": self.id
        }
