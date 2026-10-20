class Customer:
    counter = 1

    def __init__(self, name, driver_id, payment=0):
        self.name = name
        self.driver_id = driver_id
        self.payment = payment
        self.customer_id = Customer.counter
        Customer.counter += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip().title()

    @property
    def driver_id(self):
        return self._driver_id

    @driver_id.setter
    def driver_id(self, value):
        if not value or not str(value).strip():
            raise ValueError("Driver ID is required")
        self._driver_id = str(value).strip()

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, value):
        if float(value) < 0:
            raise ValueError("Payment cannot be negative")
        self._payment = float(value)

    def add_payment(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be more than 0")
        self.payment = self.payment + amount

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "driver_id": self.driver_id,
            "payment": self.payment,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["driver_id"], data.get("payment", 0))

    def __str__(self):
        return f"{self.customer_id}. {self.name} | Driver ID: {self.driver_id} | Paid: {self.payment}"
