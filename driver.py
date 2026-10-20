class Driver:
    __next__=10001


    def __init__(self,driver_name,mileage,vehicle_id,driver_id):
        self.driver_name=driver_name
        self.mileage=mileage
        self.vehicle_id=vehicle_id
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

    