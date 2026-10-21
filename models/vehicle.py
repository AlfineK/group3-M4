class Vehicle:
    owner = "Group 2 LTD"
    vehicles = {}
    _next_id = 100

    def __init__(self, vehicle_id, mileage, brand, driver=None):
        self.vehicle_id = vehicle_id
        self.mileage = mileage
        self.brand = brand
        self.driver = driver
        Vehicle.vehicles[self.vehicle_id] = self

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        if not value or not str(value).strip():
            raise ValueError("Vehicle ID is required")
        self._vehicle_id = str(value).strip()

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if int(value) < 0:
            raise ValueError("Mileage cannot be negative")
        self._mileage = int(value)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not value or not value.strip():
            raise ValueError("Brand is required")
        self._brand = value.strip().title()

    @classmethod
    def _generate_id(cls):
        while True:
            vid = f"KDZ {cls._next_id}Z"
            cls._next_id += 1
            if vid not in cls.vehicles:
                return vid

    @classmethod
    def create(cls, mileage, brand):
        return cls(cls._generate_id(), mileage, brand)

    @classmethod
    def get(cls, vehicle_id):
        return cls.vehicles.get(vehicle_id)

    @classmethod
    def all(cls):
        return list(cls.vehicles.values())

    def to_dict(self):
        return {
            "vehicle_id": self.vehicle_id,
            "brand": self.brand,
            "current_mileage": self.mileage,
            "driver_id": self.driver.driver_id if self.driver else None,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            vehicle_id=data["vehicle_id"],
            mileage=data.get("current_mileage", data.get("mileage", 0)),
            brand=data["brand"],
        )

    def __str__(self):
        return f"{self.vehicle_id} | {self.brand} | {self.mileage} km"

    def __repr__(self):
        return f"Vehicle({self.vehicle_id!r}, {self.mileage!r}, {self.brand!r})"