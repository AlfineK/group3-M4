from models.vehicle import Vehicle

class Driver:
    _accounts={}
    _next_id=10001

    def __init__(self,driver_name,mileage,driver_id,vehicle_id=None,):
        self.driver_name=driver_name
        self.mileage=mileage
        self.vehicle_id=vehicle_id if vehicle_id is not None else []
        self.driver_id=driver_id

    @property
    def driver_name(self):
        return self._driver_name

    @driver_name.setter
    def driver_name(self,value):
        if not value or not value.strip():
            raise ValueError("Driver name is required")
        self._driver_name=value.strip()

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self,value):
        if value <=0:
            raise ValueError("Mileage should be a positive number and not zero")
        self._mileage=value

    def to_dict(self):
        return{
            "driver_name":self.driver_name,
            "mileage":self.mileage,
            "driver_id":self.driver_id,
            "vehicle_id":(self.vehicle_id.to_dict()  if self.vehicle_id else None)

        }


    @classmethod
    def _generate_id(cls):
        while True:
            cls._next_id +=1
            driver_id=f"Driver {cls._next_id}"
            if driver_id not in cls._accounts:
                return driver_id

    @classmethod
    def create(cls):
        driver_id=cls._generate_id
        account=cls(driver_id)
        cls._accounts[driver_id]=account
        return account

    @classmethod
    def from_dict(cls,data):
        vehicles_data=data.get("vehicle_ids",[])
        target_id=data.get("selected_vehicle_id")
        chosen_vehicle=None

        if target_id:
            matching_dict=next((v for v in vehicles_data
                                if isinstance(v,dict) and v.get("vehicle_id") ==target_id),None)
            if matching_dict:
                chosen_vehicle=Vehicle.from_dict(matching_dict)
        return cls(
            driver_name=data.get("driver_name"),
            mileage=data.get("mileage"),
            driver_id=data.get("driver_id"),
            vehicle_id=chosen_vehicle

        )

    @classmethod
    def get(cls,driver_id):
        return cls._accounts[driver_id]

    @classmethod
    def all(cls):
        return list(cls._accounts.values())

    def __repr__(self):
        return f"Driver(driver_name={self._driver_name!r},driver_id={self.driver_id!r},vehicle_id={self.vehicle_id!r},mileage={self.mileage})"
    

    