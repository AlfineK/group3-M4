class Vehicle:
    owner = "Group 2 LTD"
    vehicles = {"KDL001A": {"vehicle_id": "KDL001A",
                            "brand": "Toyota Prado", "current_mileage": 20000}}
    _next_id = 100

    def __init__(self, vehicle_id, mileage, brand):
        self.vehicle_id = vehicle_id
        self.mileage = mileage
        self.brand = brand
        self.driver = None

    @property
    def registration_number(self):
        return self.vehicle_id

    @registration_number.setter
    def registration_number(self, vehicle_id):
        if not vehicle_id:
            self.vehicle_id = vehicle_id
        else:
            print("Brand cannot be empty")

    @classmethod
    def _generate_id(cls):
        cls._next_id += 1
        return f"KDZ {cls._next_id}Z"

    @classmethod
    def add_vehicle(cls, vehicle):
        cls.vehicles.append(vehicle)

    @classmethod
    def create(cls, mileage, brand):
        vehicle_id = cls._generate_id()
        vehicle = cls(vehicle_id, mileage, brand)
        cls.vehicles[vehicle_id] = {"vehicle_id": vehicle_id,
                                    "brand": brand, "current_mileage": mileage}
        return vehicle

    def __repr__(self):
        return f"cls({self.vehicle_id!r},{self.mileage!r},{self.brand!r})"
