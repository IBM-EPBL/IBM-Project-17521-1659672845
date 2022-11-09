# Waste management system Backend
## Getting Started
### Installing Dependencies
####python3.7
we are using python as a backend language
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
##### Windows
[python3.7](https://www.python.org/downloads/windows/)
#### virtual environment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:
```shell script
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.
#### key dependencies
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [SQLALCHEMY](https://www.sqlalchemy.org/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)

## Setup Database
## Running the Server 
## API References
### Getting Started
### Error Handling
### Endpoints
#### GET /areas
- ##### General 
    * Return a list of areas objects and number of total areas
- ##### Sample
    * Request
    ```shell script
    curl https://wastes-management.herokuapp.com/api/areas
    ```
    * Response
    ```json
    {
        "areas": [
            {
                "area_code": 22,
                "area_name": "الحي الثاني",
                "area_size": 100.0,
                "city": "مدينة الشروق",
                "latitude": "342342",
                "longitude": "42342"
            },
            {
                "area_code": 33,
                "area_name": "الحي الثالث",
                "area_size": 100.0,
                "city": "مدينة الشروق",
                "latitude": "45345",
                "longitude": "423"
            },
            {
                "area_code": 44,
                "area_name": "الحي الرابع",
                "area_size": 120.0,
                "city": "مدينة الشروق",
                "latitude": "45344635",
                "longitude": "423423"
            }
        ],
        "total_areas": 3
    }
    ```
  
#### GET /areas/{area_code}
- ##### General 
    * Return a specific area object by area code
- ##### Sample
    * Request
    ```shell script
    curl https://wastes-management.herokuapp.com/api/areas/22
    ```
    * Response
    ```json
    {
        "area": {
            "area_code": 22,
            "area_name": "الحي الثاني",
            "area_size": 100.0,
            "city": "مدينة الشروق",
            "latitude": "342342",
            "longitude": "42342"
        }
    }
    ```
  
#### GET /areas/{area_code}/baskets
- ##### General 
    * Return a list of baskets objects based on a specific area, 
    * The object that return include list of baskets, total number of basket in this area
- ##### Sample
    * Request
    ```shell script
    curl https://wastes-management.herokuapp.com/api/areas/22/baskets
    ```
    * Response
    ```json
    {
        "baskets": [
            {
                "basket_height": 90,
                "basket_length": 40,
                "basket_width": 40,
                "id": 6,
                "latitude": "534535534",
                "level": "0%",
                "longitude": "435345",
                "software_version": "v2.0"
            },
            {
                "basket_height": 90,
                "basket_length": 40,
                "basket_width": 40,
                "id": 7,
                "latitude": "5345345",
                "level": "0%",
                "longitude": "5345",
                "software_version": "v2.0"
            },
            {
                "basket_height": 90,
                "basket_length": 40,
                "basket_width": 40,
                "id": 5,
                "latitude": "534534",
                "level": "83%",
                "longitude": "534534534",
                "software_version": "v2.0"
            }
        ],
        "total_baskets": 3
    }
    ```

#### GET /areas/{area_code}/users
- ##### General 
    * Return a list of users objects based on a specific area, 
    * The object that return include list of users, total number of users in this area
- ##### Sample
    * Request
    ```shell script
    curl https://wastes-management.herokuapp.com/api/areas/22/users
    ```
    * Response
    ```json
    {
        "total_users": 0,
        "users": []
    }
    ```

#### POST /areas
- #####General 
    * Insert new area in the system using the submitted longitude, latitude and area code
    * Return success message and area object if created successfully
- #####Sample
    * Request
    ```shell script
    curl -X POST https://wastes-management.herokuapp.com/api/areas -H "Content-Type: application/json" -d '{ "area_code": 33, "longitude": 4234432, "latitude": 324242 }'
    ```
    * Response
    ```json
    {
        "area": {
            "area_code": 55,
            "area_name": "الحي الخامس",
            "area_size": 100.0,
            "city": "مدينة الشروق",
            "latitude": "43424",
            "longitude": "423434"
        },
        "success": true
    }
    ```

#### Get /baskets
- ##### General 
    * Return a list of baskets objects and number of total basket
- ##### Sample
    * Request
    ```shell script
    curl https://wastes-management.herokuapp.com/api/baskets
    ```
    * Response
    ```json
    {
        "baskets": [
            {
                "basket_height": 90,
                "basket_length": 40,
                "basket_width": 40,
                "id": 1,
                "latitude": "42342423",
                "level": "33%",
                "longitude": "534534534",
                "software_version": "v1.0"
            },
            {
                "basket_height": 90,
                "basket_length": 40,
                "basket_width": 40,
                "id": 2,
                "latitude": "345353535",
                "level": "44%",
                "longitude": "53453453",
                "software_version": "v1.0"
            },
            {
                "basket_height": 90,
                "basket_length": 40,
                "basket_width": 40,
                "id": 3,
                "latitude": "34535345",
                "level": "88%",
                "longitude": "545353",
                "software_version": "v1.0"
            }
        ],
        "total_baskets": 9
    }
    ```
#### Get /baskets/{basket_id}
- ##### General 
    * return a specific basket by id
- ##### Sample
    * Request
    ```shell script
    curl https://wastes-management.herokuapp.com/api/baskets/1
    ```
    * Response
    ```json
    {
        "basket": {
            "basket_height": 90,
            "basket_length": 40,
            "basket_width": 40,
            "id": 1,
            "latitude": "42342423",
            "level": "33%",
            "longitude": "534534534",
            "software_version": "v1.0"
        }
    }
    ```

#### GET /baskets/{basket_id}/wastes
- #####General 
    * Return a list of wastes object based on a specific basket, 
    * the object that return include basket id, wastes, total size of wastes that generated by this basket
- #####Sample
    * Request
    ```shell script
    curl https://wastes-management.herokuapp.com/api/baskets/1/wastes
    ```
    * Response
    ```json
    {
        "basket_id": 1,
        "total_size": 0.048,
        "wastes": [
            {
                "basket_id": 1,
                "date_of_creation": "Mon, 25 Jan 2021 18:42:35 GMT",
                "size": 0.016,
                "type": "bio"
            },
            {
                "basket_id": 1,
                "date_of_creation": "Mon, 25 Jan 2021 18:42:46 GMT",
                "size": 0.016,
                "type": "bio"
            },
            {
                "basket_id": 1,
                "date_of_creation": "Mon, 25 Jan 2021 18:42:50 GMT",
                "size": 0.016,
                "type": "bio"
            }
        ]
    }
    ```

#### POST /baskets
- #####General 
    * Create new basket using the submitted longitude, latitude and area code
    * you can set basket height, width, length, version manually, 
    * Return success message and basket object if created successfully
- #####Sample
    * Request
    ```shell script
    curl -X POST https://wastes-management.herokuapp.com/api/baskets -H "Content-Type: application/json" -d '{ "area_code": 33, "longitude": 4234432, "latitude": 324242 }'
    ```
    ```shell script
    curl -X POST https://wastes-management.herokuapp.com/api/baskets -H "Content-Type: application/json" -d '{ "area_code": 33, "longitude": 4234432, "latitude": 324242, "basket_height: 120, "basket_width": 50, "basket_length": 50, "basket_version": "v4.0" }'
    ```
    * Response
    ```json
    {
        "basket": {
            "basket_height": 90,
            "basket_length": 40,
            "basket_width": 40,
            "id": 10,
            "latitude": "324242",
            "level": "0%",
            "longitude": "4234432",
            "software_version": "v1.0"
        },
        "success": true
    }
    ```

#### PATCH /baskets
- #####General 
    * Update the basket software version
    * Return the number of updated baskets
- #####Sample
    * Request
    ```shell script
    curl -X PATCH https://wastes-management.herokuapp.com/api/baskets -H "Content-Type: application/json" -d '{ "software_version": "V2.0"}'
    ```
    * Response
    ```json
    {
        "baskets_update": 10
    }
    ```
#### PATCH /baskets/{basket_id}
- #####General 
    * Update basket level by submitted basket level
    * Return success message
- #####Sample
    * Request
    ```shell script
    curl -X PATCH https://wastes-management.herokuapp.com/api/baskets/1 -H "Content-Type: application/json" -d '{ "level": 0}'
    ```
    * Response
    ```json
    {
        "success": true
    }
    ```
#### DELETE /baskets/{basket_id}
- #####General 
    * Update the basket software version
    * Return the number of updated baskets
- #####Sample
    * Request
    ```shell script
    curl -X DELETE https://wastes-management.herokuapp.com/api/baskets/1
    ```
    * Response
    ```json
    {
        "success": true
    }
    ```
#### GET /users
- ##### General
    * Return a list of user object
- ##### Sample
    * Request
    ```shell script
    curl https://wastes-management.herokuapp.com/api/users
    ```
    * Response
    ```json
    {
        "user": [
            {
                "Date_of_birth": null,
                "email": "ahemdhostam@gamil.com",
                "first_name": "ahemd",
                "gender": "male",
                "last_name": "hosam",
                "user_name": "ahmed"
            },
            {
                "Date_of_birth": null,
                "email": "mahmoudamr@gamil.com",
                "first_name": "mahmoud",
                "gender": "male",
                "last_name": "amr",
                "user_name": "mahmoud2"
            },
            {
                "Date_of_birth": null,
                "email": "ahemd.esmail@gamil.com",
                "first_name": "ahmed",
                "gender": "male",
                "last_name": "esmail",
                "user_name": "ahmed2"
            }
        ]
    }
    ``` 

#### GET /users/{user_name}
- ##### General
    * Return specific user object based on user_name
- ##### Sample
    * Request
    ```shell script
    curl https://wastes-management.herokuapp.com/api/users/meladsamuel
    ```
    * Response
    
#### GET /users
- ##### General
    * Create new user by submitted user name, first name, last name, email, password, gender
    * Return success message and user object
- ##### Sample
    * Request
    ```shell script
    curl -X POST https://wastes-management.herokuapp.com/api/users -H "Content-Type: application/json" -d '{ "user_name": "ali", "first_name": "ali", "last_name": "emad", "email": "ali.emad@gamil.com", "password":"123", "gender": "male", "area_code": 22 }    ```
    * Response
    ```json
    {
        "success":true,
        "user": {
            "Date_of_birth":null,
            "email":"ali.emad@gamil.com",
            "first_name":"ali",
            "gender":"male",
            "last_name":"emad",
            "user_name":"ali"
        }
    }
    ```
#### GET /vehicles
- ##### General 
    * Return a list of vehicles objects
- ##### Sample
    * Request
    ```shell script
    curl https://wastes-management.herokuapp.com/api/vehicles
    ```
    * Response
    ```json

    ```
#### GET /vehicles/{plate_number}
- ##### General 
    * Return a list of vehicles objects
- ##### Sample
    * Request
    ```shell script
    curl https://wastes-management.herokuapp.com/api/vehicles
    ```
    * Response
    ```json

    ```
#### POST /vehicles
- ##### General
    * Insert new vehicles in the system by submitted plate number, container size, tank size, employee ssn
    * Return success message and list of vehicles object
- ##### Sample
    * Request
    ```shell script
    curl -X POST https://wastes-management.herokuapp.com/api/vehicles -H "Content-Type: application/json" -d '{"plate_number": 543, "container_size": 6.0, "tank_size": 100.0, "employee_ssn": 29854364445354}'
    ```
    * Response
    ```json
    {
        "success": true,
        "vehicle": [
            {
                "container_size": 6.0,
                "driver": {
                    "SSN": 29854364445354,
                    "date_of_birth": "Sun, 11 Oct 1998 00:00:00 GMT",
                    "full_name": "مصطفي صابر محمد",
                    "phone": "011432523482",
                    "user_name": "mostafa"
                },
                "plate_number": 543,
                "tank_level": null,
                "tank_size": 100.0
            }
        ]
    }
    ```