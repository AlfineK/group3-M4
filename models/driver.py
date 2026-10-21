from .vehicle import Vehicle


class Driver:
    _accounts = {}
    _next_id = 10001

    def __init__(self, driver_name, mileage=1000, driver_id=None, vehicle=None):
        self.driver_name = driver_name
        self.mileage = mileage
        self.driver_id = driver_id if driver_id else self._generate_id()
        self.vehicle = vehicle
        Driver._accounts[self.driver_id] = self

    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self, value):
        if not value or not value.strip():
            raise ValueError("Driver name is required")
        self._driver_name = value.strip().title()

    @property
    def driver_id(self):
        return self._driver_id

    @driver_id.setter
    def driver_id(self, value):
        if not value or not str(value).strip():
            raise ValueError("Driver ID is required")
        self._driver_id = str(value).strip()

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value <= 0:
            raise ValueError("Mileage must be positive")
        self._mileage = value

    @property
    def vehicle(self):
        return self._vehicle

    @vehicle.setter
    def vehicle(self, value):
        self._vehicle = value
        if value is not None and value.driver is not self:
            value.driver = self

    @classmethod
    def _generate_id(cls):
        while True:
            cls._next_id += 1
            did = f"DRV-{cls._next_id}"
            if did not in cls._accounts:
                return did

    @classmethod
    def create(cls, driver_name, mileage=1000, vehicle=None):
        return cls(driver_name, mileage, vehicle=vehicle)

    @classmethod
    def get(cls, driver_id):
        return cls._accounts.get(driver_id)

    @classmethod
    def all(cls):
        return list(cls._accounts.values())

    def to_dict(self):
        return {
            "driver_name": self.driver_name,
            "mileage": self.mileage,
            "driver_id": self.driver_id,
            "vehicle_id": self.vehicle.to_dict() if self.vehicle else None,
        }

    @classmethod
    def from_dict(cls, data):
        vdata = data.get("vehicle_id")
        vehicle = Vehicle.from_dict(vdata) if vdata else None
        return cls(
            driver_name=data["driver_name"],
            mileage=data["mileage"],
            driver_id=data.get("driver_id"),
            vehicle=vehicle,
        )

    def __str__(self):
        veh = self.vehicle.vehicle_id if self.vehicle else "-"
        return f"{self.driver_id} | {self.driver_name} | mileage={self.mileage} | vehicle={veh}"
    

    